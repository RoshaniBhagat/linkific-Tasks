import pandas as pd
from helper_functions import print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("SUMMARY STATISTICS")

print("\nNumerical Summary")
print(df.describe())

print("\nCategorical Summary")
print(df.describe(include="object"))

print("\nMean Price:", df["Price"].mean())
print("Median Price:", df["Price"].median())
print("Maximum Price:", df["Price"].max())
print("Minimum Price:", df["Price"].min())

print("\nAverage Quantity:", df["Quantity"].mean())

print("\nUnique Cities")
print(df["City"].unique())

print("\nUnique Categories")
print(df["Category"].unique())