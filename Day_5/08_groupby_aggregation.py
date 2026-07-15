import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------
df = pd.read_csv("datasets/employees.csv")

print("=" * 50)
print("Original Dataset")
print("=" * 50)
print(df)

# ---------------------------------
# Group By Department
# ---------------------------------
department_group = df.groupby("Department")

# ---------------------------------
# Average Salary
# ---------------------------------
print("\nAverage Salary by Department")
print(department_group["Salary"].mean())

# ---------------------------------
# Maximum Salary
# ---------------------------------
print("\nMaximum Salary by Department")
print(department_group["Salary"].max())

# ---------------------------------
# Minimum Salary
# ---------------------------------
print("\nMinimum Salary by Department")
print(department_group["Salary"].min())

# ---------------------------------
# Total Salary
# ---------------------------------
print("\nTotal Salary by Department")
print(department_group["Salary"].sum())

# ---------------------------------
# Employee Count
# ---------------------------------
print("\nEmployee Count by Department")
print(department_group["Employee_ID"].count())

# ---------------------------------
# Multiple Aggregations
# ---------------------------------
print("\nMultiple Aggregations")
summary = department_group["Salary"].agg([
    "count",
    "sum",
    "mean",
    "min",
    "max"
])

print(summary)

# ---------------------------------
# Reset Index
# ---------------------------------
summary = summary.reset_index()

print("\nSummary Table")
print(summary)

# ---------------------------------
# Save Summary
# ---------------------------------
summary.to_csv("datasets/department_salary_summary.csv", index=False)

print("\nSummary saved as:")
print("datasets/department_salary_summary.csv")