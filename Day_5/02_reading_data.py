import pandas as pd

# Read CSV

sales = pd.read_csv("datasets/sales.csv")

print("Sales Dataset")
print(sales)

# Read Excel

# sales.to_excel("datasets/sales.xlsx", index=False)

# excel = pd.read_excel("datasets/sales.xlsx")

# Read JSON

sales.to_json("datasets/sales.json", orient="records")

json_data = pd.read_json("datasets/sales.json")

print("\nJSON Data")

print(json_data)

# SQL Example

"""
import sqlite3

conn = sqlite3.connect("company.db")

df = pd.read_sql("SELECT * FROM employees", conn)

print(df)
"""