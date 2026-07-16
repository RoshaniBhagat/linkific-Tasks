import pandas as pd

print("=" * 70)
print("EXCEL AUTOMATION")
print("=" * 70)

# --------------------------------------------------------
# Load Dataset
# --------------------------------------------------------

employees = pd.read_excel("datasets/employees.xlsx")

print("\nOriginal Dataset")
print(employees)

# --------------------------------------------------------
# Salary Hike (10%)
# --------------------------------------------------------

print("\nAdding Salary Hike")

employees["NewSalary"] = employees["Salary"] * 1.10

# --------------------------------------------------------
# Bonus (5%)
# --------------------------------------------------------

employees["Bonus"] = employees["Salary"] * 0.05

# --------------------------------------------------------
# Total Salary
# --------------------------------------------------------

employees["TotalSalary"] = (
    employees["NewSalary"] +
    employees["Bonus"]
)

print(employees)

# --------------------------------------------------------
# Department Summary
# --------------------------------------------------------

print("\nDepartment-wise Salary Summary")

summary = employees.groupby("Department").agg(
    Employee_Count=("EmployeeID", "count"),
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Total_Salary=("Salary", "sum")
)

print(summary)

# --------------------------------------------------------
# Save Multiple Sheets
# --------------------------------------------------------

print("\nCreating Excel Report...")

with pd.ExcelWriter(
    "datasets/Employee_Report.xlsx",
    engine="openpyxl"
) as writer:

    employees.to_excel(
        writer,
        sheet_name="Employees",
        index=False
    )

    summary.to_excel(
        writer,
        sheet_name="Department Summary"
    )

print("\nEmployee_Report.xlsx Created Successfully")

print("\nProgram Completed Successfully")