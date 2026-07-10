# Writing to a text file

with open("sample.txt", "w") as file:
    file.write("Welcome to Data Engineering!\n")
    file.write("Learning Python File Handling.\n")

print("Data written successfully.")

# Reading the file

with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Appending new data

with open("sample.txt", "a") as file:
    file.write("This line is added later.\n")

print("Data appended successfully.")

# Reading again

with open("sample.txt", "r") as file:
    print("\nUpdated File:")
    print(file.read())