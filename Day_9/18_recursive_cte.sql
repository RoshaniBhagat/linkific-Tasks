-------------------------------------------------------------
-- Query 1: Generate Numbers from 1 to 10
-------------------------------------------------------------
WITH RECURSIVE numbers AS (
    SELECT 1 AS num

    UNION ALL

    SELECT num + 1
    FROM numbers
    WHERE num < 10
)
SELECT *
FROM numbers;

-------------------------------------------------------------
-- Query 2: Generate Even Numbers up to 20
-------------------------------------------------------------
WITH RECURSIVE even_numbers AS (
    SELECT 2 AS num

    UNION ALL

    SELECT num + 2
    FROM even_numbers
    WHERE num < 20
)
SELECT *
FROM even_numbers;

-------------------------------------------------------------
-- Query 3: Generate Dates for One Week
-------------------------------------------------------------
WITH RECURSIVE dates AS (
    SELECT DATE '2026-01-01' AS day

    UNION ALL

    SELECT day + INTERVAL '1 day'
    FROM dates
    WHERE day < DATE '2026-01-07'
)
SELECT day
FROM dates;

-------------------------------------------------------------
-- Query 4: Employee Hierarchy
-------------------------------------------------------------
WITH RECURSIVE employee_hierarchy AS (
    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh
        ON e.manager_id = eh.employee_id
)
SELECT *
FROM employee_hierarchy
ORDER BY level, employee_id;

-------------------------------------------------------------
-- Query 5: Employee Reporting Path
-------------------------------------------------------------
WITH RECURSIVE reporting_path AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        employee_name::TEXT AS hierarchy
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        rp.hierarchy || ' -> ' || e.employee_name
    FROM employees e
    JOIN reporting_path rp
        ON e.manager_id = rp.employee_id
)
SELECT *
FROM reporting_path;

-------------------------------------------------------------
-- Query 6: Factorial of 10
-------------------------------------------------------------
WITH RECURSIVE factorial AS (
    SELECT
        1 AS n,
        1::BIGINT AS fact

    UNION ALL

    SELECT
        n + 1,
        fact * (n + 1)
    FROM factorial
    WHERE n < 10
)
SELECT *
FROM factorial;

-------------------------------------------------------------
-- Query 7: Fibonacci Series (First 10 Terms)
-------------------------------------------------------------
WITH RECURSIVE fibonacci AS (
    SELECT
        1 AS n,
        0 AS first_num,
        1 AS second_num

    UNION ALL

    SELECT
        n + 1,
        second_num,
        first_num + second_num
    FROM fibonacci
    WHERE n < 10
)
SELECT
    n,
    first_num AS fibonacci_number
FROM fibonacci;

-------------------------------------------------------------
-- Query 8: Generate Multiplication Table of 5
-------------------------------------------------------------
WITH RECURSIVE multiplication AS (
    SELECT
        1 AS n,
        5 AS value

    UNION ALL

    SELECT
        n + 1,
        (n + 1) * 5
    FROM multiplication
    WHERE n < 10
)
SELECT *
FROM multiplication;

-------------------------------------------------------------
-- Query 9: Generate Alphabet Sequence (A-E)
-------------------------------------------------------------
WITH RECURSIVE alphabet AS (
    SELECT
        65 AS ascii_code

    UNION ALL

    SELECT
        ascii_code + 1
    FROM alphabet
    WHERE ascii_code < 69
)
SELECT
    CHR(ascii_code) AS letter
FROM alphabet;

-------------------------------------------------------------
-- Query 10: Department Levels
-------------------------------------------------------------
WITH RECURSIVE department_levels AS (
    SELECT
        department_id,
        department_name,
        1 AS level
    FROM departments

    UNION ALL

    SELECT
        department_id,
        department_name,
        level + 1
    FROM department_levels
    WHERE level < 3
)
SELECT *
FROM department_levels
ORDER BY department_id, level;

-------------------------------------------------------------
-- Query 11: Countdown from 10 to 1
-------------------------------------------------------------
WITH RECURSIVE countdown AS (
    SELECT 10 AS num

    UNION ALL

    SELECT num - 1
    FROM countdown
    WHERE num > 1
)
SELECT *
FROM countdown;

-------------------------------------------------------------
-- Query 12: Sum of Numbers from 1 to 100
-------------------------------------------------------------
WITH RECURSIVE numbers AS (
    SELECT
        1 AS num

    UNION ALL

    SELECT
        num + 1
    FROM numbers
    WHERE num < 100
)
SELECT
    SUM(num) AS total_sum
FROM numbers;

-------------------------------------------------------------
-- Query 13: Powers of Two
-------------------------------------------------------------
WITH RECURSIVE powers AS (
    SELECT
        0 AS exponent,
        1::BIGINT AS value

    UNION ALL

    SELECT
        exponent + 1,
        value * 2
    FROM powers
    WHERE exponent < 10
)
SELECT *
FROM powers;

-------------------------------------------------------------
-- Query 14: Reverse Numbers (10 to 1)
-------------------------------------------------------------
WITH RECURSIVE reverse_numbers AS (
    SELECT 10 AS num

    UNION ALL

    SELECT num - 1
    FROM reverse_numbers
    WHERE num > 1
)
SELECT *
FROM reverse_numbers;

-------------------------------------------------------------
-- Query 15: Generate Months (1-12)
-------------------------------------------------------------
WITH RECURSIVE months AS (
    SELECT 1 AS month_number

    UNION ALL

    SELECT month_number + 1
    FROM months
    WHERE month_number < 12
)
SELECT *
FROM months;