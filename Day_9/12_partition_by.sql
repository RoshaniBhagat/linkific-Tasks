-------------------------------------------------------------
-- Query 1: Row Number within each Department
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    department_id,
    salary,
    ROW_NUMBER() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS row_num
FROM employees;

-------------------------------------------------------------
-- Query 2: Rank Employees within each Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS dept_rank
FROM employees;

-------------------------------------------------------------
-- Query 3: Dense Rank Employees within each Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    DENSE_RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS dense_rank
FROM employees;

-------------------------------------------------------------
-- Query 4: Highest Paid Employee in Each Department
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
) t
WHERE rn = 1;

-------------------------------------------------------------
-- Query 5: Average Salary by Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    ROUND(
        AVG(salary) OVER(
            PARTITION BY department_id
        ), 2
    ) AS department_average
FROM employees;

-------------------------------------------------------------
-- Query 6: Total Salary by Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    SUM(salary) OVER(
        PARTITION BY department_id
    ) AS department_salary_total
FROM employees;

-------------------------------------------------------------
-- Query 7: Employee Count in Each Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    COUNT(*) OVER(
        PARTITION BY department_id
    ) AS department_employee_count
FROM employees;

-------------------------------------------------------------
-- Query 8: Minimum and Maximum Salary by Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary,
    MIN(salary) OVER(
        PARTITION BY department_id
    ) AS minimum_salary,
    MAX(salary) OVER(
        PARTITION BY department_id
    ) AS maximum_salary
FROM employees;

-------------------------------------------------------------
-- Query 9: Product Ranking within Category
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price,
    RANK() OVER(
        PARTITION BY category
        ORDER BY price DESC
    ) AS category_rank
FROM products;

-------------------------------------------------------------
-- Query 10: Average Product Price by Category
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price,
    ROUND(
        AVG(price) OVER(
            PARTITION BY category
        ),2
    ) AS category_average_price
FROM products;

-------------------------------------------------------------
-- Query 11: Total Revenue by Product Category
-------------------------------------------------------------
SELECT
    p.product_name,
    p.category,
    SUM(oi.quantity * p.price) OVER(
        PARTITION BY p.category
    ) AS category_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id;

-------------------------------------------------------------
-- Query 12: Customer Order Count
-------------------------------------------------------------
SELECT
    c.customer_name,
    o.order_id,
    COUNT(o.order_id) OVER(
        PARTITION BY c.customer_id
    ) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;

-------------------------------------------------------------
-- Query 13: Customer Total Spending
-------------------------------------------------------------
SELECT
    customer_name,
    total_spent,
    SUM(total_spent) OVER() AS overall_sales
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
-- Query 14: Running Count of Employees by Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    COUNT(*) OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS running_employee_count
FROM employees;

-------------------------------------------------------------
-- Query 15: Top 2 Highest Paid Employees in Each Department
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
) ranked_employees
WHERE rn <= 2
ORDER BY department_name, salary DESC;