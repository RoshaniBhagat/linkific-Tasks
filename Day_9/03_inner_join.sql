-------------------------------------------------------------
-- Query 1: Display orders with customer names
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    o.order_date
FROM orders o
INNER JOIN customers c
ON o.customer_id = c.customer_id;

-------------------------------------------------------------
-- Query 2: Display ordered products
-------------------------------------------------------------
SELECT
    oi.order_item_id,
    p.product_name,
    oi.quantity
FROM order_items oi
INNER JOIN products p
ON oi.product_id = p.product_id;

-------------------------------------------------------------
-- Query 3: Customer with product purchased
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    oi.quantity
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id
ORDER BY c.customer_name;

-------------------------------------------------------------
-- Query 4: Employee with department
-------------------------------------------------------------
SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

-------------------------------------------------------------
-- Query 5: Orders with customer city
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    c.city,
    o.order_date
FROM orders o
INNER JOIN customers c
ON o.customer_id = c.customer_id
ORDER BY o.order_date;

-------------------------------------------------------------
-- Query 6: Product price with quantity ordered
-------------------------------------------------------------
SELECT
    p.product_name,
    p.price,
    oi.quantity,
    (p.price * oi.quantity) AS total_price
FROM products p
INNER JOIN order_items oi
ON p.product_id = oi.product_id
ORDER BY total_price DESC;

-------------------------------------------------------------
-- Query 7: Orders containing Electronics products
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    p.product_name,
    p.category
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id
WHERE p.category = 'Electronics';

-------------------------------------------------------------
-- Query 8: Employees earning more than 65000
-------------------------------------------------------------
SELECT
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.salary > 65000
ORDER BY e.salary DESC;

-------------------------------------------------------------
-- Query 9: Total amount for each order
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    SUM(p.price * oi.quantity) AS order_total
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id
GROUP BY
    o.order_id,
    c.customer_name
ORDER BY order_total DESC;

-------------------------------------------------------------
-- Query 10: Customer and number of products purchased
-------------------------------------------------------------
SELECT
    c.customer_name,
    SUM(oi.quantity) AS total_products
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY c.customer_name
ORDER BY total_products DESC;