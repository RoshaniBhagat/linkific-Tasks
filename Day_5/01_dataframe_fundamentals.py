import pandas as pd

# -----------------------------
# Creating DataFrame using Dictionary
# -----------------------------

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23, 28, 21, 30],
    "City": ["Bangalore", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("DataFrame")
print(df)

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names")
print(df.columns)

print("\nIndex")
print(df.index)

# -----------------------------
# Creating DataFrame from List
# -----------------------------

students = [
    ["John", 89],
    ["Emma", 92],
    ["Chris", 85]
]

df2 = pd.DataFrame(students, columns=["Student", "Marks"])

print("\nStudent Data")
print(df2)

# -----------------------------
# Creating DataFrame from List of Dictionaries
# -----------------------------

employees = [
    {"Name": "Amit", "Salary": 60000},
    {"Name": "Priya", "Salary": 75000},
    {"Name": "Rahul", "Salary": 55000}
]

df3 = pd.DataFrame(employees)

print("\nEmployee Data")
print(df3)

# -----------------------------
# Basic Information
# -----------------------------

print("\nData Types")
print(df.dtypes)

print("\nMemory Usage")
print(df.memory_usage())