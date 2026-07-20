-- Query 1: Complete Order Details
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    o.order_date,
    p.product_name,
    p.category,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi
    ON o.order_id = oi.order_id
INNER JOIN products p
    ON oi.product_id = p.product_id
ORDER BY o.order_id;

-------------------------------------------------------------
-- Query 2: Customer Purchase History
-------------------------------------------------------------
SELECT
    c.customer_name,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
ORDER BY c.customer_name, o.order_date;

-------------------------------------------------------------
-- Query 3: Total Amount of Each Order
-------------------------------------------------------------
SELECT
    o.order_id,
    c.customer_name,
    SUM(oi.quantity * p.price) AS order_total
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    o.order_id,
    c.customer_name
ORDER BY order_total DESC;

-------------------------------------------------------------
-- Query 4: Total Spending by Each Customer
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
ORDER BY total_spent DESC;

-------------------------------------------------------------
-- Query 5: Most Purchased Products
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
-- Query 6: Sales by Product Category
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
-- Query 7: Number of Orders by Each Customer
-------------------------------------------------------------
SELECT
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_orders DESC;

-------------------------------------------------------------
-- Query 8: Average Order Value for Each Customer
-------------------------------------------------------------
SELECT
    c.customer_name,
    ROUND(AVG(order_total), 2) AS average_order_value
FROM (
    SELECT
        o.order_id,
        o.customer_id,
        SUM(oi.quantity * p.price) AS order_total
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY o.order_id, o.customer_id
) t
JOIN customers c
    ON t.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY average_order_value DESC;

-------------------------------------------------------------
-- Query 9: Employee Details with Department
-------------------------------------------------------------
SELECT
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
ORDER BY d.department_name;

-------------------------------------------------------------
-- Query 10: Department Salary Report
-------------------------------------------------------------
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees,
    SUM(e.salary) AS total_salary,
    ROUND(AVG(e.salary), 2) AS average_salary
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC;

-------------------------------------------------------------
-- Query 11: Highest Purchased Product by Revenue
-------------------------------------------------------------
SELECT
    p.product_name,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 12: Customer, Product and Total Cost
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_cost
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
ORDER BY c.customer_name;