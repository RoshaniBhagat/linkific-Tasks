-------------------------------------------------------------
-- Query 1: Employees earning more than average salary
-------------------------------------------------------------
SELECT
    employee_id,
    employee_name,
    salary
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);

-------------------------------------------------------------
-- Query 2: Most expensive product
-------------------------------------------------------------
SELECT
    product_name,
    price
FROM products
WHERE price =
(
    SELECT MAX(price)
    FROM products
);

-------------------------------------------------------------
-- Query 3: Customers who placed at least one order
-------------------------------------------------------------
SELECT
    customer_name
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);

-------------------------------------------------------------
-- Query 4: Customers who never placed an order
-------------------------------------------------------------
SELECT
    customer_name
FROM customers
WHERE customer_id NOT IN
(
    SELECT customer_id
    FROM orders
);

-------------------------------------------------------------
-- Query 5: Products that have been ordered
-------------------------------------------------------------
SELECT
    product_name
FROM products
WHERE product_id IN
(
    SELECT product_id
    FROM order_items
);

-------------------------------------------------------------
-- Query 6: Products never ordered
-------------------------------------------------------------
SELECT
    product_name
FROM products
WHERE product_id NOT IN
(
    SELECT product_id
    FROM order_items
);

-------------------------------------------------------------
-- Query 7: Employees earning more than John
-------------------------------------------------------------
SELECT
    employee_name,
    salary
FROM employees
WHERE salary >
(
    SELECT salary
    FROM employees
    WHERE employee_name = 'John'
);

-------------------------------------------------------------
-- Query 8: Orders with total amount greater than average order value
-------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        o.order_id,
        SUM(oi.quantity * p.price) AS order_total
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY o.order_id
) order_summary
WHERE order_total >
(
    SELECT AVG(order_total)
    FROM
    (
        SELECT
            SUM(oi.quantity * p.price) AS order_total
        FROM orders o
        JOIN order_items oi
            ON o.order_id = oi.order_id
        JOIN products p
            ON oi.product_id = p.product_id
        GROUP BY o.order_id
    ) avg_orders
);

-------------------------------------------------------------
-- Query 9: Departments having employees
-------------------------------------------------------------
SELECT
    department_name
FROM departments d
WHERE EXISTS
(
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.department_id
);

-------------------------------------------------------------
-- Query 10: Customers with spending above average
-------------------------------------------------------------
SELECT *
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
) customer_sales
WHERE total_spent >
(
    SELECT AVG(total_spent)
    FROM
    (
        SELECT
            SUM(oi.quantity * p.price) AS total_spent
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        JOIN products p
            ON oi.product_id = p.product_id
        GROUP BY c.customer_name
    ) avg_sales
);

-------------------------------------------------------------
-- Query 11: Correlated Subquery
-- Employees earning more than department average
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary
FROM employees e1
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.department_id = e2.department_id
);

-------------------------------------------------------------
-- Query 12: Products costing more than category average
-------------------------------------------------------------
SELECT
    product_name,
    category,
    price
FROM products p1
WHERE price >
(
    SELECT AVG(price)
    FROM products p2
    WHERE p1.category = p2.category
);

-------------------------------------------------------------
-- Query 13: Employee with Highest Salary in Each Department
-------------------------------------------------------------
SELECT
    employee_name,
    department_id,
    salary
FROM employees e1
WHERE salary =
(
    SELECT MAX(salary)
    FROM employees e2
    WHERE e1.department_id = e2.department_id
);

-------------------------------------------------------------
-- Query 14: Customers who purchased Electronics
-------------------------------------------------------------
SELECT DISTINCT
    customer_name
FROM customers
WHERE customer_id IN
(
    SELECT o.customer_id
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    JOIN products p
        ON oi.product_id = p.product_id
    WHERE p.category = 'Electronics'
);

-------------------------------------------------------------
-- Query 15: Employees earning more than ALL employees in HR
-------------------------------------------------------------
SELECT
    employee_name,
    salary
FROM employees
WHERE salary > ALL
(
    SELECT salary
    FROM employees
    WHERE department_id = 1
);