filename = "students.csv"

try:

    with open(filename, "r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print("File not found.")

except PermissionError:

    print("Permission denied.")

except Exception as error:

    print("Unexpected Error:", error)

finally:

    print("Program Finished.")