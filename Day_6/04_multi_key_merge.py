import pandas as pd

print("=" * 60)
print("MULTI KEY MERGE")
print("=" * 60)

# ---------------------------------------------------------
# Employee Details
# ---------------------------------------------------------

employees = pd.DataFrame({
    "EmployeeID": [1, 2, 3, 4],
    "Department": ["HR", "IT", "IT", "Finance"],
    "Salary": [35000, 55000, 60000, 50000]
})

# ---------------------------------------------------------
# Bonus Details
# ---------------------------------------------------------

bonus = pd.DataFrame({
    "EmployeeID": [1, 2, 3, 5],
    "Department": ["HR", "IT", "IT", "Finance"],
    "Bonus": [5000, 8000, 9000, 7000]
})

print("\nEmployees")
print(employees)

print("\nBonus")
print(bonus)

print("""
Multiple columns can be used as merge keys.

Syntax:

pd.merge(df1,
         df2,
         on=["Column1","Column2"])
""")

# =========================================================
# Merge on Multiple Columns
# =========================================================

merged = pd.merge(
    employees,
    bonus,
    on=["EmployeeID", "Department"],
    how="inner"
)

print("\nMerged DataFrame")
print(merged)

print("""
Rows are merged only when BOTH EmployeeID
and Department match.
""")

print("\nProgram Completed Successfully")