# =============================================================================
# analysis.py — Video Game Sales Data Analysis
# Course  : CSE 310 Applied Programming — BYU-Idaho
# Author  : Tro Opong Ebenezer Jules Samuel
# Date    : May 2026
#
# Description:
#   Loads the vgsales.csv dataset and produces several analyses:
#     1. Top 10 best-selling video games globally (bar chart)
#     2. Total global sales by genre (bar chart)
#     3. Top 5 publishers by global sales (bar chart)
#     4. Summary statistics printed to the console
#   All charts are saved as PNG files inside the output/ folder.
# =============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# Setup — create the output directory if it does not already exist
# ------------------------------------------------------------------
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------------
# Load dataset
# The CSV contains: Rank, Name, Platform, Year, Genre, Publisher,
# NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
# ------------------------------------------------------------------
print("Loading dataset...")
df = pd.read_csv("vgsales.csv")
print(f"Dataset loaded: {len(df)} rows, {len(df.columns)} columns\n")

# Drop rows where Global_Sales or Genre is missing
df = df.dropna(subset=["Global_Sales", "Genre"])

# Convert Year column to numeric, coercing bad values to NaN
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# ------------------------------------------------------------------
# Summary statistics — print basic info about the dataset
# ------------------------------------------------------------------
print("=== Summary Statistics ===")
print(f"Total games in dataset : {len(df)}")
print(f"Unique genres          : {df['Genre'].nunique()}")
print(f"Unique platforms       : {df['Platform'].nunique()}")
print(f"Unique publishers      : {df['Publisher'].nunique()}")
print(f"Year range             : {int(df['Year'].min())} – {int(df['Year'].max())}")
print(f"Total global sales     : {df['Global_Sales'].sum():.2f} million units\n")

# ------------------------------------------------------------------
# Helper function — saves and optionally shows a matplotlib figure
# ------------------------------------------------------------------
def save_chart(filename):
    """Save the current figure to the output folder and display it."""
    path = os.path.join(OUTPUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(path)
    plt.show()
    print(f"Saved {path}")


# ==================================================================
# Chart 1: Top 10 Video Games by Global Sales
# ==================================================================
print("Generating Chart 1: Top 10 games by global sales...")

# Select the 10 rows with the highest Global_Sales value
top10 = df.nlargest(10, "Global_Sales")[["Name", "Global_Sales"]]

fig, ax = plt.subplots(figsize=(13, 6))
bars = ax.bar(top10["Name"], top10["Global_Sales"], color="steelblue", edgecolor="white")

# Annotate each bar with its sales value
for bar, value in zip(bars, top10["Global_Sales"]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        f"{value:.1f}M",
        ha="center", va="bottom", fontsize=8, color="black"
    )

ax.set_title("Top 10 Video Games by Global Sales", fontsize=14, fontweight="bold")
ax.set_xlabel("Game Title", fontsize=11)
ax.set_ylabel("Global Sales (millions of units)", fontsize=11)
ax.set_ylim(0, top10["Global_Sales"].max() * 1.15)
plt.xticks(rotation=30, ha="right", fontsize=9)
save_chart("top10_games.png")


# ==================================================================
# Chart 2: Total Global Sales by Genre
# ==================================================================
print("Generating Chart 2: Total global sales by genre...")

# Group by genre and sum Global_Sales, then sort descending
genre_sales = (
    df.groupby("Genre")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(13, 6))
bars = ax.bar(genre_sales.index, genre_sales.values, color="coral", edgecolor="white")

# Annotate each bar with the total sales value
for bar, value in zip(bars, genre_sales.values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 5,
        f"{value:.0f}M",
        ha="center", va="bottom", fontsize=8, color="black"
    )

ax.set_title("Total Global Sales by Genre", fontsize=14, fontweight="bold")
ax.set_xlabel("Genre", fontsize=11)
ax.set_ylabel("Total Global Sales (millions of units)", fontsize=11)
plt.xticks(rotation=30, ha="right", fontsize=9)
save_chart("sales_by_genre.png")


# ==================================================================
# Chart 3: Top 5 Publishers by Global Sales
# ==================================================================
print("Generating Chart 3: Top 5 publishers by global sales...")

# Aggregate sales per publisher, keep top 5
top_publishers = (
    df.groupby("Publisher")["Global_Sales"]
    .sum()
    .nlargest(5)
)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(top_publishers.index, top_publishers.values, color="mediumseagreen", edgecolor="white")

# Annotate each bar
for bar, value in zip(bars, top_publishers.values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 10,
        f"{value:.0f}M",
        ha="center", va="bottom", fontsize=9, color="black"
    )

ax.set_title("Top 5 Publishers by Global Sales", fontsize=14, fontweight="bold")
ax.set_xlabel("Publisher", fontsize=11)
ax.set_ylabel("Total Global Sales (millions of units)", fontsize=11)
plt.xticks(rotation=15, ha="right", fontsize=10)
save_chart("top5_publishers.png")

# ------------------------------------------------------------------
# Done
# ------------------------------------------------------------------
print("\nAll charts saved to the output/ folder.")
