-- Customers from India
SELECT *
FROM customers
WHERE country='India';

-- Products with stock greater than 20
SELECT *
FROM products
WHERE stock>20;

-- Products between 1000 and 50000
SELECT *
FROM products
WHERE price BETWEEN 1000 AND 50000;

-- Electronics products
SELECT *
FROM products
WHERE category='Electronics';

-- Total products in each category
SELECT category, COUNT(*)
FROM products
GROUP BY category;

-- Number of customers by city
SELECT city, COUNT(*)
FROM customers
GROUP BY city;

-- Top 2 expensive products
SELECT *
FROM products
ORDER BY price DESC
LIMIT 2;

-- Products starting with 'P'
SELECT *
FROM products
WHERE product_name LIKE 'P%';

-- Customers sorted alphabetically
SELECT *
FROM customers
ORDER BY first_name ASC;

-- Orders above ₹30,000
SELECT *
FROM orders
WHERE total_amount > 30000;