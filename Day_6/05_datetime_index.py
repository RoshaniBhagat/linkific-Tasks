import pandas as pd

print("=" * 70)
print("DATETIME INDEX IN PANDAS")
print("=" * 70)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

sales = pd.read_csv("datasets/sales_timeseries.csv")

print("\nOriginal Dataset")
print(sales.head())

# -------------------------------------------------------
# Convert Date column into datetime
# -------------------------------------------------------

sales["Date"] = pd.to_datetime(sales["Date"])

print("\nData Types After Conversion")
print(sales.dtypes)

# -------------------------------------------------------
# Set Date as Index
# -------------------------------------------------------

sales.set_index("Date", inplace=True)

print("\nDataset with DateTime Index")
print(sales.head())

# -------------------------------------------------------
# Date Components
# -------------------------------------------------------

print("\nExtracting Date Components")

sales["Year"] = sales.index.year
sales["Month"] = sales.index.month
sales["Day"] = sales.index.day
sales["DayName"] = sales.index.day_name()

print(sales.head())

# -------------------------------------------------------
# Date Filtering
# -------------------------------------------------------

print("\nSales Between Jan 10 and Jan 20")

filtered = sales.loc["2025-01-10":"2025-01-20"]

print(filtered)

print("\nProgram Completed Successfully")