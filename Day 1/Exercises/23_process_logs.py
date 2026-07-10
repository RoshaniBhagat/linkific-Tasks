info = 0
warning = 0
error = 0

with open("application.log", "r") as file:

    for line in file:

        if line.startswith("INFO"):
            info += 1

        elif line.startswith("WARNING"):
            warning += 1

        elif line.startswith("ERROR"):
            error += 1

print("Log Summary")

print("INFO:", info)

print("WARNING:", warning)

print("ERROR:", error)