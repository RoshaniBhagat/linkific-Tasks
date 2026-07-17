import pandas as pd

from helper_functions import print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("NUMERICAL ANALYSIS")

numeric = df.select_dtypes(include="number")

print("\nNumerical Columns")

print(list(numeric.columns))

print("\nCorrelation Matrix")

print(numeric.corr())

print("\nSummary Statistics")

print(numeric.describe().T)

print("\nMean")

print(numeric.mean())

print("\nMedian")

print(numeric.median())

print("\nVariance")

print(numeric.var())

print("\nStandard Deviation")

print(numeric.std())

print("\nMaximum Values")

print(numeric.max())

print("\nMinimum Values")

print(numeric.min())

print("\nRange")

print(numeric.max() - numeric.min())