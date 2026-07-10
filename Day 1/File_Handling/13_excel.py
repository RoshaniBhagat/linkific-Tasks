import pandas as pd

students = {
    "Name": ["Roshani", "Rahul", "Anita"],
    "Age": [23, 25, 22],
    "City": ["Karwar", "Bangalore", "Mysore"]
}

df = pd.DataFrame(students)

# Save to Excel

df.to_excel("students.xlsx", index=False)

print("Excel file created.")

# Read Excel

data = pd.read_excel("students.xlsx")

print("\nExcel Data")
print(data)