-- ==========================================================
-- Day 9 - Common Table Expressions (CTE)
-- File: 17_cte.sql
-- Description: Practice WITH clause (CTEs)
-- Database: PostgreSQL
-- ==========================================================

-------------------------------------------------------------
-- Query 1: Employees earning above average salary
-------------------------------------------------------------
WITH avg_salary AS
(
    SELECT AVG(salary) AS average_salary
    FROM employees
)
SELECT
    employee_id,
    employee_name,
    salary
FROM employees
WHERE salary >
(
    SELECT average_salary
    FROM avg_salary
);

-------------------------------------------------------------
-- Query 2: Customer Spending Report
-------------------------------------------------------------
WITH customer_sales AS
(
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(oi.quantity * p.price) AS total_spent
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT *
FROM customer_sales
ORDER BY total_spent DESC;

-------------------------------------------------------------
-- Query 3: Highest Spending Customer
-------------------------------------------------------------
WITH customer_sales AS
(
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
)
SELECT *
FROM customer_sales
WHERE total_spent =
(
    SELECT MAX(total_spent)
    FROM customer_sales
);

-------------------------------------------------------------
-- Query 4: Department Salary Summary
-------------------------------------------------------------
WITH department_salary AS
(
    SELECT
        d.department_name,
        COUNT(e.employee_id) AS total_employees,
        SUM(e.salary) AS total_salary,
        AVG(e.salary) AS average_salary
    FROM departments d
    JOIN employees e
        ON d.department_id = e.department_id
    GROUP BY d.department_name
)
SELECT *
FROM department_salary
ORDER BY average_salary DESC;

-------------------------------------------------------------
-- Query 5: Products with Revenue
-------------------------------------------------------------
WITH product_revenue AS
(
    SELECT
        p.product_name,
        SUM(oi.quantity * p.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
)
SELECT *
FROM product_revenue
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 6: Multiple CTEs
-------------------------------------------------------------
WITH customer_sales AS
(
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(oi.quantity * p.price) AS total_spent
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name
),
average_sales AS
(
    SELECT AVG(total_spent) AS avg_spending
    FROM customer_sales
)
SELECT
    customer_name,
    total_spent
FROM customer_sales
WHERE total_spent >
(
    SELECT avg_spending
    FROM average_sales
);

-------------------------------------------------------------
-- Query 7: Employee Ranking using CTE
-------------------------------------------------------------
WITH ranked_employees AS
(
    SELECT
        employee_name,
        department_id,
        salary,
        RANK() OVER(
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT *
FROM ranked_employees
ORDER BY salary_rank;

-------------------------------------------------------------
-- Query 8: Top 3 Highest Paid Employees
-------------------------------------------------------------
WITH ranked_employees AS
(
    SELECT
        employee_name,
        salary,
        ROW_NUMBER() OVER(
            ORDER BY salary DESC
        ) AS rn
    FROM employees
)
SELECT *
FROM ranked_employees
WHERE rn <= 3;

-------------------------------------------------------------
-- Query 9: Monthly Revenue
-------------------------------------------------------------
WITH monthly_sales AS
(
    SELECT
        EXTRACT(MONTH FROM o.order_date) AS month,
        SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY month
)
SELECT *
FROM monthly_sales
ORDER BY month;

-------------------------------------------------------------
-- Query 10: Highest Revenue Month
-------------------------------------------------------------
WITH monthly_sales AS
(
    SELECT
        EXTRACT(MONTH FROM o.order_date) AS month,
        SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY month
)
SELECT *
FROM monthly_sales
WHERE revenue =
(
    SELECT MAX(revenue)
    FROM monthly_sales
);

-------------------------------------------------------------
-- Query 11: Category Revenue Report
-------------------------------------------------------------
WITH category_sales AS
(
    SELECT
        p.category,
        SUM(oi.quantity * p.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.category
)
SELECT *
FROM category_sales
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 12: Running Revenue using CTE
-------------------------------------------------------------
WITH daily_sales AS
(
    SELECT
        o.order_date,
        SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY o.order_date
)
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER(
        ORDER BY order_date
    ) AS running_total
FROM daily_sales;

-------------------------------------------------------------
-- Query 13: Employees Above Department Average
-------------------------------------------------------------
WITH department_avg AS
(
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT
    e.employee_name,
    e.salary,
    d.avg_salary
FROM employees e
JOIN department_avg d
ON e.department_id = d.department_id
WHERE e.salary > d.avg_salary;

-------------------------------------------------------------
-- Query 14: Product Sales Summary
-------------------------------------------------------------
WITH product_sales AS
(
    SELECT
        p.product_name,
        SUM(oi.quantity) AS quantity_sold,
        SUM(oi.quantity * p.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
)
SELECT *
FROM product_sales
ORDER BY revenue DESC;

-------------------------------------------------------------
-- Query 15: Customer Order Summary
-------------------------------------------------------------
WITH customer_orders AS
(
    SELECT
        c.customer_name,
        COUNT(o.order_id) AS total_orders
    FROM customers c
    LEFT JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_name
)
SELECT *
FROM customer_orders
ORDER BY total_orders DESC;