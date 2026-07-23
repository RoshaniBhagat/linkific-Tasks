# Day 11 - Data Warehousing & Dimensional Modeling

## Overview

This project demonstrates the fundamentals of Data Warehousing by designing and implementing a Sales Data Warehouse using PostgreSQL. It covers dimensional modeling, star schema design, Slowly Changing Dimensions (SCD), and analytical reporting.

---

## Learning Objectives

* Understand Data Warehousing concepts
* Learn Dimensional Modeling
* Design Star and Snowflake Schemas
* Implement Slowly Changing Dimensions (SCD)
* Build a Sales Data Warehouse
* Perform analytical queries on warehouse data
---

## Data Warehouse Architecture

```
Source Data
      │
      ▼
Staging Tables
      │
      ▼
Dimension Tables
      │
      ▼
Fact Table
      │
      ▼
Business Analytics
```

---

## Data Model

### Dimension Tables

* dim_customer
* dim_product
* dim_store
* dim_date

### Fact Table

* fact_sales

---

## Topics Covered

### Data Warehouse Concepts

* OLTP vs OLAP
* Data Warehouse vs Database
* Data Mart
* Data Warehouse Architecture

### Dimensional Modeling

* Fact Tables
* Dimension Tables
* Star Schema
* Snowflake Schema
* Galaxy Schema

### Design Concepts

* Fact Table Grain
* Measures
* Primary & Foreign Keys
* Surrogate Keys
* Natural Keys
* Conformed Dimensions

### Slowly Changing Dimensions

* Type 1 (Overwrite)
* Type 2 (History Tracking)
* Type 3 (Previous Value)

---

## Implementation Steps

1. Create the database.
2. Create staging tables.
3. Load sample source data.
4. Create dimension tables.
5. Create the fact table.
6. Load dimensions from staging.
7. Load fact data.
8. Implement SCD Type 1.
9. Implement SCD Type 2.
10. Execute analytical SQL queries.

---

## Sample Analytical Queries

* Total Sales
* Sales by Product
* Sales by Customer
* Sales by Store
* Monthly Sales Analysis

---

## Technologies Used

* PostgreSQL
* SQL
* pgAdmin
* VS Code

---

## Key Concepts Learned

* Data Warehouse Design
* Dimensional Modeling
* ETL Loading
* Star Schema
* Snowflake Schema
* Fact & Dimension Tables
* Surrogate Keys
* Slowly Changing Dimensions
* OLAP Reporting

---


