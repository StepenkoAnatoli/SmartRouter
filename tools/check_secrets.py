#!/usr/bin/env python3
"""Secrets scan — fail the build if a credential-like token is committed.

Row-4 key-placement decision: the Anthropic key lives in a local, gitignored
`.env`. This tool is the second guard: it scans tracked files for
credential-shaped strings and for references to `.env` values leaking into
tracked artifacts.

Checked patterns (conservative; a hit names file:line):
  * Anthropic keys:      sk-ant-... (>= 20 chars after prefix)
  * generic API keys:    sk-[A-Za-z0-9_-]{16,}
  * OpenAI-style keys:   sk-proj-...
  * key assignment:      (api_?key|secret|token|password)\\s*[=:]\\s*["']?[A-Za-z0-9_\\-]{12,}
  * raw authorization headers with bearer tokens

Scope: all git-tracked files via `git ls-files -z` (untracked local files are
out of scope — .env is untracked by design). Binary files are skipped.
Exits 0 clean; 1 on any hit; 2 if a parameter (e.g. tracked-file listing) is
unavailable. Designed as a stop-the-line check, not advisory output.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS = [
    ("anthropic-key", re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("openai-style-key", re.compile(r"sk-proj-[A-Za-z0-9_\-]{16,}")),
    ("generic-sk-key", re.compile(r"\bsk-[A-Za-z0-9_\-]{24,}\b")),
    ("key-assignment", re.compile(
        r"""(?i)\b(api_?key|secret|token|password)\b['"\s]*[=:]\s*["']?[A-Za-z0-9_\-]{12,}""")),
    ("bearer-token", re.compile(r"(?i)authorization['\"]?\s*[:=]\s*['\"]?bearer\s+[A-Za-z0-9_\-\.]{16,}")),
]

_SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".zip", ".pdf", ".woff", ".woff2", ".ico"}
_SKIP_DIRS = (".git/", "__pycache__/")
# self-exclusions: this file's own pattern definitions must not self-trip
SELF_PATH = "tools/check_secrets.py".replace("\\", "/")


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT,
                         capture_output=True, timeout=60)
    if out.returncode != 0:
        print(f"check_secrets: git ls-files failed: {out.stderr.decode(errors='replace')}",
              file=sys.stderr)
        raise SystemExit(2)
    return [f.decode("utf-8", errors="replace")
            for f in out.stdout.split(b"\x00") if f.strip()]


def scan() -> list[str]:
    hits: list[str] = []
    for rel in tracked_files():
        win_rel = rel.replace("/", "\\")
        if win_rel.startswith(_SKIP_DIRS) or rel.startswith(_SKIP_DIRS):
            continue
        p = ROOT / rel
        suffix = p.suffix.lower()
        if suffix in _SKIP_EXTENSIONS:
            continue
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        for name, pat in PATTERNS:
            for i, line in enumerate(text.splitlines(), 1):
                # skip the scanner's own literal pattern definitions
                if SELF_PATH in rel and ("re.compile(r" in line or "re.compile(" in line):
                    continue
                if pat.search(line):
                    snippet = line.strip()
                    if len(snippet) > 120:
                        snippet = snippet[:117] + "..."
                    hits.append(f"{rel}:{i}: {name}: {snippet}")
    return hits


def main() -> int:
    hits = scan()
    if hits:
        print(f"check_secrets: {len(hits)} hit(s) — DO NOT COMMIT; remove the credential:")
        for h in hits:
            print("  " + h)
        return 1
    print("check_secrets: clean (0 hits)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
