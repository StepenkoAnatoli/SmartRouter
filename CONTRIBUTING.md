# Contributing to SmartRouter

Three rules govern every change to this repo. They exist because this project is a
documented, owner-authorized evaluation pipeline — its gates are the deliverable as much
as the code is.

## 1. The pre-commit gate runs on every commit

`git config core.hooksPath .githooks` routes every commit through
[.githooks/pre-commit](.githooks/pre-commit), which:

1. stashes your worktree-only and untracked changes (index preserved),
2. runs the full regression gate (`tools/run_regression.py` — currently **10 checks**:
   skills validator, dispatcher suite, adapter suite, pilot-close, task persistence,
   task crosscheck, pilot-report, arm-matrix, secrets/env-guard, secrets scan),
3. restores your worktree, and refuses the commit on any failure.

The gate validates the **staged tree** (HEAD + index), not your dirty worktree — what
lands is what was tested.

- Setup on a fresh clone: `python tools/install_hooks.py` (or
  `git config core.hooksPath .githooks`).
- `--no-verify` bypasses the hook locally; the CI workflow
  ([.github/workflows/regression-gate.yml](.github/workflows/regression-gate.yml)) runs the
  same gate server-side on every push to `main` and every pull request, so a bypassed commit
  still fails CI. Do not bypass the hook to "fix later" — that is what CI failure records are.
- If the hook refuses your commit, fix the cause. Do not weaken a test's assertion to get a
  green gate.

## 2. Secrets live in `.env`, never in the repo

- Copy [.env.example](.env.example) to `.env` and paste the Anthropic key there by hand.
- `.env` is gitignored; [tools/check_secrets.py](tools/check_secrets.py) scans every
  **tracked** file for credential-shaped strings and is part of the gate — a pasted key
  anywhere tracked fails your commit/push.
- Never echo key values into chat, logs, issues, or commit messages. Rotate immediately if
  one leaks.
- Egress goes to `https://api.anthropic.com` **only** — [tools/dispatch_adapter.py](tools/dispatch_adapter.py)
  hard-refuses any other endpoint before any HTTP is attempted.

## 3. Evaluation artifacts are append-only and honestly labeled

- Ledger lines (`tools/pilot_ledger.jsonl`, gitignored) are never edited after the fact;
  corruptions are disclosed by the report tools, not smoothed over.
- Every document that records a decision carries explicit status labels
  (RATIFIED / PENDING / PROPOSED) and provenance for who signed it. Keep that discipline:
  if you change an evaluation contract, you change the label with it.
- The `--task-store` state files (`tools/task_state/`, gitignored) back the cross-check
  ([tools/task_crosscheck.py](tools/task_crosscheck.py)): it flags any task whose persisted
  counters disagree with the ledger so a mid-restart crash cannot under-report spend.

## Quick start

```bash
python tools/install_hooks.py        # wire the pre-commit gate
python tools/run_regression.py       # confirm the full gate is green on your clone
cp .env.example .env                 # then paste your key into .env by hand
```
