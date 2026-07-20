-- Query 1: Count customers in each city
-------------------------------------------------------------
SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-------------------------------------------------------------
-- Query 2: Count products in each category
-------------------------------------------------------------
SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;

-------------------------------------------------------------
-- Query 3: Average product price by category
-------------------------------------------------------------
SELECT
    category,
    ROUND(AVG(price), 2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

-------------------------------------------------------------
-- Query 4: Maximum and Minimum price in each category
-------------------------------------------------------------
SELECT
    category,
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM products
GROUP BY category
ORDER BY highest_price DESC;

-------------------------------------------------------------
-- Query 5: Number of orders placed by each customer
-------------------------------------------------------------
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC;

-------------------------------------------------------------
-- Query 6: Total quantity sold for each product
-------------------------------------------------------------
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;

-------------------------------------------------------------
-- Query 7: Total sales by category
-------------------------------------------------------------
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS total_sales
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

-------------------------------------------------------------
-- Query 8: Department-wise employee count
-------------------------------------------------------------
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_employees DESC;

-------------------------------------------------------------
-- Query 9: Department-wise average salary
-------------------------------------------------------------
SELECT
    d.department_name,
    ROUND(AVG(e.salary), 2) AS average_salary
FROM departments d
JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY average_salary DESC;

-------------------------------------------------------------
-- Query 10: Customers who placed more than one order
-------------------------------------------------------------
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;

-------------------------------------------------------------
-- Query 11: Categories with average price greater than 200
-------------------------------------------------------------
SELECT
    category,
    ROUND(AVG(price), 2) AS average_price
FROM products
GROUP BY category
HAVING AVG(price) > 200;

-------------------------------------------------------------
-- Query 12: Products sold more than 3 times
-------------------------------------------------------------
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name
HAVING SUM(oi.quantity) > 3
ORDER BY total_quantity DESC;

-------------------------------------------------------------
-- Query 13: Departments with average salary above 65000
-------------------------------------------------------------
SELECT
    d.department_name,
    ROUND(AVG(e.salary), 2) AS average_salary
FROM departments d
JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 65000
ORDER BY average_salary DESC;

-------------------------------------------------------------
-- Query 14: Customers spending more than 1000
-------------------------------------------------------------
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
GROUP BY c.customer_name
HAVING SUM(oi.quantity * p.price) > 1000
ORDER BY total_spent DESC;

-------------------------------------------------------------
-- Query 15: Orders containing more than one product
-------------------------------------------------------------
SELECT
    order_id,
    COUNT(product_id) AS total_products
FROM order_items
GROUP BY order_id
HAVING COUNT(product_id) > 1
ORDER BY total_products DESC;