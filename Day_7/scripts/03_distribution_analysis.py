import pandas as pd
import matplotlib.pyplot as plt
from helper_functions import save_plot, print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("DISTRIBUTION ANALYSIS")

numerical_cols = ["Price", "Quantity", "Rating"]

for col in numerical_cols:
    plt.figure(figsize=(6,4))

    plt.hist(
        df[col],
        bins=10,
        edgecolor="black"
    )

    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")

    save_plot(
        "images/histograms",
        f"{col.lower()}_histogram.png"
    )

print("Histograms generated successfully.")