# Convenience targets. `make setup` is the one-command onboarding.

SHELL := /bin/bash

.PHONY: setup gate hooks check clean-proof

## setup: clone (optional URL arg), wire the pre-commit gate, PROVE it fires
##   make setup                       # current checkout
##   make setup REPO=<clone-url> DEST=<dir>
REPO ?=
DEST ?=
setup:
	bash tools/setup_machine.sh $(if $(REPO),$(REPO) $(DEST),)

## gate: run the full regression gate (same thing the hook and CI run)
gate:
	python tools/run_regression.py

## hooks: wire the pre-commit gate only (no proof run)
hooks:
	python tools/install_hooks.py

## check: secrets scan only
check:
	python tools/check_secrets.py
