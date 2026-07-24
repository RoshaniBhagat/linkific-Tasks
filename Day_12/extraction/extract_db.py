import pandas as pd

from database.db_connection import get_connection


def extract_customers_db():

    connection = get_connection()

    query = "SELECT * FROM customers"

    df = pd.read_sql(query, connection)

    connection.close()

    print("Customers extracted from database.")

    return df


def extract_products_db():

    connection = get_connection()

    query = "SELECT * FROM products"

    df = pd.read_sql(query, connection)

    connection.close()

    print("Products extracted from database.")

    return df


def extract_sales_db():

    connection = get_connection()

    query = "SELECT * FROM sales"

    df = pd.read_sql(query, connection)

    connection.close()

    print("Sales extracted from database.")

    return df


if __name__ == "__main__":

    customers = extract_customers_db()

    print(customers.head())