from pathlib import Path
import pandas as pd

folder = Path("CSV_Files")

all_data = []

for file in folder.glob("*.csv"):
    print("Reading:", file.name)

    df = pd.read_csv(file)

    all_data.append(df)

combined = pd.concat(all_data, ignore_index=True)

print("\nCombined Data")

print(combined)

combined.to_csv("combined_students.csv", index=False)

print("\nCombined CSV Saved.")