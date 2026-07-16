import pandas as pd

print("=" * 60)
print("PANDAS MERGE BASICS")
print("=" * 60)

# ---------------------------------------------------------
# Loading datasets
# ---------------------------------------------------------

customers = pd.read_csv("datasets/customers.csv")
orders = pd.read_csv("datasets/orders.csv")

print("\nCustomers DataFrame")
print(customers)

print("\nOrders DataFrame")
print(orders)

# =========================================================
# What is Merge?
# =========================================================

print("\n" + "=" * 60)
print("Concept: Merge")
print("=" * 60)

print("""
Merge combines two DataFrames using a common column,
similar to SQL JOIN operations.

Syntax

pd.merge(left_dataframe,
         right_dataframe,
         on='CommonColumn',
         how='join_type')
""")

# =========================================================
# INNER JOIN
# =========================================================

print("\nINNER JOIN")
print("-" * 60)

inner_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="inner"
)

print(inner_merge)

print("""
Explanation:
Only matching CustomerIDs are returned.
CustomerID 107 is removed because it is absent in customers.
""")

# =========================================================
# LEFT JOIN
# =========================================================

print("\nLEFT JOIN")
print("-" * 60)

left_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="left"
)

print(left_merge)

print("""
Explanation:
All customers are kept.
Customers without orders show NaN values.
""")

# =========================================================
# RIGHT JOIN
# =========================================================

print("\nRIGHT JOIN")
print("-" * 60)

right_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="right"
)

print(right_merge)

print("""
Explanation:
All orders are kept.
CustomerID 107 appears with missing customer information.
""")

# =========================================================
# OUTER JOIN
# =========================================================

print("\nOUTER JOIN")
print("-" * 60)

outer_merge = pd.merge(
    customers,
    orders,
    on="CustomerID",
    how="outer"
)

print(outer_merge)

print("""
Explanation:
Returns every row from both DataFrames.
Missing values are filled with NaN.
""")

print("\nProgram Completed Successfully")