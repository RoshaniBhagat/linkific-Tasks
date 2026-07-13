import csv
import json

employees = [
    {
        "Name": "Roshani",
        "Age": 22,
        "City": "Bangalore"
    },
    {
        "Name": "Amit",
        "Age": 24,
        "City": "Mumbai"
    },
    {
        "Name": "Priya",
        "Age": 23,
        "City": "Delhi"
    }
]

# -----------------------------
# Save CSV
# -----------------------------

with open("employees.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Age", "City"]
    )

    writer.writeheader()
    writer.writerows(employees)

print("CSV Saved Successfully!")

# -----------------------------
# Save JSON
# -----------------------------

with open("employees.json", "w", encoding="utf-8") as file:

    json.dump(
        employees,
        file,
        indent=4
    )

print("JSON Saved Successfully!")