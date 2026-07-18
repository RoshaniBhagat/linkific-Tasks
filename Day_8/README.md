# Day 8 - SQL & PostgreSQL Practice

## Overview

This project is part of my **Data Engineering Learning Journey**. It focuses on learning PostgreSQL and SQL fundamentals by creating a sample E-commerce database and performing various SQL operations.

---

#  Learning Objectives

- Install and configure PostgreSQL
- Understand relational database concepts
- Create databases and tables
- Apply constraints and indexes
- Perform CRUD operations
- Write aggregate and complex SQL queries
- Learn database design fundamentals
- Practice SQL for Data Engineering

---

#  Technologies Used

- PostgreSQL 17
- pgAdmin 4
- Visual Studio Code
- SQL


#  Database Used

**Database Name**

```
day8_sql_practice
```

---

#  SQL Topics Covered

## 1. Database Creation

- CREATE DATABASE

---

## 2. Table Creation

- CREATE TABLE
- Primary Key
- Foreign Key
- Data Types

---

## 3. Table Modification

- ALTER TABLE
- ADD COLUMN
- DROP COLUMN
- ALTER COLUMN

---

## 4. Constraints

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK

---

## 5. Indexes

- CREATE INDEX
- Query Optimization

---

## 6. CRUD Operations

### Create

- INSERT INTO

### Read

- SELECT
- WHERE
- ORDER BY
- LIMIT

### Update

- UPDATE

### Delete

- DELETE

---

## 7. Aggregate Functions

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()
- GROUP BY

---

## 8. Complex SQL

- INNER JOIN
- Multiple Table JOIN
- Subqueries
- DISTINCT

---

# 🗃 Database Schema

The project uses a simple E-commerce database.

### Tables

### Customers

| Column | Type |
|---------|------|
| customer_id | SERIAL |
| first_name | VARCHAR |
| last_name | VARCHAR |
| email | VARCHAR |
| city | VARCHAR |
| country | VARCHAR |

---

### Products

| Column | Type |
|---------|------|
| product_id | SERIAL |
| product_name | VARCHAR |
| category | VARCHAR |
| price | DECIMAL |
| stock | INTEGER |
| brand | VARCHAR |

---

### Orders

| Column | Type |
|---------|------|
| order_id | SERIAL |
| customer_id | INTEGER |
| order_date | DATE |
| total_amount | DECIMAL |

---

### Order Items

| Column | Type |
|---------|------|
| order_item_id | SERIAL |
| order_id | INTEGER |
| product_id | INTEGER |
| quantity | INTEGER |

---

# ▶️ How to Run

## Step 1

Install PostgreSQL and pgAdmin.

---

## Step 2

Create a database.

```sql
CREATE DATABASE day8_sql_practice;
```

---

## Step 3

Open Query Tool.

---

## Step 4

Execute SQL scripts in the following order.

```
01_create_database.sql
02_create_tables.sql
03_alter_tables.sql
04_constraints.sql
05_indexes.sql
06_insert_data.sql
07_select_queries.sql
08_update_queries.sql
09_delete_queries.sql
10_aggregate_queries.sql
11_complex_queries.sql
12_practice_queries.sql
```

> **Note:** `13_drop_tables.sql` is only for cleanup and should not be executed unless you want to remove all tables.

---

# 📖 Concepts Learned

- Relational Databases
- Database Design
- SQL Syntax
- Table Relationships
- Constraints
- Indexes
- CRUD Operations
- Aggregate Functions
- SQL Joins
- Query Optimization

---

