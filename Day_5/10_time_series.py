"""
10_time_series.py

Objective:
Learn Time Series Analysis using Pandas.
"""

import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------
df = pd.read_csv("datasets/sales.csv")

print("=" * 60)
print("Original Dataset")
print("=" * 60)
print(df)

# ---------------------------------
# Convert OrderDate to Datetime
# ---------------------------------
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# ---------------------------------
# Create Sales Column
# ---------------------------------
df["Sales"] = df["Quantity"] * df["Price"]

# ---------------------------------
# Set OrderDate as Index
# ---------------------------------
df.set_index("OrderDate", inplace=True)

# ---------------------------------
# Sort by Date
# ---------------------------------
df.sort_index(inplace=True)

print("\n" + "=" * 60)
print("Dataset with Date Index")
print("=" * 60)
print(df)

# ---------------------------------
# Monthly Sales (Month End)
# ---------------------------------
monthly_sales = df["Sales"].resample("ME").sum()

print("\n" + "=" * 60)
print("Monthly Sales")
print("=" * 60)
print(monthly_sales)

# ---------------------------------
# Weekly Sales
# ---------------------------------
weekly_sales = df["Sales"].resample("W").sum()

print("\n" + "=" * 60)
print("Weekly Sales")
print("=" * 60)
print(weekly_sales)

# ---------------------------------
# Daily Sales
# ---------------------------------
daily_sales = df["Sales"].resample("D").sum()

print("\n" + "=" * 60)
print("Daily Sales")
print("=" * 60)
print(daily_sales)

# ---------------------------------
# Rolling Average (3 Orders)
# ---------------------------------
df["Rolling_Average"] = df["Sales"].rolling(window=3).mean()

print("\n" + "=" * 60)
print("Rolling Average")
print("=" * 60)
print(df[["Sales", "Rolling_Average"]])

# ---------------------------------
# Filter Data by Date
# ---------------------------------
print("\n" + "=" * 60)
print("Sales After 2025-01-15")
print("=" * 60)
print(df.loc["2025-01-15":])

# ---------------------------------
# Highest Sales Day
# ---------------------------------
highest_day = df["Sales"].idxmax()
highest_sales = df["Sales"].max()

print("\nHighest Sales Day :", highest_day.date())
print("Highest Sales     :", highest_sales)

# ---------------------------------
# Lowest Sales Day
# ---------------------------------
lowest_day = df["Sales"].idxmin()
lowest_sales = df["Sales"].min()

print("\nLowest Sales Day  :", lowest_day.date())
print("Lowest Sales      :", lowest_sales)

# ---------------------------------
# Summary Statistics
# ---------------------------------
print("\n" + "=" * 60)
print("Sales Statistics")
print("=" * 60)
print(df["Sales"].describe())

# ---------------------------------
# Save Processed Dataset
# ---------------------------------
output_file = "datasets/time_series_output.csv"
df.to_csv(output_file)

print("\nProcessed dataset saved successfully!")
print(f"Location: {output_file}")