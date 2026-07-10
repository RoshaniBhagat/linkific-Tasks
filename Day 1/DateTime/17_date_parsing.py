from datetime import datetime

# Date string
date_string = "2026-07-10"

print("Original String:")
print(date_string)

# Convert string to datetime
date_object = datetime.strptime(date_string, "%Y-%m-%d")

print("\nDatetime Object:")
print(date_object)

# Different format
formatted = date_object.strftime("%d/%m/%Y")

print("\nFormatted Date:")
print(formatted)

# Another example
another_date = "15-08-2026"

converted = datetime.strptime(another_date, "%d-%m-%Y")

print("\nSecond Date:")
print(converted)