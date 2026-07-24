from pathlib import Path

# -------------------------------
# Project Paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "datasets"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

CUSTOMERS_FILE = DATASET_DIR / "customers.csv"
PRODUCTS_FILE = DATASET_DIR / "products.csv"
ORDERS_FILE = DATASET_DIR / "orders.csv"

OUTPUT_FILE = OUTPUT_DIR / "final_dataset.csv"
LOG_FILE = LOG_DIR / "etl.log"

# -------------------------------
# PostgreSQL Configuration
# -------------------------------

DB_CONFIG = {
    "host": "localhost",
    "database": "etl_project",
    "user": "postgres",
    "password": "1234",
    "port": 5432
}