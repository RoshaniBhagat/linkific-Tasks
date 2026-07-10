# Writing into file

with open("sample.txt", "w") as file:
    file.write("Hello Data Engineering!")

# Reading file

with open("sample.txt", "r") as file:
    content = file.read()

print(content)
