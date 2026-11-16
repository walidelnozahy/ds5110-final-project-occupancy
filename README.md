# Boston short-term rentals: occupancy

DS 5110 final project, Fall 2026, Occupancy track. We use Inside Airbnb's public Boston data to look at how booked short-term rental listings are across seasons and neighbourhoods, and how sure we can be about it.

## How to run

You need Python 3.14, `git` and `make`.

```bash
git clone https://github.com/walidelnozahy/ds5110-final-project-occupancy.git
cd ds5110-final-project-occupancy
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
make data
```

`make data` downloads 8 files into `data/raw/`: the listings, calendar, reviews and neighbourhood map for two snapshots (2026-06-15 and 2026-09-19). It then checks each file against its checksum in `MANIFEST.sha256`:

- A file that is already there and correct is skipped.
- If Inside Airbnb no longer has a file, it downloads our copy from the [`data-v1` release](https://github.com/walidelnozahy/ds5110-final-project-occupancy/releases/tag/data-v1).
- If a file doesn't match its checksum, it stops and says which file.

To test the backup copy on its own: `python src/download_data.py --from-release`.

**Windows:** `make` isn't installed by default. Either run the commands in WSL, or skip `make` and run `python src/download_data.py`, which does the same thing.

## Data

[Inside Airbnb](https://insideairbnb.com/get-the-data/), Boston. Build snapshot 2026-06-15, test snapshot 2026-09-19. Details are in the data card, [`data/README.md`](data/README.md).

Data from Inside Airbnb (https://insideairbnb.com), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Team

| Role (Nov 16–23) | Name | Contribution to this milestone |
|---|---|---|
| Delivery lead | Walid Elnozahy | Repo skeleton, `make data`, `MANIFEST.sha256` and the data release ([#1](https://github.com/walidelnozahy/ds5110-final-project-occupancy/issues/1)) |
| Data lead | | |
| Model lead | | |

## AI use

- **Claude (Anthropic), in Claude Code:** helped plan the milestone and write the download script, `Makefile` and this README. Walid reviewed and tested all of it.
