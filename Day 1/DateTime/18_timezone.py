from datetime import datetime
from zoneinfo import ZoneInfo

# Current UTC Time
utc_time = datetime.now(ZoneInfo("UTC"))

print("UTC Time:")
print(utc_time)

# Convert to India Time
india_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

print("\nIndia Time:")
print(india_time)

# Convert to New York
new_york = utc_time.astimezone(ZoneInfo("America/New_York"))

print("\nNew York Time:")
print(new_york)