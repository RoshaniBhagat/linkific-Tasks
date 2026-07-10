from pathlib import Path
import pandas as pd

folder = Path("CSV_Files")

dataframes = []

for file in folder.glob("*.csv"):
    print(f"Reading {file.name}")

    df = pd.read_csv(file)

    dataframes.append(df)

combined = pd.concat(dataframes, ignore_index=True)

print("\nCombined Data")

print(combined)

combined.to_csv("combined_sales.csv", index=False)

print("\nCombined CSV Created Successfully.")