import pandas as pd

sales = pd.read_csv("../datasets/sales.csv")

sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])

sales["Total"] = sales["Quantity"] * sales["Price"]

print("Daily Sales")

daily_sales = (
    sales.groupby("OrderDate")["Total"]
    .sum()
)

print(daily_sales)

print("\nMonthly Sales")

monthly_sales = (
    sales.groupby(
        sales["OrderDate"].dt.month
    )["Total"].sum()
)

print(monthly_sales)

print("\nOrders per Month")

print(
    sales.groupby(
        sales["OrderDate"].dt.month
    ).size()
)

print("\nSales by Weekday")

print(
    sales.groupby(
        sales["OrderDate"].dt.day_name()
    )["Total"].sum()
)

print("\nHighest Sales Day")

print(daily_sales.idxmax())

print(daily_sales.max())