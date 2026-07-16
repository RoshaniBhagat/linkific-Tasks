import os
import time
import pandas as pd

print("=" * 80)
print("PROJECT 4 : LARGE CSV PROCESSOR")
print("=" * 80)

# ============================================================
# Create Output Folder
# ============================================================

os.makedirs("../output", exist_ok=True)

# ============================================================
# Start Timer
# ============================================================

start_time = time.time()

# ============================================================
# Read Large CSV in Chunks
# ============================================================

print("\nReading CSV File in Chunks...")

chunks = []

for chunk in pd.read_csv(
        "../datasets/large_sales.csv",
        chunksize=5):

    chunks.append(chunk)

sales = pd.concat(
    chunks,
    ignore_index=True
)

print("CSV Loaded Successfully!")

# ============================================================
# Display Dataset
# ============================================================

print("\nDataset Preview")
print(sales.head())

print("\nDataset Shape")
print(sales.shape)

# ============================================================
# Dataset Information
# ============================================================

print("\nDataset Information")
sales.info()

# ============================================================
# Data Cleaning
# ============================================================

print("\nChecking Missing Values")
print(sales.isnull().sum())

print("\nRemoving Duplicate Records")
sales.drop_duplicates(inplace=True)

# ============================================================
# Feature Engineering
# ============================================================

print("\nCreating Total Amount Column")

sales["TotalAmount"] = (
    sales["Quantity"] *
    sales["Price"]
)

print(sales.head())

# ============================================================
# Sales Summary
# ============================================================

print("\nSales Summary")
print(sales.describe())

# ============================================================
# Category-wise Sales
# ============================================================

print("\nCategory-wise Sales")

category_summary = sales.groupby(
    "Category"
).agg(
    Orders=("OrderID", "count"),
    Quantity=("Quantity", "sum"),
    Revenue=("TotalAmount", "sum")
)

print(category_summary)

# ============================================================
# City-wise Sales
# ============================================================

print("\nCity-wise Sales")

city_summary = sales.groupby(
    "City"
).agg(
    Orders=("OrderID", "count"),
    Revenue=("TotalAmount", "sum")
)

print(city_summary)

# ============================================================
# Customer-wise Sales
# ============================================================

print("\nCustomer-wise Sales")

customer_summary = sales.groupby(
    "Customer"
).agg(
    Orders=("OrderID", "count"),
    TotalQuantity=("Quantity", "sum"),
    Revenue=("TotalAmount", "sum")
)

print(customer_summary)

# ============================================================
# Top Selling Categories
# ============================================================

print("\nTop Selling Categories")

top_categories = category_summary.sort_values(
    by="Revenue",
    ascending=False
)

print(top_categories)

# ============================================================
# Memory Optimization
# ============================================================

print("\nMemory Usage Before Optimization")

before = sales.memory_usage(
    deep=True
).sum()

print(before, "bytes")

optimized = sales.copy()

optimized["Customer"] = optimized["Customer"].astype("category")
optimized["Category"] = optimized["Category"].astype("category")
optimized["City"] = optimized["City"].astype("category")

after = optimized.memory_usage(
    deep=True
).sum()

print("\nMemory Usage After Optimization")
print(after, "bytes")

print("\nMemory Saved")
print(before - after, "bytes")

# ============================================================
# Export Reports
# ============================================================

print("\nSaving Reports...")

sales.to_csv(
    "../output/processed_sales.csv",
    index=False
)

category_summary.to_csv(
    "../output/category_summary.csv"
)

city_summary.to_csv(
    "../output/city_summary.csv"
)

customer_summary.to_csv(
    "../output/customer_summary.csv"
)

print("Reports Saved Successfully!")

# ============================================================
# End Timer
# ============================================================

end_time = time.time()

# ============================================================
# Project Summary
# ============================================================

print("\n" + "=" * 80)
print("PROJECT SUMMARY")
print("=" * 80)

print(f"Total Orders             : {sales['OrderID'].count()}")
print(f"Unique Customers         : {sales['Customer'].nunique()}")
print(f"Unique Categories        : {sales['Category'].nunique()}")
print(f"Total Quantity Sold      : {sales['Quantity'].sum()}")
print(f"Total Revenue            : ₹{sales['TotalAmount'].sum():,}")
print(f"Average Revenue          : ₹{sales['TotalAmount'].mean():,.2f}")
print(f"Execution Time           : {end_time-start_time:.4f} seconds")

print("\nGenerated Files:")
print("- processed_sales.csv")
print("- category_summary.csv")
print("- city_summary.csv")
print("- customer_summary.csv")
print("Location : ../output/")

print("\nProject Completed Successfully")