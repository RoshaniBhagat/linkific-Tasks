import json

with open("employee.json", "r") as file:
    data = json.load(file)

employee = data["employee"]

print("Employee ID:", employee["id"])
print("Employee Name:", employee["name"])
print("Department:", employee["department"])

print("\nSkills")

for skill in employee["skills"]:
    print(skill)