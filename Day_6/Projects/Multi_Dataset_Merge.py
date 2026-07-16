import pandas as pd

print("=" * 80)
print("PROJECT 1 : MULTI DATASET MERGE")
print("=" * 80)

# ============================================================
# Load Datasets
# ============================================================

customers = pd.read_csv("../datasets/customers.csv")
orders = pd.read_csv("../datasets/orders.csv")
products = pd.read_csv("../datasets/products.csv")

print("\nCustomers Dataset")
print(customers)

print("\nOrders Dataset")
print(orders)

print("\nProducts Dataset")
print(products)

# ============================================================
# Merge Customers with Orders
# ============================================================

print("\n" + "=" * 80)
print("STEP 1 : Merge Customers with Orders")
print("=" * 80)

customer_orders = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)

print(customer_orders)

# ============================================================
# Merge with Products
# ============================================================

print("\n" + "=" * 80)
print("STEP 2 : Merge Product Information")
print("=" * 80)

sales = pd.merge(
    customer_orders,
    products,
    on="ProductID",
    how="inner"
)

print(sales)

# ============================================================
# Create Total Amount
# ============================================================

print("\nCreating Total Amount Column")

sales["TotalAmount"] = sales["Quantity"] * sales["Price"]

print(sales)

# ============================================================
# Display Important Columns
# ============================================================

print("\nSales Report")

report = sales[
    [
        "CustomerName",
        "City",
        "ProductName",
        "Category",
        "Quantity",
        "Price",
        "TotalAmount"
    ]
]

print(report)

# ============================================================
# Customer-wise Sales
# ============================================================

print("\n" + "=" * 80)
print("Customer-wise Sales Summary")
print("=" * 80)

customer_summary = sales.groupby(
    "CustomerName"
).agg(
    Orders=("OrderID", "count"),
    TotalQuantity=("Quantity", "sum"),
    TotalSales=("TotalAmount", "sum")
)

print(customer_summary)

# ============================================================
# Category-wise Sales
# ============================================================

print("\n" + "=" * 80)
print("Category-wise Sales")
print("=" * 80)

category_summary = sales.groupby(
    "Category"
).agg(
    Quantity=("Quantity", "sum"),
    Sales=("TotalAmount", "sum")
)

print(category_summary)

# ============================================================
# City-wise Sales
# ============================================================

print("\n" + "=" * 80)
print("City-wise Sales")
print("=" * 80)

city_summary = sales.groupby(
    "City"
).agg(
    Customers=("CustomerID", "nunique"),
    Sales=("TotalAmount", "sum")
)

print(city_summary)

# ============================================================
# Top Selling Products
# ============================================================

print("\n" + "=" * 80)
print("Top Selling Products")
print("=" * 80)

top_products = sales.groupby(
    "ProductName"
).agg(
    Quantity=("Quantity", "sum"),
    Revenue=("TotalAmount", "sum")
)

top_products = top_products.sort_values(
    by="Revenue",
    ascending=False
)

print(top_products)

# ============================================================
# Highest Spending Customer
# ============================================================

print("\n" + "=" * 80)
print("Highest Spending Customer")
print("=" * 80)

highest_customer = customer_summary.sort_values(
    by="TotalSales",
    ascending=False
)

print(highest_customer.head(1))

# ============================================================
# Save Final Report
# ============================================================

import os

os.makedirs("../output", exist_ok=True)

report.to_csv(
    "../output/final_sales_report.csv",
    index=False
)

print("\nReport saved successfully!")

# ============================================================
# Project Summary
# ============================================================

print("\n" + "=" * 80)
print("PROJECT SUMMARY")
print("=" * 80)

print(f"Total Customers           : {sales['CustomerID'].nunique()}")
print(f"Total Orders              : {sales['OrderID'].nunique()}")
print(f"Total Products Sold       : {sales['Quantity'].sum()}")
print(f"Total Revenue             : ₹{sales['TotalAmount'].sum():,}")
print(f"Average Order Value       : ₹{sales['TotalAmount'].mean():,.2f}")

print("\nProject Completed Successfully")