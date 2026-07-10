import json

student = {
    "name": "Roshani",
    "age": 23,
    "course": "MCA",
    "skills": ["Python", "SQL", "Git"]
}

# Write JSON

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")

# Read JSON

with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details")
print(data)

print("\nName:", data["name"])
print("Skills:", data["skills"])