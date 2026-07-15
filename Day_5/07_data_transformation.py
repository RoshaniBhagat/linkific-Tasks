
import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------
df = pd.read_csv("datasets/employees.csv")

print("=" * 50)
print("Original Dataset")
print("=" * 50)
print(df)

# ---------------------------------
# Create Bonus Column (10% of Salary)
# ---------------------------------
df["Bonus"] = df["Salary"] * 0.10

# ---------------------------------
# Create Total Salary Column
# ---------------------------------
df["Total_Salary"] = df["Salary"] + df["Bonus"]

# ---------------------------------
# Increase Salary by 5%
# ---------------------------------
df["Updated_Salary"] = df["Salary"] * 1.05

# ---------------------------------
# Convert Employee Names to Uppercase
# ---------------------------------
df["Name"] = df["Name"].str.upper()

# ---------------------------------
# Rename Column
# ---------------------------------
df.rename(columns={"Salary": "Monthly_Salary"}, inplace=True)

# ---------------------------------
# Replace Department Names
# ---------------------------------
df["Department"] = df["Department"].replace({
    "IT": "Technology",
    "HR": "Human Resources"
})

# ---------------------------------
# Create Salary Category
# ---------------------------------
df["Salary_Category"] = df["Monthly_Salary"].apply(
    lambda x: "High" if x >= 50000 else "Medium"
)

# ---------------------------------
# Experience Level
# ---------------------------------
def experience_level(years):
    if years >= 5:
        return "Senior"
    elif years >= 3:
        return "Mid-Level"
    else:
        return "Junior"

df["Experience_Level"] = df["Experience"].apply(experience_level)

# ---------------------------------
# Display Transformed Dataset
# ---------------------------------
print("\nTransformed Dataset")
print(df)

# ---------------------------------
# Save the Transformed Dataset
# ---------------------------------
df.to_csv("datasets/transformed_employees.csv", index=False)

print("\nTransformed dataset saved as:")
print("datasets/transformed_employees.csv")