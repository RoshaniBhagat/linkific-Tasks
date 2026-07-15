import pandas as pd

sales = pd.read_csv("../datasets/sales.csv")
customers = pd.read_csv("../datasets/customers.csv")

# Merge datasets
data = pd.merge(sales, customers, on="Customer")

print("Merged Dataset")
print(data)

# Total Amount
data["Total_Amount"] = data["Quantity"] * data["Price"]

# Total Spending
customer_spending = (
    data.groupby("Customer")["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCustomer Spending")
print(customer_spending)

# Average Age by Membership
print("\nAverage Age by Membership")
print(data.groupby("Membership")["Age"].mean())

# Orders by City
print("\nOrders by City")
print(data.groupby("City").size())

# Product Category Sales
print("\nCategory Sales")
print(data.groupby("Category")["Total_Amount"].sum())

# Highest Spending Customer
highest = customer_spending.idxmax()

print("\nHighest Spending Customer:", highest)