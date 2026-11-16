"""Download the Inside Airbnb Boston snapshots into data/raw/ and check them.

Run it with `make data` (or `python src/download_data.py`).

MANIFEST.sha256 is the list of files we expect, with a checksum for each.
For every file in it, this script:
  1. skips the file if it is already in data/raw/ and its checksum matches,
  2. otherwise downloads it from Inside Airbnb,
  3. if that fails or the checksum is wrong, downloads our copy from the
     GitHub release instead,
  4. stops with an error if no source gives a file with the right checksum.

It only uses the Python standard library, so it works before
`pip install -r requirements.txt`.
"""

import hashlib
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "MANIFEST.sha256"

PORTAL = "https://data.insideairbnb.com/united-states/ma/boston"
RELEASE = (
    "https://github.com/walidelnozahy/ds5110-final-project-occupancy"
    "/releases/download/data-v1"
)

# Where each file sits inside a snapshot folder on the Inside Airbnb site.
PORTAL_FOLDER = {
    "listings.csv.gz": "data",
    "calendar.csv.gz": "data",
    "reviews.csv.gz": "data",
    "neighbourhoods.geojson": "visualisations",
}


def sha256(path):
    """Checksum of a file, read in 1 MB pieces so big files fit in memory."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_manifest():
    """Return (checksum, path) pairs, e.g. ('ab12…', 'data/raw/2026-06-15/listings.csv.gz')."""
    entries = []
    for line in MANIFEST.read_text().splitlines():
        if line.strip():
            checksum, path = line.split(maxsplit=1)
            entries.append((checksum, path.strip()))
    return entries


def sources(path):
    """The two places a file can come from: Inside Airbnb first, then our release."""
    snapshot, name = Path(path).parts[-2:]  # e.g. '2026-06-15', 'listings.csv.gz'
    return [
        ("Inside Airbnb", f"{PORTAL}/{snapshot}/{PORTAL_FOLDER[name]}/{name}"),
        ("GitHub release", f"{RELEASE}/{snapshot}_{name}"),
    ]


def download(url, target):
    """Save url to target. Returns an error message, or None if it worked."""
    request = urllib.request.Request(url, headers={"User-Agent": "ds5110-course-project"})
    try:
        with urllib.request.urlopen(request, timeout=120) as response, open(target, "wb") as out:
            while block := response.read(1024 * 1024):
                out.write(block)
    except OSError as error:  # covers HTTP errors, no internet, timeouts
        return str(error)
    return None


def fetch(checksum, path, from_release_only):
    """Make sure one file is in place with the right checksum. Returns an error or None."""
    target = ROOT / path
    if target.exists() and sha256(target) == checksum:
        print(f"ok        {path} (already downloaded)")
        return None

    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_name(target.name + ".part")
    problems = []
    for source, url in sources(path):
        if from_release_only and source != "GitHub release":
            continue
        error = download(url, partial)
        if error:
            problems.append(f"{source}: {error}")
            continue
        if sha256(partial) != checksum:
            problems.append(f"{source}: downloaded, but the checksum does not match MANIFEST.sha256")
            continue
        partial.replace(target)
        print(f"ok        {path} (from {source})")
        return None

    partial.unlink(missing_ok=True)
    return f"{path}\n    " + "\n    ".join(problems)


def main():
    from_release_only = "--from-release" in sys.argv[1:]
    entries = read_manifest()
    failed = [error for checksum, path in entries if (error := fetch(checksum, path, from_release_only))]

    if failed:
        print(f"\nERROR: {len(failed)} of {len(entries)} files could not be downloaded and checked:\n")
        print("\n".join(failed))
        sys.exit(1)
    print(f"\nAll {len(entries)} files are in data/raw/ and match MANIFEST.sha256.")


if __name__ == "__main__":
    main()
