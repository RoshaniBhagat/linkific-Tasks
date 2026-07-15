import pandas as pd

# ---------------------------------
# Load Employee Dataset
# ---------------------------------
employees = pd.read_csv("datasets/employees.csv")

print("=" * 50)
print("Employees Dataset")
print("=" * 50)
print(employees)

# ---------------------------------
# Department Dataset
# ---------------------------------
departments = pd.DataFrame({
    "Department": ["HR", "IT", "Finance"],
    "Manager": ["Anita", "Rahul", "Kiran"]
})

print("\nDepartment Dataset")
print(departments)

# ---------------------------------
# Merge DataFrames
# ---------------------------------
merged_df = pd.merge(
    employees,
    departments,
    on="Department",
    how="left"
)

print("\nMerged Data")
print(merged_df)

# ---------------------------------
# Join Example
# ---------------------------------
emp = employees.set_index("Department")
dept = departments.set_index("Department")

joined_df = emp.join(dept)

print("\nJoined Data")
print(joined_df)

# ---------------------------------
# Pivot Table
# ---------------------------------
pivot = employees.pivot_table(
    values="Salary",
    index="Department",
    aggfunc=["mean", "sum", "max", "min", "count"]
)

print("\nPivot Table")
print(pivot)

# ---------------------------------
# Save Results
# ---------------------------------
merged_df.to_csv("datasets/merged_employees.csv", index=False)
pivot.to_csv("datasets/pivot_salary_summary.csv")

print("\nFiles Saved Successfully!")
print("1. datasets/merged_employees.csv")
print("2. datasets/pivot_salary_summary.csv")