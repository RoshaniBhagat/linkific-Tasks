-------------------------------------------------------------
-- Query 1: Running Total of Employee Salaries
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    SUM(salary) OVER(
        ORDER BY salary
    ) AS running_salary_total
FROM employees;

-------------------------------------------------------------
-- Query 2: Running Total of Product Prices
-------------------------------------------------------------
SELECT
    product_id,
    product_name,
    price,
    SUM(price) OVER(
        ORDER BY price
    ) AS running_price_total
FROM products;

-------------------------------------------------------------
-- Query 3: Running Count of Orders
-------------------------------------------------------------
SELECT
    order_id,
    order_date,
    COUNT(*) OVER(
        ORDER BY order_date
    ) AS running_order_count
FROM orders;

-------------------------------------------------------------
-- Query 4: Running Revenue by Order Date
-------------------------------------------------------------
SELECT
    o.order_date,
    o.order_id,
    SUM(oi.quantity * p.price) AS order_amount,
    SUM(SUM(oi.quantity * p.price))
    OVER(
        ORDER BY o.order_date
    ) AS running_revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY
    o.order_date,
    o.order_id
ORDER BY o.order_date;

-------------------------------------------------------------
-- Query 5: Running Quantity Sold
-------------------------------------------------------------
SELECT
    o.order_date,
    SUM(oi.quantity) AS quantity_sold,
    SUM(SUM(oi.quantity))
    OVER(
        ORDER BY o.order_date
    ) AS cumulative_quantity
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY o.order_date
ORDER BY o.order_date;

-------------------------------------------------------------
-- Query 6: Running Total by Product Category
-------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    p.price,
    SUM(p.price) OVER(
        PARTITION BY p.category
        ORDER BY p.price
    ) AS category_running_total
FROM products p;

-------------------------------------------------------------
-- Query 7: Running Salary by Department
-------------------------------------------------------------
SELECT
    d.department_name,
    e.employee_name,
    e.salary,
    SUM(e.salary)
    OVER(
        PARTITION BY d.department_name
        ORDER BY e.salary
    ) AS department_running_salary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;

-------------------------------------------------------------
-- Query 8: Cumulative Customer Spending
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    SUM(total_spent)
    OVER(
        ORDER BY total_spent
    ) AS cumulative_spending
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
-- Query 9: Running Average Salary
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    ROUND(
        AVG(salary)
        OVER(
            ORDER BY salary
        ),2
    ) AS running_average_salary
FROM employees;

-------------------------------------------------------------
-- Query 10: Running Maximum Salary
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    MAX(salary)
    OVER(
        ORDER BY salary
    ) AS running_maximum_salary
FROM employees;

-------------------------------------------------------------
-- Query 11: Running Minimum Product Price
-------------------------------------------------------------
SELECT
    product_name,
    price,
    MIN(price)
    OVER(
        ORDER BY price
    ) AS running_minimum_price
FROM products;

-------------------------------------------------------------
-- Query 12: Running Revenue by Customer
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    SUM(total_spent)
    OVER(
        ORDER BY customer_name
    ) AS cumulative_customer_revenue
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
) sales_summary;

-------------------------------------------------------------
-- Query 13: Percentage of Total Salary
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    ROUND(
        salary * 100.0 /
        SUM(salary) OVER(),
        2
    ) AS salary_percentage
FROM employees;

-------------------------------------------------------------
-- Query 14: Percentage of Product Revenue
-------------------------------------------------------------
SELECT
    product_name,
    revenue,
    ROUND(
        revenue * 100.0 /
        SUM(revenue) OVER(),
        2
    ) AS revenue_percentage
FROM
(
    SELECT
        p.product_name,
        SUM(oi.quantity * p.price) AS revenue
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    GROUP BY p.product_name
) product_sales;

-------------------------------------------------------------
-- Query 15: Cumulative Monthly Revenue
-------------------------------------------------------------
SELECT
    EXTRACT(MONTH FROM o.order_date) AS month,
    SUM(oi.quantity * p.price) AS monthly_revenue,
    SUM(SUM(oi.quantity * p.price))
    OVER(
        ORDER BY EXTRACT(MONTH FROM o.order_date)
    ) AS cumulative_monthly_revenue
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products p
ON oi.product_id = p.product_id
GROUP BY EXTRACT(MONTH FROM o.order_date)
ORDER BY month;