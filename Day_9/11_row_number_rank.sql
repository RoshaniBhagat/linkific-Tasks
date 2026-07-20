------------------------------------------------------------
-- Query 1: ROW_NUMBER() by Salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_number
FROM employees;

-------------------------------------------------------------
-- Query 2: RANK() by Salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-------------------------------------------------------------
-- Query 3: DENSE_RANK() by Salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS dense_rank
FROM employees;

-------------------------------------------------------------
-- Query 4: ROW_NUMBER() by Product Price
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price,
    ROW_NUMBER() OVER(ORDER BY price DESC) AS row_number
FROM products;

-------------------------------------------------------------
-- Query 5: Rank Products by Price
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price,
    RANK() OVER(ORDER BY price DESC) AS price_rank
FROM products;

-------------------------------------------------------------
-- Query 6: Dense Rank Products
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price,
    DENSE_RANK() OVER(ORDER BY price DESC) AS dense_rank
FROM products;

-------------------------------------------------------------
-- Query 7: Top 5 Highest Paid Employees
-------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        employee_name,
        salary,
        ROW_NUMBER() OVER(ORDER BY salary DESC) AS rn
    FROM employees
) t
WHERE rn <= 5;

-------------------------------------------------------------
-- Query 8: Top 3 Most Expensive Products
-------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        product_name,
        price,
        ROW_NUMBER() OVER(ORDER BY price DESC) AS rn
    FROM products
) t
WHERE rn <= 3;

-------------------------------------------------------------
-- Query 9: NTILE() Divide Employees into 4 Groups
-------------------------------------------------------------
SELECT
    employee_name,
    salary,
    NTILE(4) OVER(ORDER BY salary DESC) AS salary_group
FROM employees;

-------------------------------------------------------------
-- Query 10: NTILE() Divide Products into 3 Groups
-------------------------------------------------------------
SELECT
    product_name,
    price,
    NTILE(3) OVER(ORDER BY price DESC) AS product_group
FROM products;

-------------------------------------------------------------
-- Query 11: Row Number for Orders by Date
-------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_date,
    ROW_NUMBER() OVER(ORDER BY order_date) AS order_sequence
FROM orders;

-------------------------------------------------------------
-- Query 12: Rank Customers by Total Spending
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    RANK() OVER(ORDER BY total_spent DESC) AS spending_rank
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
-- Query 13: Dense Rank Customers
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    DENSE_RANK() OVER(ORDER BY total_spent DESC) AS spending_rank
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
-- Query 14: Highest Salary in Each Department
-------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        e.employee_name,
        d.department_name,
        e.salary,
        ROW_NUMBER() OVER(
            PARTITION BY d.department_name
            ORDER BY e.salary DESC
        ) AS rn
    FROM employees e
    JOIN departments d
        ON e.department_id = d.department_id
) department_salary
WHERE rn = 1;

-------------------------------------------------------------
-- Query 15: Highest Revenue Product
-------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        p.product_name,
        SUM(oi.quantity * p.price) AS revenue,
        ROW_NUMBER() OVER(
            ORDER BY SUM(oi.quantity * p.price) DESC
        ) AS rn
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
) product_revenue
WHERE rn = 1;