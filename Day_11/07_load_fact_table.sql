INSERT INTO fact_sales
(
customer_key,
product_key,
store_key,
date_key,
quantity,
sales_amount
)

SELECT

dc.customer_key,

dp.product_key,

ds.store_key,

TO_CHAR(ss.sale_date,'YYYYMMDD')::INT,

ss.quantity,

ss.quantity * dp.price

FROM staging_sales ss

JOIN dim_customer dc

ON ss.customer_id=dc.customer_id

JOIN dim_product dp

ON ss.product_id=dp.product_id

JOIN dim_store ds

ON ss.store_id=ds.store_id;