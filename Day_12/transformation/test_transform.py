from extraction.extract_csv import (
    extract_customers,
    extract_products,
    extract_orders,
)

from transformation.transform import transform_data


customers = extract_customers()
products = extract_products()
orders = extract_orders()

final_df = transform_data(
    customers,
    products,
    orders,
)

print(final_df.head())

print("\nColumns:")
print(final_df.columns)

print("\nShape:")
print(final_df.shape)