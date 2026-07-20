-- Query 1: Show all customers and their orders
SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

-------------------------------------------------------------

-- Query 2: Customers who have not placed any orders
SELECT
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-------------------------------------------------------------

-- Query 3: Show all departments and employees
SELECT
    d.department_name,
    e.employee_name,
    e.salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
ORDER BY d.department_name;

-------------------------------------------------------------
-- RIGHT JOIN
-------------------------------------------------------------

-- Query 4: Show all orders and customer details
SELECT
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY o.order_id;

-------------------------------------------------------------

-- Query 5: Show all products and ordered quantities
SELECT
    p.product_name,
    oi.quantity
FROM order_items oi
RIGHT JOIN products p
ON oi.product_id = p.product_id
ORDER BY p.product_name;

-------------------------------------------------------------

-- Query 6: Products that have never been ordered
SELECT
    p.product_name,
    p.category
FROM order_items oi
RIGHT JOIN products p
ON oi.product_id = p.product_id
WHERE oi.order_item_id IS NULL;

-------------------------------------------------------------
-- FULL OUTER JOIN
-------------------------------------------------------------

-- Query 7: Show all customers and all orders
SELECT
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
FULL OUTER JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY c.customer_name;

-------------------------------------------------------------

-- Query 8: Show all departments and employees
SELECT
    d.department_name,
    e.employee_name
FROM departments d
FULL OUTER JOIN employees e
ON d.department_id = e.department_id
ORDER BY d.department_name;

-------------------------------------------------------------

-- Query 9: Show all products and order items
SELECT
    p.product_name,
    oi.order_id,
    oi.quantity
FROM products p
FULL OUTER JOIN order_items oi
ON p.product_id = oi.product_id
ORDER BY p.product_name;

-------------------------------------------------------------
-- Comparison Queries
-------------------------------------------------------------

-- Query 10: Number of orders placed by each customer
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC;

-------------------------------------------------------------

-- Query 11: Number of employees in each department
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_employees DESC;

-------------------------------------------------------------

-- Query 12: List customers with or without orders
SELECT
    c.customer_name,
    COALESCE(CAST(o.order_id AS TEXT), 'No Order') AS order_status
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY c.customer_name;