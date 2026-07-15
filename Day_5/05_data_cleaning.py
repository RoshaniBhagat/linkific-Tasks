import pandas as pd

# Load Dataset
df = pd.read_csv("datasets/messy_sales.csv")

print("Original Dataset")
print(df)

# ------------------------------------------------
# Missing Values
# ------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# ------------------------------------------------
# Drop Missing Values
# ------------------------------------------------

print("\nDrop Missing Rows")

drop_df = df.dropna()

print(drop_df)

# ------------------------------------------------
# Fill Missing Values
# ------------------------------------------------

print("\nFill Quantity with 0")

df["Quantity"] = df["Quantity"].fillna(0)

print(df)

print("\nFill Price with Mean")

mean_price = df["Price"].mean()

df["Price"] = df["Price"].fillna(mean_price)

print(df)

print("\nFill Missing City")

df["City"] = df["City"].fillna("Unknown")

print(df)

# ------------------------------------------------
# Remove Duplicates
# ------------------------------------------------

print("\nDuplicate Rows")

print(df.duplicated())

print("\nRemove Duplicate Rows")

df = df.drop_duplicates()

print(df)

# ------------------------------------------------
# Data Type Conversion
# ------------------------------------------------

print("\nData Types Before")

print(df.dtypes)

df["Quantity"] = df["Quantity"].astype(int)

df["Price"] = df["Price"].astype(float)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

print("\nData Types After")

print(df.dtypes)

# ------------------------------------------------
# Rename Columns
# ------------------------------------------------

df = df.rename(columns={
    "OrderID": "Order_ID",
    "OrderDate": "Order_Date"
})

print("\nRenamed Columns")

print(df.columns)

# ------------------------------------------------
# Set Index
# ------------------------------------------------

df = df.set_index("Order_ID")

print("\nAfter set_index()")

print(df.head())

# ------------------------------------------------
# Reset Index
# ------------------------------------------------

df = df.reset_index()

print("\nAfter reset_index()")

print(df.head())