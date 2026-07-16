import pandas as pd

print("=" * 70)
print("TIME SERIES RESAMPLING")
print("=" * 70)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

sales = pd.read_csv(
    "datasets/sales_timeseries.csv",
    parse_dates=["Date"]
)

sales.set_index("Date", inplace=True)

print("\nOriginal Dataset")
print(sales.head())

# -------------------------------------------------------
# Concept
# -------------------------------------------------------

print("""
Resampling changes the frequency of time-series data.

Example

Daily  ---> Weekly
Daily  ---> Monthly

Common Functions

sum()
mean()
max()
min()
""")

# -------------------------------------------------------
# Weekly Sales
# -------------------------------------------------------

print("\nWeekly Sales Sum")
weekly = sales.resample("W").sum()
print(weekly)

# -------------------------------------------------------
# Weekly Average
# -------------------------------------------------------

print("\nWeekly Average Sales")
weekly_avg = sales.resample("W").mean()
print(weekly_avg)

# -------------------------------------------------------
# Monthly Sales
# -------------------------------------------------------

print("\nMonthly Sales")

# In pandas 2.3+, use "ME" (Month End) instead of "M"
monthly = sales.resample("ME").sum()

print(monthly)

# -------------------------------------------------------
# Maximum Weekly Sales
# -------------------------------------------------------

print("\nWeekly Maximum Sales")
maximum = sales.resample("W").max()

print(maximum)

print("\nProgram Completed Successfully")