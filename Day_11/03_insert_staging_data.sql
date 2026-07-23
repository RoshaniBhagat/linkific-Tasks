Customers
INSERT INTO staging_customers VALUES
(1,'Roshani','Bangalore','Karnataka'),
(2,'Amit','Mumbai','Maharashtra'),
(3,'Sara','Delhi','Delhi');

Products
INSERT INTO staging_products VALUES
(101,'Laptop','Electronics',65000),
(102,'Phone','Electronics',25000),
(103,'Keyboard','Accessories',1200);

Stores
INSERT INTO staging_stores VALUES
(1,'Store A','Bangalore'),
(2,'Store B','Mumbai');

Sales
INSERT INTO staging_sales VALUES
(1,1,101,1,2,'2026-07-10'),
(2,2,102,2,1,'2026-07-11'),
(3,3,103,1,4,'2026-07-12');
