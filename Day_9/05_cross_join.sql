-- Query 1: Every customer with every product
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name
FROM customers c
CROSS JOIN products p
ORDER BY c.customer_name, p.product_name;

-------------------------------------------------------------
-- Query 2: Every employee with every department
-------------------------------------------------------------
SELECT
    e.employee_name,
    d.department_name
FROM employees e
CROSS JOIN departments d
ORDER BY e.employee_name;

-------------------------------------------------------------
-- Query 3: Count total combinations of customers and products
-------------------------------------------------------------
SELECT
    COUNT(*) AS total_combinations
FROM customers
CROSS JOIN products;

-------------------------------------------------------------
-- Query 4: Show product price for every customer
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    p.price
FROM customers c
CROSS JOIN products p
ORDER BY c.customer_name;

-------------------------------------------------------------
-- Query 5: Customers from New York with every Electronics product
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    p.price
FROM customers c
CROSS JOIN products p
WHERE c.city = 'New York'
  AND p.category = 'Electronics';

-------------------------------------------------------------
-- Query 6: Every department with every product category
-------------------------------------------------------------
SELECT DISTINCT
    d.department_name,
    p.category
FROM departments d
CROSS JOIN products p
ORDER BY d.department_name, p.category;

-------------------------------------------------------------
-- Query 7: Every employee with every customer
-------------------------------------------------------------
SELECT
    e.employee_name,
    c.customer_name
FROM employees e
CROSS JOIN customers c
ORDER BY e.employee_name;

-------------------------------------------------------------
-- Query 8: Count combinations of employees and customers
-------------------------------------------------------------
SELECT
    COUNT(*) AS total_pairs
FROM employees
CROSS JOIN customers;

-------------------------------------------------------------
-- Query 9: Show every customer with every product costing above 200
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    p.price
FROM customers c
CROSS JOIN products p
WHERE p.price > 200
ORDER BY p.price DESC;

-------------------------------------------------------------
-- Query 10: Display first 20 combinations
-------------------------------------------------------------
SELECT
    c.customer_name,
    p.product_name,
    p.price
FROM customers c
CROSS JOIN products p
LIMIT 20;