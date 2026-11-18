# Data card

## Source
The data is sourced from https://insideairbnb.com/get-the-data/ (Boston section). The publisher is Inside Airbnb, which is an independent project and not affiliated with Airbnb. The data was collected by scraping public Airbnb listing pages.

## Snapshots
* **Build snapshot:** 2026-06-15
* **Test snapshot:** 2026-09-19

We use two snapshots so we can develop our occupancy analysis on an earlier quarter and then check if our findings still hold on the more recent September 19 dataset.

## License
The files are licensed under CC BY 4.0. This requires attribution, meaning we must cite Inside Airbnb on our final project site and in the main README.

The license covers Inside Airbnb's files, but the content in them was scraped from Airbnb's public pages. So we only use these published snapshots, we don't scrape Airbnb ourselves, and we keep host names and listing URLs out of our site and slides.

## Files
Each snapshot has the same four files, in `data/raw/<snapshot date>/`. Row counts are given as June 15 / September 19.
* **`listings.csv.gz`**: Grain is one row per listing. Contains 4,378 / 4,368 rows. Main use is for features, hosts, and prices.
* **`calendar.csv.gz`**: Grain is one row per listing per date. Contains 1,611,110 / 1,594,327 rows. Main use is for availability, occupancy, and scale.
* **`reviews.csv.gz`**: Grain is one row per review. Contains 252,910 / 267,731 rows. Main use is for text and activity over time.
* **`neighbourhoods.geojson`**: Grain is one polygon per neighbourhood. Contains 26 / 26 features (the same file in both snapshots). Main use is for grouping and optional maps.

## Known limits
Our track focuses on Occupancy, which comes with a specific pitfall: an "unavailable" date in the calendar does not necessarily mean the listing was booked. Hosts often block dates themselves for personal use or maintenance. Therefore, relying strictly on calendar unavailability risks overstating actual booking rates.

## Checksums
The `MANIFEST.sha256` file is located in the root directory of the repository. To verify the integrity of the downloaded snapshot files against these checksums, run `make data` (or `python src/download_data.py`). The script automatically checks each downloaded file against its expected hash and stops with an error if a mismatch is found.

To check the files by hand, run this from the repository root: `shasum -a 256 -c MANIFEST.sha256` on a Mac, or `sha256sum -c MANIFEST.sha256` on Linux. Every line should end in `OK`.
