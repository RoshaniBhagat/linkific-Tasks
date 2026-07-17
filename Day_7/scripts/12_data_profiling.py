import pandas as pd
from ydata_profiling import ProfileReport

from helper_functions import print_heading

print_heading("DATA PROFILING")

df = pd.read_csv("Day_7/datasets/ecommerce_data.csv")

profile = ProfileReport(
    df,
    title="Ecommerce Data Profiling Report",
    explorative=True
)

profile.to_file("Day_7/reports/ecommerce_profile.html")

print("\nProfile report saved successfully.")
print("Location : reports/ecommerce_profile.html")