-- Total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Total products
SELECT COUNT(*) AS total_products
FROM products;

-- Average product price
SELECT AVG(price) AS average_price
FROM products;

-- Total stock
SELECT SUM(stock) AS total_stock
FROM products;

-- Highest price
SELECT MAX(price) AS highest_price
FROM products;

-- Lowest price
SELECT MIN(price) AS lowest_price
FROM products;

-- Number of products in each category
SELECT category, COUNT(*) AS total_products
FROM products
GROUP BY category;

-- Average price by category
SELECT category, AVG(price) AS average_price
FROM products
GROUP BY category;