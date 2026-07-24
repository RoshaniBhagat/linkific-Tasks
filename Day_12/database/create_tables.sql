-- Drop existing tables
DROP TABLE IF EXISTS sales;

DROP TABLE IF EXISTS customers;

DROP TABLE IF EXISTS products;

---------------------------------------------------
-- Customers Table
---------------------------------------------------

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50)
);

---------------------------------------------------
-- Products Table
---------------------------------------------------

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);

---------------------------------------------------
-- Sales Table
---------------------------------------------------

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id VARCHAR(10) REFERENCES products(product_id),
    quantity INT,
    order_date DATE
);