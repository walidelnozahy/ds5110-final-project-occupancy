.PHONY: data

# Download the raw snapshots into data/raw/ and check them against MANIFEST.sha256.
# Phony: it runs every time, so the checksums are checked every time.
data:
	python src/download_data.py
