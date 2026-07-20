-- Query 1: Product Category Statistics
-------------------------------------------------------------
SELECT
    category,
    COUNT(*) AS total_products,
    SUM(price) AS total_price,
    ROUND(AVG(price), 2) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

-------------------------------------------------------------
-- Query 2: Department Salary Statistics
-------------------------------------------------------------
SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_employees,
    SUM(e.salary) AS total_salary,
    ROUND(AVG(e.salary), 2) AS average_salary,
    MIN(e.salary) AS minimum_salary,
    MAX(e.salary) AS maximum_salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY average_salary DESC;

-------------------------------------------------------------
-- Query 3: Customer Order Summary
-------------------------------------------------------------
SELECT
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity) AS total_items,
    SUM(oi.quantity * p.price) AS total_spent,
    ROUND(AVG(oi.quantity * p.price), 2) AS average_item_value
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
-- Query 4: Product Sales Summary
-------------------------------------------------------------
SELECT
    p.product_name,
    COUNT(oi.order_item_id) AS times_ordered,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * p.price) AS revenue,
    ROUND(AVG(oi.quantity), 2) AS average_quantity,
    MIN(oi.quantity) AS minimum_quantity,
    MAX(oi.quantity) AS maximum_quantity
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 5: Monthly Order Statistics
-------------------------------------------------------------
SELECT
    EXTRACT(MONTH FROM order_date) AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY month
ORDER BY month;

-------------------------------------------------------------
-- Query 6: City-wise Customer Statistics
-------------------------------------------------------------
SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-------------------------------------------------------------
-- Query 7: Category Revenue Report
-------------------------------------------------------------
SELECT
    p.category,
    COUNT(DISTINCT p.product_id) AS products,
    SUM(oi.quantity) AS units_sold,
    SUM(oi.quantity * p.price) AS revenue,
    ROUND(AVG(p.price), 2) AS average_price
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 8: Employee Salary Report
-------------------------------------------------------------
SELECT
    COUNT(*) AS total_employees,
    SUM(salary) AS salary_budget,
    ROUND(AVG(salary),2) AS average_salary,
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary
FROM employees;

-------------------------------------------------------------
-- Query 9: Orders Per Customer
-------------------------------------------------------------
SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    MIN(order_date) AS first_order,
    MAX(order_date) AS latest_order
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;

-------------------------------------------------------------
-- Query 10: Order Revenue Statistics
-------------------------------------------------------------
SELECT
    o.order_id,
    COUNT(oi.product_id) AS total_products,
    SUM(oi.quantity) AS total_quantity,
    SUM(oi.quantity * p.price) AS total_amount,
    ROUND(AVG(oi.quantity * p.price),2) AS average_product_cost
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY o.order_id
ORDER BY total_amount DESC;

-------------------------------------------------------------
-- Query 11: Customers with Highest Spending
-------------------------------------------------------------
SELECT
    c.customer_name,
    SUM(oi.quantity * p.price) AS total_spent,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

-------------------------------------------------------------
-- Query 12: Overall Business Summary
-------------------------------------------------------------
SELECT
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT p.product_id) AS products,
    SUM(oi.quantity * p.price) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id;