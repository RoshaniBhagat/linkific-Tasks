-- Update customer's city
UPDATE customers
SET city = 'Mangalore'
WHERE customer_id = 1;

-- Update product stock
UPDATE products
SET stock = 50
WHERE product_name = 'Mouse';

-- Update laptop price
UPDATE products
SET price = 70000
WHERE product_name = 'Laptop';

-- Update customer country
UPDATE customers
SET country = 'India'
WHERE customer_id = 2;

-- Update order amount
UPDATE orders
SET total_amount = 71200
WHERE order_id = 1;