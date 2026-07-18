-- Index on customer city
CREATE INDEX idx_customer_city
ON customers(city);

-- Index on product category
CREATE INDEX idx_product_category
ON products(category);