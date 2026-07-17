import pandas as pd

from helper_functions import print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("CUSTOM DATA QUALITY REPORT")

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nUnique Values")

for col in df.columns:
    print(f"{col:<20} {df[col].nunique()}")

print("\nData Types")
print(df.dtypes)

print("\nColumns containing Null Values")

null_columns = df.columns[df.isnull().any()]

if len(null_columns) == 0:
    print("No Null Values Found")
else:
    print(list(null_columns))