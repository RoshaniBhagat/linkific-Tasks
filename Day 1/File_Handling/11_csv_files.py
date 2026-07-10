import csv

# Writing CSV

data = [
    ["Name", "Age", "City"],
    ["Roshani", 23, "Karwar"],
    ["Rahul", 25, "Bangalore"],
    ["Anita", 22, "Mysore"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created.")

# Reading CSV

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("\nCSV Content:")
    for row in reader:
        print(row)