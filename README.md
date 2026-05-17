# Data Analysis with Python — Video Game Sales

**Name:** Tro Opong Ebenezer Jules Samuel
**Date:** May 2026
**Course:** CSE 310 Applied Programming — BYU-Idaho

## Demo Video
[Click here to watch the demo](https://youtu.be/uZPS6yQ3udE)

## Overview
This program analyzes a dataset of over 16,000 video games and their global sales figures using Python and the pandas and matplotlib libraries. It produces three bar charts: the top 10 best-selling games of all time, total global sales by genre, and the top 5 publishers by global sales. All charts are saved as PNG files in the `output/` folder and displayed interactively when the script is run.

## Dataset

**Source:** [Video Game Sales — Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales)

The dataset (`vgsales.csv`) contains 16,598 records of video games with sales greater than 100,000 copies. Each row includes:

| Column | Description |
|---|---|
| Name | Title of the game |
| Platform | Console or platform (e.g. PS2, Wii) |
| Year | Year of release |
| Genre | Game genre (e.g. Action, Sports) |
| Publisher | Publisher name |
| NA_Sales | North America sales (millions) |
| EU_Sales | Europe sales (millions) |
| JP_Sales | Japan sales (millions) |
| Other_Sales | Rest of world sales (millions) |
| Global_Sales | Total worldwide sales (millions) |

**Install dependencies:**
```bash
pip install pandas matplotlib
```

**Run the analysis:**
```bash
python analysis.py
```

**Output files generated:**
```
output/top10_games.png       # Top 10 games by global sales
output/sales_by_genre.png    # Total global sales by genre
output/top5_publishers.png   # Top 5 publishers by global sales
```

## Time Log

| Date | Hours | Description |
|---|---|---|
| May 16, 2026 | 1.0 | Set up project, initialized git repository |
| May 16, 2026 | 1.5 | Installed pandas and matplotlib, wrote analysis.py |
| May 16, 2026 | 0.5 | Generated charts, verified output PNG files |
| May 17, 2026 | 1.0 | Expanded analysis.py to 100+ lines with comments, updated README |
| **Total** | **4.0** | |
