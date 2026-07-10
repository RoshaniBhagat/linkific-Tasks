import pandas as pd

# Create a date range
dates = pd.date_range(
    start="2026-07-01",
    end="2026-07-10",
    freq="D"
)

print("Date Range:")
print(dates)

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Sales": [100, 120, 150, 130, 170, 180, 200, 190, 210, 250]
})

print("\nSales Data")
print(df)

# Save CSV
df.to_csv("sales_timeseries.csv", index=False)

print("\nCSV File Saved Successfully.")