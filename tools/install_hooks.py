#!/usr/bin/env python3
"""Install the repo-local pre-commit hook (regression gate).

Every fresh clone must run this once: `python tools/install_hooks.py`.
The hook makes every future commit run tools/run_regression.py (validator,
dispatcher cap suite, adapter suite, closure/report/matrix suites, secrets
scan) so cap enforcement can never silently regress. Hooks live in .git/ and
are not tracked — hence this installer.
"""
from __future__ import annotations

import shutil
import stat
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK_SRC = REPO_ROOT / "docs" / "hook_pre_commit.sh"
HOOK_DST = REPO_ROOT / ".git" / "hooks" / "pre-commit"


def main() -> int:
    if not REPO_ROOT.name or not (REPO_ROOT / ".git").is_dir():
        print("install_hooks: not a git repository — nothing to install", file=sys.stderr)
        return 2
    if not HOOK_SRC.is_file():
        print(f"install_hooks: missing {HOOK_SRC}", file=sys.stderr)
        return 2
    HOOK_DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HOOK_SRC, HOOK_DST)
    HOOK_DST.chmod(HOOK_DST.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"install_hooks: pre-commit hook installed at {HOOK_DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
