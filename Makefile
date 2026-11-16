# Use whichever Python is on the PATH: `python` inside a virtual environment
# (Mac, Linux and Windows), `python3` on a Mac without one.
# Override with: make data PYTHON=/path/to/python
PYTHON ?= $(shell command -v python 2>/dev/null || command -v python3)

.PHONY: data

# Download the raw snapshots into data/raw/ and check them against MANIFEST.sha256.
data:
	$(PYTHON) src/download_data.py
