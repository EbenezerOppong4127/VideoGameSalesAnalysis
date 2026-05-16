import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)

df = pd.read_csv("vgsales.csv")

# Chart 1: Top 10 games by global sales
top10 = df.nlargest(10, "Global_Sales")[["Name", "Global_Sales"]]
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top10["Name"], top10["Global_Sales"], color="steelblue")
ax.set_title("Top 10 Video Games by Global Sales")
ax.set_xlabel("Game")
ax.set_ylabel("Global Sales (millions)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("output/top10_games.png")
plt.show()
print("Saved output/top10_games.png")

# Chart 2: Total global sales by genre
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(genre_sales.index, genre_sales.values, color="coral")
ax.set_title("Total Global Sales by Genre")
ax.set_xlabel("Genre")
ax.set_ylabel("Global Sales (millions)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("output/sales_by_genre.png")
plt.show()
print("Saved output/sales_by_genre.png")
