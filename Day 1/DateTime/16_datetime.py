from datetime import datetime

# Current date and time
current_datetime = datetime.now()

print("Current Date and Time:")
print(current_datetime)

# Current Date
print("\nCurrent Date:")
print(current_datetime.date())

# Current Time
print("\nCurrent Time:")
print(current_datetime.time())

# Formatting
formatted = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

print("\nFormatted Date and Time:")
print(formatted)

# Individual components
print("\nYear:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)