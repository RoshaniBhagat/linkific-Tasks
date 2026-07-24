import pandas as pd


def merge_datasets(customers_df, products_df, orders_df):
    """
    Merge customers, orders and products.
    """

    merged_df = pd.merge(
        orders_df,
        customers_df,
        on="customer_id",
        how="inner"
    )

    merged_df = pd.merge(
        merged_df,
        products_df,
        on="product_id",
        how="inner"
    )

    return merged_df