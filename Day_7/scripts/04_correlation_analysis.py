import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from helper_functions import save_plot, print_heading

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("CORRELATION ANALYSIS")

corr = df.select_dtypes(include="number").corr()

print(corr)

plt.figure(figsize=(7,5))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

save_plot(
    "images/heatmaps",
    "correlation_heatmap.png"
)