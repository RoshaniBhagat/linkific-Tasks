import pandas as pd


def clean_customers(customers_df):
    """
    Clean customer data.
    """

    customers_df = customers_df.copy()

    # Remove duplicate rows
    customers_df.drop_duplicates(inplace=True)

    # Remove rows with missing customer_id
    customers_df.dropna(subset=["customer_id"], inplace=True)

    # Remove leading/trailing spaces
    customers_df["customer_name"] = customers_df["customer_name"].str.strip()

    # Convert email to lowercase
    customers_df["email"] = customers_df["email"].str.lower()

    return customers_df


def clean_products(products_df):
    """
    Clean product data.
    """

    products_df = products_df.copy()

    products_df.drop_duplicates(inplace=True)

    products_df.dropna(subset=["product_id"], inplace=True)

    products_df["product_name"] = products_df["product_name"].str.strip()

    products_df["category"] = products_df["category"].str.title()

    return products_df


def clean_orders(orders_df):
    """
    Clean order data.
    """

    orders_df = orders_df.copy()

    orders_df.drop_duplicates(inplace=True)

    orders_df.dropna(inplace=True)

    orders_df["order_date"] = pd.to_datetime(
        orders_df["order_date"]
    )

    return orders_df