import pandas as pd

df = pd.read_csv("datasets/sales.csv")

# ----------------------------------------
# Convert to Uppercase
# ----------------------------------------

print(df["Customer"].str.upper())

# ----------------------------------------
# Convert to Lowercase
# ----------------------------------------

print(df["Customer"].str.lower())

# ----------------------------------------
# Length of Strings
# ----------------------------------------

print(df["Customer"].str.len())

# ----------------------------------------
# Replace Values
# ----------------------------------------

df["City"] = df["City"].str.replace(
    "Bangalore",
    "Bengaluru"
)

print(df["City"])

# ----------------------------------------
# Startswith
# ----------------------------------------

print(df[df["Customer"].str.startswith("A")])

# ----------------------------------------
# Endswith
# ----------------------------------------

print(df[df["Customer"].str.endswith("e")])

# ----------------------------------------
# Contains
# ----------------------------------------

print(df[df["Product"].str.contains("top")])

# ----------------------------------------
# Strip Spaces
# ----------------------------------------

sample = pd.Series([
    "  Apple ",
    " Banana ",
    " Orange "
])

print(sample.str.strip())

# ----------------------------------------
# Split Strings
# ----------------------------------------

emails = pd.Series([
    "alice@gmail.com",
    "bob@yahoo.com",
    "john@hotmail.com"
])

print(emails.str.split("@"))

# ----------------------------------------
# Extract Domain
# ----------------------------------------

print(emails.str.split("@").str[1])

# ----------------------------------------
# Concatenate Columns
# ----------------------------------------

df["Customer_Product"] = (
    df["Customer"] +
    " - " +
    df["Product"]
)

print(df[["Customer_Product"]])

# ----------------------------------------
# Capitalize
# ----------------------------------------

print(df["Customer"].str.capitalize())

# ----------------------------------------
# Title Case
# ----------------------------------------

print(df["Customer"].str.title())