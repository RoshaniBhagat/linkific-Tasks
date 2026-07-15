import pandas as pd

sales = pd.read_csv("datasets/sales.csv")

print("First 5 Rows")

print(sales.head())

print("\nFirst 3 Rows")

print(sales.head(3))

print("\nLast 5 Rows")

print(sales.tail())

print("\nShape")

print(sales.shape)

print("\nInformation")

sales.info()

print("\nStatistics")

print(sales.describe())

print("\nColumn Names")

print(sales.columns)

print("\nIndex")

print(sales.index)

print("\nMissing Values")

print(sales.isnull().sum())

print("\nData Types")

print(sales.dtypes)

print("\nUnique Categories")

print(sales["Category"].unique())

print("\nNumber of Unique Cities")

print(sales["City"].nunique())