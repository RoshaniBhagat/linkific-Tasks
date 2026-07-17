import pandas as pd

from helper_functions import print_heading
df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("PATTERN IDENTIFICATION")

print("\nAverage Price by Category")

print(
    df.groupby("Category")["Price"]
      .mean()
      .sort_values(ascending=False)
)

print("\nAverage Rating by Category")

print(
    df.groupby("Category")["Rating"]
      .mean()
      .sort_values(ascending=False)
)

print("\nCity-wise Sales")

city_sales = (
    df.groupby("City")["Price"]
      .sum()
      .sort_values(ascending=False)
)

print(city_sales)

print("\nMost Common Payment Method")

print(df["Payment_Mode"].value_counts())

print("\nTop Selling Category")

print(df["Category"].value_counts())

# Save markdown report

with open(
    "Day_7/reports/pattern_identification.md",
    "w",
    encoding="utf-8"
) as file:

    file.write("# Pattern Identification Report\n\n")

    file.write("## Average Price by Category\n")
    file.write(
        df.groupby("Category")["Price"]
        .mean()
        .to_markdown()
    )

    file.write("\n\n## City-wise Sales\n")

    file.write(
        city_sales.to_markdown()
    )

print("\nMarkdown report generated.")