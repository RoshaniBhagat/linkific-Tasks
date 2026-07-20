-------------------------------------------------------------
-- Query 1: Previous Employee Salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    LAG(salary) OVER(
        ORDER BY salary
    ) AS previous_salary
FROM employees;

-------------------------------------------------------------
-- Query 2: Next Employee Salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    LEAD(salary) OVER(
        ORDER BY salary
    ) AS next_salary
FROM employees;

-------------------------------------------------------------
-- Query 3: Salary Difference from Previous Employee
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    salary -
    LAG(salary) OVER(
        ORDER BY salary
    ) AS salary_difference
FROM employees;

-------------------------------------------------------------
-- Query 4: Previous Product Price
-------------------------------------------------------------
SELECT
    product_name,
    price,
    LAG(price) OVER(
        ORDER BY price
    ) AS previous_price
FROM products;

-------------------------------------------------------------
-- Query 5: Next Product Price
-------------------------------------------------------------
SELECT
    product_name,
    price,
    LEAD(price) OVER(
        ORDER BY price
    ) AS next_price
FROM products;

-------------------------------------------------------------
-- Query 6: Price Difference Between Products
-------------------------------------------------------------
SELECT
    product_name,
    price,
    price -
    LAG(price) OVER(
        ORDER BY price
    ) AS price_difference
FROM products;

-------------------------------------------------------------
-- Query 7: Previous Order Date
-------------------------------------------------------------
SELECT
    order_id,
    order_date,
    LAG(order_date) OVER(
        ORDER BY order_date
    ) AS previous_order_date
FROM orders;

-------------------------------------------------------------
-- Query 8: Days Between Orders
-------------------------------------------------------------
SELECT
    order_id,
    order_date,
    order_date -
    LAG(order_date) OVER(
        ORDER BY order_date
    ) AS days_difference
FROM orders;

-------------------------------------------------------------
-- Query 9: Previous Customer Spending
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    LAG(total_spent) OVER(
        ORDER BY total_spent DESC
    ) AS previous_customer_spending
FROM
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
) customer_sales;

-------------------------------------------------------------
-- Query 10: Compare Salary Within Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    LAG(salary) OVER(
        PARTITION BY department_id
        ORDER BY salary
    ) AS previous_department_salary
FROM employees;

-------------------------------------------------------------
-- Query 11: Next Salary Within Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    LEAD(salary) OVER(
        PARTITION BY department_id
        ORDER BY salary
    ) AS next_department_salary
FROM employees;

-------------------------------------------------------------
-- Query 12: Revenue Difference Between Products
-------------------------------------------------------------
SELECT
    product_name,
    revenue,
    revenue -
    LAG(revenue) OVER(
        ORDER BY revenue DESC
    ) AS revenue_difference
FROM
(
    SELECT
        p.product_name,
        SUM(oi.quantity * p.price) AS revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
) product_revenue;

-------------------------------------------------------------
-- Query 13: Previous Running Revenue
-------------------------------------------------------------
SELECT
    order_date,
    daily_revenue,
    LAG(daily_revenue) OVER(
        ORDER BY order_date
    ) AS previous_day_revenue
FROM
(
    SELECT
        o.order_date,
        SUM(oi.quantity * p.price) AS daily_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY o.order_date
) daily_sales;

-------------------------------------------------------------
-- Query 14: Revenue Growth
-------------------------------------------------------------
SELECT
    order_date,
    daily_revenue,
    daily_revenue -
    LAG(daily_revenue) OVER(
        ORDER BY order_date
    ) AS revenue_growth
FROM
(
    SELECT
        o.order_date,
        SUM(oi.quantity * p.price) AS daily_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY o.order_date
) sales;

-------------------------------------------------------------
-- Query 15: Next Order Date
-------------------------------------------------------------
SELECT
    order_id,
    order_date,
    LEAD(order_date) OVER(
        ORDER BY order_date
    ) AS next_order_date
FROM orders;