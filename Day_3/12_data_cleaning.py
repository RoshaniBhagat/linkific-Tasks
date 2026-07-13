# Sample scraped data

data = [
    "Python",
    " Java ",
    "",
    "Python",
    None,
    "Data Science",
    "Machine Learning ",
    "Java",
    " "
]

print("Original Data:")
print(data)

# Step 1: Remove None values
cleaned = [item for item in data if item is not None]

# Step 2: Remove extra spaces
cleaned = [item.strip() for item in cleaned]

# Step 3: Remove empty strings
cleaned = [item for item in cleaned if item != ""]

# Step 4: Remove duplicates
cleaned = list(dict.fromkeys(cleaned))

print("\nCleaned Data:")
print(cleaned)