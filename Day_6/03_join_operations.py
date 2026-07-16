import pandas as pd

print("=" * 60)
print("JOIN OPERATIONS")
print("=" * 60)

customers = pd.read_csv("datasets/customers.csv")
orders = pd.read_csv("datasets/orders.csv")

# ---------------------------------------------------------
# Setting Index
# ---------------------------------------------------------

customers = customers.set_index("CustomerID")
orders = orders.set_index("CustomerID")

print("\nCustomers")
print(customers)

print("\nOrders")
print(orders)

print("""
DataFrame.join() joins using indexes.
""")

# =========================================================
# Left Join
# =========================================================

print("\nLEFT JOIN")
print("-" * 60)

left = customers.join(
    orders,
    how="left"
)

print(left)

# =========================================================
# Right Join
# =========================================================

print("\nRIGHT JOIN")
print("-" * 60)

right = customers.join(
    orders,
    how="right"
)

print(right)

# =========================================================
# Inner Join
# =========================================================

print("\nINNER JOIN")
print("-" * 60)

inner = customers.join(
    orders,
    how="inner"
)

print(inner)

print("\nProgram Completed Successfully")