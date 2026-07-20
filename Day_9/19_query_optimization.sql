-------------------------------------------------------------
-- Query 1: View Execution Plan
-------------------------------------------------------------
EXPLAIN
SELECT *
FROM customers;

-------------------------------------------------------------
-- Query 2: View Actual Execution Statistics
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT *
FROM products
WHERE category = 'Electronics';

-------------------------------------------------------------
-- Query 3: Create Index on Customer Email
-------------------------------------------------------------
CREATE INDEX idx_customers_email
ON customers(email);

-------------------------------------------------------------
-- Query 4: Create Index on Product Category
-------------------------------------------------------------
CREATE INDEX idx_products_category
ON products(category);

-------------------------------------------------------------
-- Query 5: Create Index on Order Date
-------------------------------------------------------------
CREATE INDEX idx_orders_order_date
ON orders(order_date);

-------------------------------------------------------------
-- Query 6: Create Composite Index
-------------------------------------------------------------
CREATE INDEX idx_order_items_order_product
ON order_items(order_id, product_id);

-------------------------------------------------------------
-- Query 7: Query Using Indexed Column
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    customer_id,
    customer_name,
    email
FROM customers
WHERE email = 'john@example.com';

-------------------------------------------------------------
-- Query 8: Filter Before Joining
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    c.customer_name,
    o.order_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_date >= '2026-01-01';

-------------------------------------------------------------
-- Query 9: Select Only Required Columns
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    product_name,
    price
FROM products
WHERE price > 500;

-------------------------------------------------------------
-- Query 10: Aggregate with GROUP BY
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category;

-------------------------------------------------------------
-- Query 11: Optimized Join
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    c.customer_name,
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY c.customer_name;

-------------------------------------------------------------
-- Query 12: EXISTS Instead of IN
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

-------------------------------------------------------------
-- Query 13: LIMIT for Testing
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 5;

-------------------------------------------------------------
-- Query 14: Check Index Usage
-------------------------------------------------------------
EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE order_date = '2026-01-10';

-------------------------------------------------------------
-- Query 15: List Existing Indexes
-------------------------------------------------------------
SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;