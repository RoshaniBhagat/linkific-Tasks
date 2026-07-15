import pandas as pd

sales = pd.read_csv("datasets/sales.csv")

# Selecting One Column

print(sales["Customer"])

# Selecting Multiple Columns

print(sales[["Customer", "Product", "Price"]])

# Selecting Rows using iloc

print("\nFirst Row")

print(sales.iloc[0])

print("\nFirst Five Rows")

print(sales.iloc[:5])

print("\nRows 2 to 6")

print(sales.iloc[2:7])

# Selecting with loc

print("\nUsing loc")

print(sales.loc[0:3])

# Filtering

print("\nElectronics Products")

electronics = sales[sales["Category"] == "Electronics"]

print(electronics)

print("\nPrice Greater Than 10000")

print(sales[sales["Price"] > 10000])

print("\nCity is Bangalore")

print(sales[sales["City"] == "Bangalore"])

print("\nMultiple Conditions")

print(

    sales[
        (sales["Category"] == "Electronics")
        & (sales["Price"] > 1000)
    ]

)

print("\nOR Condition")

print(

    sales[
        (sales["City"] == "Delhi")
        | (sales["City"] == "Mumbai")
    ]

)

# isin()

print("\nUsing isin()")

print(

    sales[
        sales["City"].isin(["Delhi", "Mumbai"])
    ]

)

# Query

print("\nUsing query()")

print(

    sales.query("Quantity >= 2")
)