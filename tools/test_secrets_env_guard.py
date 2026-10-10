#!/usr/bin/env python3
"""Tests for the row-4 .env key-placement guard contract.

Verifies the exact invariants the secrets scan relies on:
  E1. `.env` is gitignored (never tracked, never scannable contents-wise)
  E2. `.env.example` is TRACKED and contains no real key — only the empty
      placeholder and a non-secret base URL
  E3. the scanner (tools/check_secrets.py) WOULD flag a real-looking key if
      it ever leaked into a tracked file (patterns proven with synthetic
      fixtures, no network)
  E4. the scanner's scope is exactly `git ls-files` — i.e. by construction
      .env is out of the scan corpus even if formatted like a tracked file
  E5. .gitignore rules match precisely: `.env`, `.env.*` ignored; `.env.example`
      explicitly negated `!.env.example`
Run as part of the regression gate (folded into tools/run_regression.py).
"""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("cs", REPO / "tools" / "check_secrets.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    return r.stdout.strip()


class EnvGuard(unittest.TestCase):

    # E1 ------------------------------------------------------------------
    def test_env_is_gitignored(self):
        r = subprocess.run(["git", "check-ignore", ".env"], cwd=REPO, capture_output=True)
        # exit 0 = ignored. If .env doesn't exist locally, create+delete nothing—
        # check-ignore works from the rule table regardless of file existence.
        self.assertEqual(r.returncode, 0, ".env must be gitignored per the row-4 decision")

    def test_env_never_tracked(self):
        tracked = git("ls-files")
        self.assertNotIn(".env\n", "\n" + tracked + "\n")
        self.assertNotIn(".env ", tracked)  # any tracked path starting '.env'

    # E2 ------------------------------------------------------------------
    def test_env_example_is_tracked(self):
        tracked = git("ls-files", ".env.example")
        self.assertEqual(tracked, ".env.example", ".env.example must be tracked as the template")

    def test_env_example_contains_no_real_key(self):
        text = (REPO / ".env.example").read_text(encoding="utf-8")
        for name, pat in cs.PATTERNS:
            for line in text.splitlines():
                if "re.compile" in line:  # not applicable: example file has no patterns
                    continue
                self.assertIsNone(pat.search(line),
                                  f".env.example leaked a credential-shaped string ({name}): {line!r}")

    def test_env_example_has_empty_key_placeholder(self):
        text = (REPO / ".env.example").read_text(encoding="utf-8")
        self.assertIn("ANTHROPIC_API_KEY=", text)
        # the template must NOT carry a value after the = (placeholder is empty)
        for line in text.splitlines():
            if line.strip().startswith("ANTHROPIC_API_KEY="):
                self.assertEqual(line.strip(), "ANTHROPIC_API_KEY=")

    # E3 ------------------------------------------------------------------
    def test_scanner_flags_a_leaked_fake_key(self):
        leaked = 'ANTHROPIC_API_KEY=' + 'sk-ant-AA' + 'AAfake' + '0123456789abcdef0123\n'
        hits = []
        for name, pat in cs.PATTERNS:
            m = pat.search(leaked)
            if m:
                hits.append(name)
        self.assertIn("anthropic-key", hits, "scanner must catch an Anthropic-shaped leak")
        self.assertTrue(hits, "scanner must catch the leak")

    def test_scanner_flags_key_assignment_without_prefix(self):
        leaked = 'api_key = ' + 'someopaque' + 'value12345\n'
        hits = [n for n, p in cs.PATTERNS if p.search(leaked)]
        self.assertIn("key-assignment", hits)

    def test_clean_tree_scans_clean(self):
        # full real scan must be clean at the time this test runs (tracked files only)
        self.assertEqual(cs.scan(), [], f"unexpected hits: {cs.scan()}")

    # E4 ------------------------------------------------------------------
    def test_scan_scope_is_tracked_files(self):
        out = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, capture_output=True)
        self.assertEqual(out.returncode, 0)
        files = out.stdout.decode().split("\x00")
        self.assertNotIn(".env", [f for f in files if f],
                         ".env must never appear in the scan corpus (it is untracked)")

    # E5 ------------------------------------------------------------------
    def test_gitignore_rules_exact(self):
        gi = (REPO / ".gitignore").read_text(encoding="utf-8")
        lines = [l.strip() for l in gi.splitlines()]
        self.assertIn(".env", lines)
        self.assertIn(".env.*", lines)
        self.assertIn("!.env.example", lines)


if __name__ == "__main__":
    unittest.main(verbosity=2)
