import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

from helper_functions import print_heading  

# Load dataset
df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

print_heading("STATISTICAL TESTS")

# -----------------------------
# Independent T-Test
# -----------------------------
electronics = df[df["Category"] == "Electronics"]["Price"]
fashion = df[df["Category"] == "Fashion"]["Price"]

if len(electronics) > 1 and len(fashion) > 1:
    t_stat, p_value = ttest_ind(
        electronics,
        fashion,
        equal_var=False
    )

    print("\nIndependent T-Test")
    print(f"T Statistic : {t_stat:.4f}")
    print(f"P Value     : {p_value:.4f}")

    if p_value < 0.05:
        print("Result      : Significant Difference")
    else:
        print("Result      : No Significant Difference")

# -----------------------------
# Chi-Square Test
# -----------------------------
print("\nChi-Square Test")

table = pd.crosstab(
    df["Category"],
    df["Payment_Mode"]
)

chi2, p, dof, expected = chi2_contingency(table)

print(f"Chi2 Statistic : {chi2:.4f}")
print(f"P Value        : {p:.4f}")

if p < 0.05:
    print("Category and Payment Mode are associated.")
else:
    print("No association detected.")