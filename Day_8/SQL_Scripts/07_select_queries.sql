-- Display all customers
SELECT * FROM customers;

-- Display all products
SELECT * FROM products;

-- Display all orders
SELECT * FROM orders;

-- Display all order items
SELECT * FROM order_items;

-- Show customer names and emails
SELECT first_name, email
FROM customers;

-- Products costing more than 1000
SELECT *
FROM products
WHERE price > 1000;

-- Customers from Sirsi
SELECT *
FROM customers
WHERE city = 'Sirsi';

-- Products sorted by price
SELECT *
FROM products
ORDER BY price DESC;

-- Show only first 2 products
SELECT *
FROM products
LIMIT 2;