DROP TABLE IF EXISTS sales_warehouse;

CREATE TABLE sales_warehouse (

    order_id INT PRIMARY KEY,

    customer_id INT,

    customer_name VARCHAR(100),

    city VARCHAR(50),

    state VARCHAR(50),

    product_id VARCHAR(10),

    product_name VARCHAR(100),

    category VARCHAR(50),

    price NUMERIC(10,2),

    quantity INT,

    total_amount NUMERIC(12,2),

    order_date DATE
);