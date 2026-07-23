Customer
INSERT INTO dim_customer
(
customer_id,
customer_name,
city,
state,
start_date,
end_date,
current_flag
)

SELECT

customer_id,
customer_name,
city,
state,
CURRENT_DATE,
NULL,
'Y'

FROM staging_customers;

Product
INSERT INTO dim_product
(
product_id,
product_name,
category,
price
)

SELECT *

FROM staging_products;

Store
INSERT INTO dim_store
(
store_id,
store_name,
city
)

SELECT *

FROM staging_stores;

Date
INSERT INTO dim_date

SELECT

TO_CHAR(sale_date,'YYYYMMDD')::INT,

sale_date,

EXTRACT(YEAR FROM sale_date),

EXTRACT(MONTH FROM sale_date),

EXTRACT(DAY FROM sale_date)

FROM staging_sales;