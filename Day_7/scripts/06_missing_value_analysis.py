import pandas as pd
import matplotlib.pyplot as plt

from helper_functions import print_heading, save_plot

# Load dataset
df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("MISSING VALUE ANALYSIS")

# Missing values count
missing = df.isnull().sum()

print("\nMissing Values:")
print(missing)

print("\nMissing Percentage:")
print((missing / len(df)) * 100)

# Visualization
plt.figure(figsize=(8,4))

missing.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Missing Values by Column")
plt.ylabel("Count")

save_plot(
    "images",
    "missing_values.png"
)

print("\nNo missing values found." if missing.sum()==0 else "\nMissing values detected.")