import pandas as pd

print("=" * 70)
print("READING AND WRITING EXCEL FILES")
print("=" * 70)

# --------------------------------------------------------
# Read Excel File
# --------------------------------------------------------

employees = pd.read_excel("datasets/employees.xlsx")

print("\nEmployee Dataset")
print(employees)

# --------------------------------------------------------
# Dataset Information
# --------------------------------------------------------

print("\nData Types")
print(employees.dtypes)

print("\nSummary Statistics")
print(employees.describe())

# --------------------------------------------------------
# Filter Employees
# --------------------------------------------------------

print("\nEmployees with Salary > 50000")

high_salary = employees[employees["Salary"] > 50000]

print(high_salary)

# --------------------------------------------------------
# Add Bonus Column
# --------------------------------------------------------

print("\nAdding Bonus Column")

employees["Bonus"] = employees["Salary"] * 0.10

print(employees)

# --------------------------------------------------------
# Save to Excel
# --------------------------------------------------------

employees.to_excel(
    "datasets/employees_updated.xlsx",
    index=False
)

print("\nUpdated Excel File Saved Successfully")

print("\nProgram Completed Successfully")