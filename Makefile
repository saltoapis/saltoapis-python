SHELL = /bin/bash

REPORTS_DIR ?= .reports

#
# Common methodology based targets
#
.PHONY: prepare
prepare:

.PHONY: sanity-check
sanity-check:
	bazel build //:pyproject
	diff pyproject.toml bazel-bin/pyproject.toml

.PHONY: build
build:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install .

.PHONY: test
test:

.PHONY: release
release:

.PHONY: clean
clean:

.PHONY: gen-files
gen-files:
	@scripts/gen-files.sh
