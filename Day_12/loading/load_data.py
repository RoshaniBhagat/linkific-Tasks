import pandas as pd
from database.db_connection import get_connection


def load_customers(customers_df):
    """
    Load customers into PostgreSQL.
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO customers
    (customer_id, customer_name, email, city, state)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (customer_id)
    DO NOTHING;
    """

    for row in customers_df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()

    print("Customers loaded successfully.")


def load_products(products_df):
    """
    Load products into PostgreSQL.
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO products
    (product_id, product_name, category, price)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (product_id)
    DO NOTHING;
    """

    for row in products_df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()

    print("Products loaded successfully.")


def load_sales(orders_df):
    """
    Load sales/orders into PostgreSQL.
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO sales
    (order_id, customer_id, product_id, quantity, order_date)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (order_id)
    DO NOTHING;
    """

    for row in orders_df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()

    print("Sales loaded successfully.")


def load_warehouse(final_df):
    """
    Load transformed data into warehouse table.
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO sales_warehouse
    (
        order_id,
        customer_id,
        customer_name,
        city,
        state,
        product_id,
        product_name,
        category,
        price,
        quantity,
        total_amount,
        order_date
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (order_id)
    DO NOTHING;
    """

    for row in final_df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()

    print("Warehouse loaded successfully.")