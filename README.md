# Data Analysis with Python — Video Game Sales

**Name:** Tro Opong Ebenezer Jules Samuel
**Date:** May 2026
**Course:** CSE 310 Applied Programming — BYU-Idaho

## Demo Video
[Click here to watch the demo]()

## Overview
This program analyzes a dataset of over 16,000 video games and their global sales figures using Python. It generates two bar charts: one showing the top 10 best-selling games of all time, and another showing total global sales grouped by genre. The charts are saved as PNG files in the `output/` folder.

## Dataset

The dataset used is `vgsales.csv`, a publicly available video game sales dataset containing game titles, platforms, years, genres, publishers, and regional/global sales in millions of units.

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
output/top10_games.png      # Top 10 games by global sales
output/sales_by_genre.png   # Total global sales by genre
```
