import pandas as pd
import matplotlib.pyplot as plt

from helper_functions import save_plot, print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("OUTLIER DETECTION")

columns = ["Price", "Quantity", "Rating"]

for col in columns:

    plt.figure(figsize=(6,4))

    plt.boxplot(df[col])

    plt.title(f"{col} Boxplot")

    save_plot(
        "images/boxplots",
        f"{col.lower()}_boxplot.png"
    )

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"\n{col}")
    print("-"*40)
    print("Q1 :", Q1)
    print("Q3 :", Q3)
    print("IQR:", IQR)
    print("Lower Limit:", lower)
    print("Upper Limit:", upper)
    print("Number of Outliers:", len(outliers))

    if len(outliers) > 0:
        print(outliers[[col]])