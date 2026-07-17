import pandas as pd

from helper_functions import print_heading, save_plot

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("VARIANCE & STANDARD DEVIATION")

numeric = df.select_dtypes(include="number")

print("\nVariance\n")
print(numeric.var())

print("\nStandard Deviation\n")
print(numeric.std())

print("\nCoefficient of Variation (%)")

cv = (numeric.std() / numeric.mean()) * 100

print(cv)