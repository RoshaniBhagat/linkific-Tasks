-- Query 1: Display Employee and Manager
-------------------------------------------------------------
SELECT
    e.employee_id,
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id
ORDER BY e.employee_id;

-------------------------------------------------------------
-- Query 2: Employee, Manager and Employee Salary
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager,
    e.salary
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id
ORDER BY e.salary DESC;

-------------------------------------------------------------
-- Query 3: Employee, Manager and Department
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager,
    d.department_name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY d.department_name;

-------------------------------------------------------------
-- Query 4: Employees Who Have a Manager
-------------------------------------------------------------
SELECT
    e.employee_name,
    m.employee_name AS manager
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id
ORDER BY manager;

-------------------------------------------------------------
-- Query 5: Employees Without a Manager
-------------------------------------------------------------
SELECT
    employee_name,
    salary
FROM employees
WHERE manager_id IS NULL;

-------------------------------------------------------------
-- Query 6: Managers and Number of Employees Reporting
-------------------------------------------------------------
SELECT
    m.employee_name AS manager,
    COUNT(e.employee_id) AS total_employees
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id
GROUP BY m.employee_name
ORDER BY total_employees DESC;

-------------------------------------------------------------
-- Query 7: Employees Earning More Than Their Manager
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    e.salary AS employee_salary,
    m.employee_name AS manager,
    m.salary AS manager_salary
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;

-------------------------------------------------------------
-- Query 8: Employees Earning Less Than Their Manager
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    e.salary AS employee_salary,
    m.employee_name AS manager,
    m.salary AS manager_salary
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id
WHERE e.salary < m.salary;

-------------------------------------------------------------
-- Query 9: Display Employee Hierarchy
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    COALESCE(m.employee_name, 'No Manager') AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id
ORDER BY employee;

-------------------------------------------------------------
-- Query 10: Manager with Department Name
-------------------------------------------------------------
SELECT
    e.employee_name AS employee,
    COALESCE(m.employee_name, 'No Manager') AS manager,
    d.department_name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY d.department_name, employee;

-------------------------------------------------------------
-- Query 11: Number of Managers
-------------------------------------------------------------
SELECT
    COUNT(DISTINCT manager_id) AS total_managers
FROM employees
WHERE manager_id IS NOT NULL;

-------------------------------------------------------------
-- Query 12: Employees Reporting to John
-------------------------------------------------------------
SELECT
    e.employee_name
FROM employees e
INNER JOIN employees m
ON e.manager_id = m.employee_id
WHERE m.employee_name = 'John';