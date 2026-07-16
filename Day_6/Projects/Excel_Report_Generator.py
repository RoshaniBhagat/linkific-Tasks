import os
import pandas as pd

print("=" * 80)
print("PROJECT 3 : EXCEL REPORT GENERATOR")
print("=" * 80)

# ============================================================
# Create Output Folder
# ============================================================

os.makedirs("../output", exist_ok=True)

# ============================================================
# Load Employee Dataset
# ============================================================

employees = pd.read_excel("../datasets/employees.xlsx")

print("\nOriginal Employee Dataset")
print(employees)

# ============================================================
# Dataset Information
# ============================================================

print("\nDataset Information")
employees.info()

print("\nSummary Statistics")
print(employees.describe())

# ============================================================
# Data Cleaning
# ============================================================

print("\nChecking Missing Values")
print(employees.isnull().sum())

print("\nRemoving Duplicate Records")
employees.drop_duplicates(inplace=True)

# ============================================================
# Feature Engineering
# ============================================================

print("\nCreating New Columns")

employees["Bonus"] = employees["Salary"] * 0.10
employees["Tax"] = employees["Salary"] * 0.05
employees["NetSalary"] = (
    employees["Salary"]
    + employees["Bonus"]
    - employees["Tax"]
)

print(employees)

# ============================================================
# High Salary Employees
# ============================================================

print("\nEmployees with Salary Greater Than 50,000")

high_salary = employees[
    employees["Salary"] > 50000
]

print(high_salary)

# ============================================================
# Department Summary
# ============================================================

print("\nDepartment-wise Summary")

department_summary = employees.groupby(
    "Department"
).agg(
    Employee_Count=("EmployeeID", "count"),
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Total_Salary=("Salary", "sum")
)

print(department_summary)

# ============================================================
# Experience Summary
# ============================================================

print("\nExperience Summary")

experience_summary = employees.groupby(
    "Department"
)["Experience"].mean()

print(experience_summary)

# ============================================================
# Top 5 Highest Paid Employees
# ============================================================

print("\nTop 5 Highest Paid Employees")

top_employees = employees.sort_values(
    by="Salary",
    ascending=False
).head(5)

print(top_employees)

# ============================================================
# Salary Statistics
# ============================================================

print("\nSalary Statistics")

print(f"Highest Salary : ₹{employees['Salary'].max():,}")
print(f"Lowest Salary  : ₹{employees['Salary'].min():,}")
print(f"Average Salary : ₹{employees['Salary'].mean():,.2f}")
print(f"Total Salary   : ₹{employees['Salary'].sum():,}")

# ============================================================
# Generate Excel Report
# ============================================================

print("\nGenerating Excel Report...")

output_file = "../output/Employee_Analysis_Report.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    employees.to_excel(
        writer,
        sheet_name="Employee Data",
        index=False
    )

    department_summary.to_excel(
        writer,
        sheet_name="Department Summary"
    )

    experience_summary.to_frame(
        name="Average Experience"
    ).to_excel(
        writer,
        sheet_name="Experience Summary"
    )

    top_employees.to_excel(
        writer,
        sheet_name="Top Employees",
        index=False
    )

    high_salary.to_excel(
        writer,
        sheet_name="High Salary",
        index=False
    )

print(f"\nExcel Report Generated Successfully!")
print(f"Saved to : {output_file}")

# ============================================================
# Final Summary
# ============================================================

print("\n" + "=" * 80)
print("PROJECT SUMMARY")
print("=" * 80)

print(f"Total Employees      : {len(employees)}")
print(f"Departments          : {employees['Department'].nunique()}")
print(f"Highest Salary       : ₹{employees['Salary'].max():,}")
print(f"Average Salary       : ₹{employees['Salary'].mean():,.2f}")
print(f"Total Payroll        : ₹{employees['Salary'].sum():,}")

print("\nProject Completed Successfully")