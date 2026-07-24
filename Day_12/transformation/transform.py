from transformation.clean_data import (
    clean_customers,
    clean_products,
    clean_orders,
)

from transformation.merge_data import merge_datasets


def transform_data(customers_df, products_df, orders_df):
    """
    Perform complete transformation process.
    """

    # Cleaning
    customers_df = clean_customers(customers_df)
    products_df = clean_products(products_df)
    orders_df = clean_orders(orders_df)

    # Merge
    final_df = merge_datasets(
        customers_df,
        products_df,
        orders_df,
    )

    # Business Calculation
    final_df["total_amount"] = (
        final_df["price"] *
        final_df["quantity"]
    )

    # Reorder columns
    final_df = final_df[
        [
            "order_id",
            "customer_id",
            "customer_name",
            "city",
            "state",
            "product_id",
            "product_name",
            "category",
            "price",
            "quantity",
            "total_amount",
            "order_date",
        ]
    ]

    return final_df