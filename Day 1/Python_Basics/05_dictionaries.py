# Dictionary

student = {
    "name": "Roshani",
    "age": 23,
    "course": "MCA"
}

print(student)

print(student["name"])

student["city"] = "Karwar"

student["age"] = 24

del student["course"]

print(student)

for key, value in student.items():
    print(key, ":", value)