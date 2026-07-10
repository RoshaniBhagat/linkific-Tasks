from datetime import datetime, timedelta

today = datetime.today()

print("Today:")
print(today)

# Tomorrow
tomorrow = today + timedelta(days=1)

print("\nTomorrow:")
print(tomorrow)

# Yesterday
yesterday = today - timedelta(days=1)

print("\nYesterday:")
print(yesterday)

# Future Date
future = today + timedelta(days=30)

print("\n30 Days Later:")
print(future)

# Difference Between Dates
date1 = datetime(2026, 7, 10)
date2 = datetime(2026, 8, 15)

difference = date2 - date1

print("\nDifference:")
print(difference.days, "days")