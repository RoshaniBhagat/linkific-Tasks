import pandas as pd

print("=" * 80)
print("PROJECT 2 : TIME SERIES ANALYSIS")
print("=" * 80)

# ==============================================================
# Load Dataset
# ==============================================================

sales = pd.read_csv("../datasets/sales_timeseries.csv")

print("\nOriginal Dataset")
print(sales)

# ==============================================================
# Convert Date Column
# ==============================================================

sales["Date"] = pd.to_datetime(sales["Date"])

print("\nData Types")
print(sales.dtypes)

# ==============================================================
# Set Date as Index
# ==============================================================

sales.set_index("Date", inplace=True)

print("\nDataset with DateTime Index")
print(sales)

# ==============================================================
# Basic Statistics
# ==============================================================

print("\n" + "=" * 80)
print("BASIC STATISTICS")
print("=" * 80)

print(sales.describe())

# ==============================================================
# Date Components
# ==============================================================

print("\nExtracting Date Components")

sales["Year"] = sales.index.year
sales["Month"] = sales.index.month
sales["Day"] = sales.index.day
sales["DayName"] = sales.index.day_name()

print(sales.head())

# ==============================================================
# Weekly Sales
# ==============================================================

print("\n" + "=" * 80)
print("WEEKLY SALES")
print("=" * 80)

weekly_sales = sales["Sales"].resample("W").sum()

print(weekly_sales)

# ==============================================================
# Monthly Sales
# ==============================================================

print("\n" + "=" * 80)
print("MONTHLY SALES")
print("=" * 80)

monthly_sales = sales["Sales"].resample("ME").sum()

print(monthly_sales)

# ==============================================================
# Weekly Average
# ==============================================================

print("\nWeekly Average Sales")

weekly_average = sales["Sales"].resample("W").mean()

print(weekly_average)

# ==============================================================
# Rolling Average
# ==============================================================

print("\n" + "=" * 80)
print("3-Day Rolling Average")
print("=" * 80)

sales["RollingAverage"] = sales["Sales"].rolling(window=3).mean()

print(sales.head(10))

# ==============================================================
# Previous Day Sales
# ==============================================================

print("\nPrevious Day Sales")

sales["PreviousDaySales"] = sales["Sales"].shift(1)

print(sales.head(10))

# ==============================================================
# Daily Difference
# ==============================================================

print("\nDaily Sales Difference")

sales["SalesDifference"] = (
    sales["Sales"] -
    sales["PreviousDaySales"]
)

print(sales.head(10))

# ==============================================================
# Daily Growth Percentage
# ==============================================================

print("\nDaily Growth Percentage")

sales["GrowthPercent"] = (
    sales["Sales"].pct_change() * 100
)

print(sales.head(10))

# ==============================================================
# Highest Sales Day
# ==============================================================

print("\n" + "=" * 80)
print("HIGHEST SALES DAY")
print("=" * 80)

highest_day = sales["Sales"].idxmax()

print("Date :", highest_day.date())
print("Sales:", sales.loc[highest_day, "Sales"])

# ==============================================================
# Lowest Sales Day
# ==============================================================

print("\n" + "=" * 80)
print("LOWEST SALES DAY")
print("=" * 80)

lowest_day = sales["Sales"].idxmin()

print("Date :", lowest_day.date())
print("Sales:", sales.loc[lowest_day, "Sales"])

# ==============================================================
# Top 5 Highest Sales Days
# ==============================================================

print("\nTop 5 Sales Days")

top_sales = sales.sort_values(
    by="Sales",
    ascending=False
).head(5)

print(top_sales[["Sales"]])

# ==============================================================
# Filter Specific Date Range
# ==============================================================

print("\nSales Between 10 Jan and 20 Jan")

filtered = sales.loc["2025-01-10":"2025-01-20"]

print(filtered)

# ==============================================================
# Export Analysis
# ==============================================================

import os

os.makedirs("../output", exist_ok=True)

sales.to_csv(
    "../output/time_series_analysis.csv",
    index=True
)

print("\nAnalysis Report Saved Successfully!")

# ==============================================================
# Final Summary
# ==============================================================

print("\n" + "=" * 80)
print("PROJECT SUMMARY")
print("=" * 80)

print(f"Total Days               : {len(sales)}")
print(f"Highest Sale             : ₹{sales['Sales'].max():,}")
print(f"Lowest Sale              : ₹{sales['Sales'].min():,}")
print(f"Average Daily Sales      : ₹{sales['Sales'].mean():,.2f}")
print(f"Total Sales              : ₹{sales['Sales'].sum():,}")

print("\nProject Completed Successfully")