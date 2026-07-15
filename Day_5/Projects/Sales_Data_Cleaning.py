import pandas as pd

df = pd.read_csv("../datasets/messy_sales.csv")

print("Original Dataset")
print(df)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["City"] = df["City"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()

# Correct data types
df["Quantity"] = df["Quantity"].astype(int)
df["Price"] = df["Price"].astype(float)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Create Total Amount
df["Total_Amount"] = df["Quantity"] * df["Price"]

print("\nCleaned Dataset")
print(df)

print("\nSummary Statistics")
print(df.describe())

# Save cleaned dataset
df.to_csv("../datasets/cleaned_sales.csv", index=False)

print("\nCleaned dataset saved successfully!")