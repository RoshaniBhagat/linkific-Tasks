import pandas as pd

print("=" * 70)
print("ROLLING WINDOW | SHIFT | LAG")
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
# Rolling Average
# -------------------------------------------------------

print("\n3-Day Rolling Average")

sales["RollingAvg"] = sales["Sales"].rolling(window=3).mean()

print(sales.head(10))

print("""
Rolling Average smooths fluctuations in data.
""")

# -------------------------------------------------------
# Shift
# -------------------------------------------------------

print("\nShift Operation")

sales["PreviousDaySales"] = sales["Sales"].shift(1)

print(sales.head(10))

print("""
shift(1)
Moves values down by one row.

Useful for comparing today's sales with yesterday's sales.
""")

# -------------------------------------------------------
# Lag Feature
# -------------------------------------------------------

print("\nLag Feature")

sales["SalesDifference"] = (
    sales["Sales"] -
    sales["PreviousDaySales"]
)

print(sales.head(10))

# -------------------------------------------------------
# Percentage Growth
# -------------------------------------------------------

print("\nDaily Percentage Growth")

sales["GrowthPercent"] = (
    sales["Sales"].pct_change() * 100
)

print(sales.head(10))

print("\nFinal Dataset")

print(sales)

print("\nProgram Completed Successfully")