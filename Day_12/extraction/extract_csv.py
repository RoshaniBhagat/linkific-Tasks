import pandas as pd
from pathlib import Path


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset folder
DATASET_DIR = BASE_DIR / "datasets"


def extract_customers():
    """
    Read customers.csv
    """
    file_path = DATASET_DIR / "customers.csv"
    customers_df = pd.read_csv(file_path)

    print("Customers data extracted successfully.")
    return customers_df


def extract_products():
    """
    Read products.csv
    """
    file_path = DATASET_DIR / "products.csv"
    products_df = pd.read_csv(file_path)

    print("Products data extracted successfully.")
    return products_df


def extract_orders():
    """
    Read orders.csv
    """
    file_path = DATASET_DIR / "orders.csv"
    orders_df = pd.read_csv(file_path)

    print("Orders data extracted successfully.")
    return orders_df


if __name__ == "__main__":

    customers = extract_customers()
    products = extract_products()
    orders = extract_orders()

    print("\nCustomers")
    print(customers.head())

    print("\nProducts")
    print(products.head())

    print("\nOrders")
    print(orders.head())