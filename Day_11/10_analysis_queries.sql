Total Sales
SELECT

SUM(sales_amount)
FROM fact_sales;

Sales by Product
SELECT
p.product_name,
SUM(f.sales_amount)
FROM fact_sales f
JOIN dim_product p
ON f.product_key=p.product_key
GROUP BY p.product_name;

Sales by Store
SELECT
s.store_name,
SUM(f.sales_amount)
FROM fact_sales f
JOIN dim_store s
ON f.store_key=s.store_key
GROUP BY s.store_name;

Sales by Customer
SELECT
c.customer_name,
SUM(f.sales_amount)
FROM fact_sales f
JOIN dim_customer c
ON f.customer_key=c.customer_key
GROUP BY c.customer_name;

Sales by Month
SELECT
d.month,
SUM(f.sales_amount)
FROM fact_sales f
JOIN dim_date d
ON f.date_key=d.date_key
GROUP BY d.month
ORDER BY d.month;