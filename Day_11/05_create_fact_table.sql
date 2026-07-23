CREATE TABLE fact_sales
(
    sales_key SERIAL PRIMARY KEY,

    customer_key INT REFERENCES dim_customer(customer_key),

    product_key INT REFERENCES dim_product(product_key),

    store_key INT REFERENCES dim_store(store_key),

    date_key INT REFERENCES dim_date(date_key),

    quantity INT,

    sales_amount NUMERIC(10,2)
);