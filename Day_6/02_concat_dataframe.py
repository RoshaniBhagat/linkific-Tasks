import pandas as pd

print("=" * 60)
print("PANDAS CONCAT")
print("=" * 60)

# ---------------------------------------------------------
# Creating sample DataFrames
# ---------------------------------------------------------

sales_jan = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Sales": [15, 30, 20]
})

sales_feb = pd.DataFrame({
    "Product": ["Laptop", "Monitor", "Headphones"],
    "Sales": [18, 12, 16]
})

print("\nJanuary Sales")
print(sales_jan)

print("\nFebruary Sales")
print(sales_feb)

# =========================================================
# Vertical Concatenation
# =========================================================

print("\nVertical Concatenation")
print("-" * 60)

vertical = pd.concat(
    [sales_jan, sales_feb],
    ignore_index=True
)

print(vertical)

print("""
Rows are appended one after another.
ignore_index=True creates a new index.
""")

# =========================================================
# Horizontal Concatenation
# =========================================================

print("\nHorizontal Concatenation")
print("-" * 60)

horizontal = pd.concat(
    [sales_jan, sales_feb],
    axis=1
)

print(horizontal)

print("""
axis=1 joins DataFrames column-wise.
""")

print("\nProgram Completed Successfully")