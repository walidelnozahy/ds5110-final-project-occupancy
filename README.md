# Boston short-term rentals: occupancy

DS 5110 final project, Fall 2026, Occupancy track. We use Inside Airbnb's public Boston data to look at how booked short-term rental listings are across seasons and neighbourhoods, and how sure we can be about it.

## Question

Among Boston Airbnb listings included in the June 15, 2026 snapshot, how does calendar unavailability vary across seasons and neighbourhoods, and how uncertain are these estimates? The target population consists of Boston listings appearing in this snapshot with valid calendar records. We measure each listing's unavailable-night proportion using the available field in calendar.csv.gz and identify neighbourhoods using neighbourhood_cleansed in listings.csv.gz. We will compare seasonal and neighbourhood-level differences and estimate uncertainty using bootstrap confidence intervals. Inside Airbnb explains that unavailable dates may represent either confirmed bookings or dates blocked by hosts. Therefore, our analysis measures calendar unavailability rather than actual guest occupancy and cannot establish how frequently properties are truly rented.

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

- A file that is already there and correct is kept. Raw files are never overwritten: if one is there but wrong, it stops and tells you to delete it.
- If Inside Airbnb no longer has a file, it downloads our copy from the [`data-v1` release](https://github.com/walidelnozahy/ds5110-final-project-occupancy/releases/tag/data-v1).
- If a downloaded file doesn't match its checksum, it stops and says which file.

Run it inside the activated `.venv`, so `python` is the project's Python.

To test the backup copy on its own: `python src/download_data.py --from-release`.

**Windows:** `make` isn't installed by default. Either run the commands in WSL, or skip `make` and run `python src/download_data.py`, which does the same thing.

## Data

[Inside Airbnb](https://insideairbnb.com/get-the-data/), Boston. Build snapshot 2026-06-15, test snapshot 2026-09-19. Details are in the data card, [`data/README.md`](data/README.md).

Data from Inside Airbnb (https://insideairbnb.com), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Team

| Role (Nov 16–23) | Name | Contribution to this milestone |
|---|---|---|
| Delivery lead | Walid Elnozahy | Repo skeleton, `make data`, `MANIFEST.sha256` and the data release ([PR #5](https://github.com/walidelnozahy/ds5110-final-project-occupancy/pull/5)); reviewed the data card and fixed the question format and data card details ([PR #9](https://github.com/walidelnozahy/ds5110-final-project-occupancy/pull/9)) |
| Data lead | Max Goldmuntz | Drafted the data card (`data/README.md`), including source provenance, occupancy-specific limitations, and checksum verification documentation. ([PR #8](https://github.com/walidelnozahy/ds5110-final-project-occupancy/pull/8), [PR #7](https://github.com/walidelnozahy/ds5110-final-project-occupancy/pull/7)) |
| Model lead | Ziang Chen|Structured and outlined the research question. Verified contribution by the delivery head. ([PR #6](https://github.com/walidelnozahy/ds5110-final-project-occupancy/pull/6)) |

## AI use

- **Claude (Anthropic), in Claude Code:** helped plan the milestone, write the download script, `Makefile` and this README, and review the question and data card (checking word count and row counts). Walid reviewed and tested all of it.
