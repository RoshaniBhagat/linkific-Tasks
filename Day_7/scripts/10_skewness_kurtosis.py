import pandas as pd

from helper_functions import print_heading, save_plot

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("SKEWNESS & KURTOSIS")

numeric = df.select_dtypes(include="number")

print("\nSkewness")
print(numeric.skew())

print("\nKurtosis")
print(numeric.kurt())

print("\nInterpretation")

for column in numeric.columns:

    skew = numeric[column].skew()

    if skew > 1:
        interpretation = "Highly Positively Skewed"

    elif skew > 0.5:
        interpretation = "Moderately Positively Skewed"

    elif skew < -1:
        interpretation = "Highly Negatively Skewed"

    elif skew < -0.5:
        interpretation = "Moderately Negatively Skewed"

    else:
        interpretation = "Approximately Symmetric"

    print(f"{column:<12}: {interpretation}")