-- Product price must be greater than 0
ALTER TABLE products
ADD CONSTRAINT chk_price
CHECK (price > 0);

-- Stock cannot be negative
ALTER TABLE products
ADD CONSTRAINT chk_stock
CHECK (stock >= 0);