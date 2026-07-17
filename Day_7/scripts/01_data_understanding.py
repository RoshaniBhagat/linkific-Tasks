import pandas as pd
from helper_functions import print_heading, separator

# Load dataset
df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("DATA UNDERSTANDING")

print("\nFirst 5 Rows")
print(df.head())

separator()

print("\nLast 5 Rows")
print(df.tail())

separator()

print("\nShape")
print(df.shape)

separator()

print("\nColumns")
print(df.columns.tolist())

separator()

print("\nData Types")
print(df.dtypes)

separator()

print("\nDataset Information")
df.info()

separator()

print("\nMemory Usage")
print(df.memory_usage(deep=True))

separator()

print("\nRandom Sample")
print(df.sample(5, random_state=42))