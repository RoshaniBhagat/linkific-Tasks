Customer Dimension
CREATE TABLE dim_customer
(
    customer_key SERIAL PRIMARY KEY,

    customer_id INT,

    customer_name VARCHAR(100),

    city VARCHAR(50),

    state VARCHAR(50),

    start_date DATE,

    end_date DATE,

    current_flag CHAR(1)
);

Product Dimension
CREATE TABLE dim_product
(
    product_key SERIAL PRIMARY KEY,

    product_id INT,

    product_name VARCHAR(100),

    category VARCHAR(50),

    price NUMERIC(10,2)
);

Store Dimension
CREATE TABLE dim_store
(
    store_key SERIAL PRIMARY KEY,

    store_id INT,

    store_name VARCHAR(100),

    city VARCHAR(50)
);

Date Dimension
CREATE TABLE dim_date
(
    date_key INT PRIMARY KEY,

    full_date DATE,

    year INT,

    month INT,

    day INT
);