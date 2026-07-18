Customers
   │
   ├── customer_id (PK)
   │
   ▼
Orders
   │
   ├── order_id (PK)
   ├── customer_id (FK)
   │
   ▼
Order_Items
   │
   ├── order_item_id (PK)
   ├── order_id (FK)
   ├── product_id (FK)
   │
   ▼
Products
   ├── product_id (PK)