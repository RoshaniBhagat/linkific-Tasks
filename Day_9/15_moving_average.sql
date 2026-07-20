-------------------------------------------------------------
-- Query 1: 3-Row Moving Average of Employee Salaries
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    ROUND(
        AVG(salary) OVER(
            ORDER BY salary
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average_salary
FROM employees;

-------------------------------------------------------------
-- Query 2: 3-Row Moving Average of Product Prices
-------------------------------------------------------------
SELECT
    product_id,
    product_name,
    price,
    ROUND(
        AVG(price) OVER(
            ORDER BY price
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average_price
FROM products;

-------------------------------------------------------------
-- Query 3: Daily Revenue
-------------------------------------------------------------
SELECT
    o.order_date,
    SUM(oi.quantity * p.price) AS daily_revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY o.order_date
ORDER BY o.order_date;

-------------------------------------------------------------
-- Query 4: 3-Day Moving Average of Daily Revenue
-------------------------------------------------------------
SELECT
    order_date,
    daily_revenue,
    ROUND(
        AVG(daily_revenue) OVER(
            ORDER BY order_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average
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
-- Query 5: 5-Row Moving Average of Product Prices
-------------------------------------------------------------
SELECT
    product_name,
    price,
    ROUND(
        AVG(price) OVER(
            ORDER BY price
            ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average
FROM products;

-------------------------------------------------------------
-- Query 6: Moving Sum of Employee Salaries
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    SUM(salary) OVER(
        ORDER BY salary
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_salary_sum
FROM employees;

-------------------------------------------------------------
-- Query 7: Moving Count of Orders
-------------------------------------------------------------
SELECT
    order_id,
    order_date,
    COUNT(*) OVER(
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_order_count
FROM orders;

-------------------------------------------------------------
-- Query 8: Moving Average Salary by Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER(
            PARTITION BY department_id
            ORDER BY salary
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS department_moving_average
FROM employees;

-------------------------------------------------------------
-- Query 9: Moving Revenue by Product Category
-------------------------------------------------------------
SELECT
    category,
    product_name,
    price,
    ROUND(
        AVG(price) OVER(
            PARTITION BY category
            ORDER BY price
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS category_moving_average
FROM products;

-------------------------------------------------------------
-- Query 10: Cumulative Moving Average
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    ROUND(
        AVG(salary) OVER(
            ORDER BY salary
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS cumulative_average
FROM employees;

-------------------------------------------------------------
-- Query 11: Moving Maximum Salary
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    MAX(salary) OVER(
        ORDER BY salary
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_max_salary
FROM employees;

-------------------------------------------------------------
-- Query 12: Moving Minimum Product Price
-------------------------------------------------------------
SELECT
    product_name,
    price,
    MIN(price) OVER(
        ORDER BY price
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_min_price
FROM products;

-------------------------------------------------------------
-- Query 13: 3-Customer Moving Spending Average
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    ROUND(
        AVG(total_spent) OVER(
            ORDER BY total_spent DESC
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_average_spending
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
-- Query 14: Moving Revenue Total
-------------------------------------------------------------
SELECT
    order_date,
    daily_revenue,
    SUM(daily_revenue) OVER(
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_revenue_total
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
-- Query 15: Moving Average of Quantities Sold
-------------------------------------------------------------
SELECT
    order_id,
    quantity,
    ROUND(
        AVG(quantity) OVER(
            ORDER BY order_id
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS moving_quantity_average
FROM order_items;