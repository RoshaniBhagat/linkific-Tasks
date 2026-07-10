from datetime import datetime

dates = [
    "10-07-2026",
    "15-08-2026",
    "01-01-2027"
]

print("Original Dates")

print(dates)

converted = []

for date in dates:

    new_date = datetime.strptime(date, "%d-%m-%Y")

    converted.append(new_date.strftime("%Y-%m-%d"))

print("\nConverted Dates")

for date in converted:
    print(date)