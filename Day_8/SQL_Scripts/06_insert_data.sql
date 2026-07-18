INSERT INTO customers
(first_name, last_name, email, city, country)
VALUES
('Roshani','Bhagat','roshani@gmail.com','Sirsi','India'),
('Rahul','Patil','rahul@gmail.com','Bangalore','India'),
('Sneha','Sharma','sneha@gmail.com','Mumbai','India');

INSERT INTO products
(product_name, category, price, stock, brand)
VALUES
('Laptop','Electronics',65000,10,'Dell'),
('Phone','Electronics',30000,25,'Samsung'),
('Keyboard','Accessories',1200,100,'Logitech'),
('Mouse','Accessories',700,80,'HP');

INSERT INTO orders
(customer_id, order_date, total_amount)
VALUES
(1,'2026-07-18',66200),
(2,'2026-07-18',30700);

INSERT INTO order_items
(order_id, product_id, quantity)
VALUES
(1,1,1),
(1,3,1),
(2,2,1),
(2,4,1);