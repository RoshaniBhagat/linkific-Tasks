"""
Main ETL Pipeline

Steps
------
1. Extract data
2. Transform data
3. Load data into PostgreSQL
4. Export final dataset
5. Log every step
"""

from extraction.extract_csv import (
    extract_customers,
    extract_products,
    extract_orders
)

from transformation.transform import transform_data

from loading.load_data import (
    load_customers,
    load_products,
    load_sales,
    load_warehouse
)

from loading.incremental_load import filter_new_records

from utils.helper import (
    export_to_csv,
    display_shape
)

from utils.logger import get_logger


logger = get_logger()


def run_pipeline():

    logger.info("=" * 60)
    logger.info("ETL PIPELINE STARTED")
    logger.info("=" * 60)

    try:

        # ----------------------------------------
        # EXTRACT
        # ----------------------------------------

        logger.info("Extracting datasets...")

        customers = extract_customers()
        products = extract_products()
        orders = extract_orders()

        logger.info("Extraction completed.")

        # ----------------------------------------
        # TRANSFORM
        # ----------------------------------------

        logger.info("Transforming datasets...")

        final_df = transform_data(
            customers,
            products,
            orders
        )

        display_shape(final_df, "Final Dataset")

        logger.info("Transformation completed.")

        # ----------------------------------------
        # LOAD MASTER TABLES
        # ----------------------------------------

        logger.info("Loading Customers...")

        load_customers(customers)

        logger.info("Loading Products...")

        load_products(products)

        logger.info("Loading Sales...")

        load_sales(orders)

        # ----------------------------------------
        # INCREMENTAL LOAD
        # ----------------------------------------

        logger.info("Checking Incremental Records...")

        new_records = filter_new_records(final_df)

        if len(new_records) > 0:

            load_warehouse(new_records)

            logger.info(
                f"{len(new_records)} records loaded into warehouse."
            )

        else:

            logger.info(
                "No new records found."
            )

        # ----------------------------------------
        # EXPORT CSV
        # ----------------------------------------

        export_to_csv(final_df)

        logger.info("CSV Export Completed.")

        logger.info("ETL Pipeline Finished Successfully.")

        print("\nETL Pipeline Executed Successfully!")

    except Exception as e:

        logger.error(str(e))

        print("Pipeline Failed.")

        print(e)


if __name__ == "__main__":

    run_pipeline()