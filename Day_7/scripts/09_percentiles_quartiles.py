import pandas as pd

from helper_functions import print_heading, save_plot

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("PERCENTILES & QUARTILES")

numeric = df.select_dtypes(include="number")

print("\n25th Percentile")
print(numeric.quantile(0.25))

print("\n50th Percentile (Median)")
print(numeric.quantile(0.50))

print("\n75th Percentile")
print(numeric.quantile(0.75))

print("\n90th Percentile")
print(numeric.quantile(0.90))

print("\n95th Percentile")
print(numeric.quantile(0.95))

print("\n99th Percentile")
print(numeric.quantile(0.99))