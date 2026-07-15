import pandas as pd

employees = pd.read_csv("../datasets/employees.csv")

print("Employee Dataset")
print(employees)

print("\nHighest Salary")

print(employees["Salary"].max())

print("\nLowest Salary")

print(employees["Salary"].min())

print("\nAverage Salary")

print(employees["Salary"].mean())

print("\nDepartment Wise Salary")

print(
    employees.groupby("Department")["Salary"]
    .mean()
)

print("\nDepartment Employee Count")

print(
    employees.groupby("Department")
    .size()
)

print("\nTop 5 Highest Paid Employees")

print(
    employees.sort_values(
        "Salary",
        ascending=False
    ).head()
)

print("\nEmployees with Experience >5 Years")

print(
    employees[
        employees["Experience"] > 5
    ]
)

# Salary Category

employees["Salary_Level"] = pd.cut(
    employees["Salary"],
    bins=[0,50000,70000,100000],
    labels=["Low","Medium","High"]
)

print("\nSalary Categories")

print(employees)

print("\nSalary Level Count")

print(
    employees["Salary_Level"]
    .value_counts()
)