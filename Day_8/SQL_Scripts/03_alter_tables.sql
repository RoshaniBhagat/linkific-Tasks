-- Add a new column to customers
ALTER TABLE customers
ADD COLUMN country VARCHAR(50);

-- Add a new column to products
ALTER TABLE products
ADD COLUMN brand VARCHAR(50);

-- Change the size of city column
ALTER TABLE customers
ALTER COLUMN city TYPE VARCHAR(100);

-- Remove phone column
ALTER TABLE customers
DROP COLUMN phone;