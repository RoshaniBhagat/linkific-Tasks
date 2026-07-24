from database.db_connection import get_connection


def get_last_order_id():
    """
    Returns the largest order_id currently in the warehouse.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(order_id), 0) FROM sales_warehouse"
    )

    last_id = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return last_id


def filter_new_records(final_df):
    """
    Keep only records with order_id greater than the last loaded order.
    """
    last_order = get_last_order_id()

    new_records = final_df[
        final_df["order_id"] > last_order
    ]

    print(f"Last Loaded Order ID : {last_order}")
    print(f"New Records : {len(new_records)}")

    return new_records