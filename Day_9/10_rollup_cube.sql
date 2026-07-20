-------------------------------------------------------------
-- Query 1: Sales by Category with Grand Total (ROLLUP)
-------------------------------------------------------------
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS total_sales
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY ROLLUP(p.category);

-------------------------------------------------------------
-- Query 2: Employee Count by Department with Total
-------------------------------------------------------------
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY ROLLUP(d.department_name);

-------------------------------------------------------------
-- Query 3: Revenue by Category and Product
-------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY ROLLUP(p.category, p.product_name)
ORDER BY p.category, p.product_name;

-------------------------------------------------------------
-- Query 4: Orders by Customer and Month
-------------------------------------------------------------
SELECT
    c.customer_name,
    EXTRACT(MONTH FROM o.order_date) AS order_month,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY ROLLUP(c.customer_name, order_month)
ORDER BY c.customer_name;

-------------------------------------------------------------
-- Query 5: Sales using CUBE
-------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY CUBE(p.category, p.product_name)
ORDER BY p.category, p.product_name;

-------------------------------------------------------------
-- Query 6: Employee Salary using CUBE
-------------------------------------------------------------
SELECT
    d.department_name,
    e.employee_name,
    SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY CUBE(d.department_name, e.employee_name)
ORDER BY d.department_name;

-------------------------------------------------------------
-- Query 7: GROUPING SETS Example
-------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY GROUPING SETS
(
    (p.category),
    (p.product_name),
    ()
);

-------------------------------------------------------------
-- Query 8: Department Salary Summary
-------------------------------------------------------------
SELECT
    d.department_name,
    ROUND(AVG(e.salary),2) AS average_salary
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY ROLLUP(d.department_name);

-------------------------------------------------------------
-- Query 9: Customer Spending Summary
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
GROUP BY ROLLUP(c.customer_name);

-------------------------------------------------------------
-- Query 10: Monthly Revenue with Grand Total
-------------------------------------------------------------
SELECT
    EXTRACT(MONTH FROM o.order_date) AS order_month,
    SUM(oi.quantity * p.price) AS monthly_revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY ROLLUP(order_month)
ORDER BY order_month;

-------------------------------------------------------------
-- Query 11: Sales by Category and Month
-------------------------------------------------------------
SELECT
    p.category,
    EXTRACT(MONTH FROM o.order_date) AS order_month,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN orders o
ON oi.order_id = o.order_id
GROUP BY CUBE(p.category, order_month)
ORDER BY p.category, order_month;

-------------------------------------------------------------
-- Query 12: Product Quantity Summary
-------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY GROUPING SETS
(
    (p.category, p.product_name),
    (p.category),
    ()
)
ORDER BY p.category, p.product_name;