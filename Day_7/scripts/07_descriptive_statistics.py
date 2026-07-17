import pandas as pd

from helper_functions import print_heading, save_plot
df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("DESCRIPTIVE STATISTICS")

numeric = df.select_dtypes(include="number")

print(numeric.describe().T)

print("\nAdditional Statistics\n")

print("Mean")
print(numeric.mean())

print("\nMedian")
print(numeric.median())

print("\nMode")
print(numeric.mode().iloc[0])

print("\nMinimum")
print(numeric.min())

print("\nMaximum")
print(numeric.max())