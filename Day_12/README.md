# 🚀 Day 12 - ETL Pipeline Design & Implementation

## 📌 Overview

This project demonstrates an **ETL (Extract, Transform, Load) pipeline** built using **Python, Pandas, and PostgreSQL**. It extracts data from multiple sources, transforms and cleans the data, and loads it into a PostgreSQL data warehouse. The project also includes incremental loading, logging, and CSV export.

---

## 🛠️ Technologies Used

* Python
* Pandas
* PostgreSQL
* SQL
* psycopg2
* Requests

---

## 🏗️ Project Architecture

```text
                    +----------------------+
                    |      CSV Files       |
                    | Customers, Orders,  |
                    | Products            |
                    +----------+-----------+
                               |
                               |
                    +----------v-----------+
                    |   API Extraction     |
                    +----------+-----------+
                               |
                               |
                    +----------v-----------+
                    |   Database Source    |
                    +----------+-----------+
                               |
                               |
                 +-------------v-------------+
                 |       Extraction Layer    |
                 +-------------+-------------+
                               |
                               |
                 +-------------v-------------+
                 |    Transformation Layer   |
                 | - Data Cleaning           |
                 | - Data Validation         |
                 | - Data Merging            |
                 | - Business Calculations   |
                 +-------------+-------------+
                               |
                               |
                 +-------------v-------------+
                 |       Loading Layer       |
                 | PostgreSQL Data Warehouse |
                 +-------------+-------------+
                               |
                +--------------+--------------+
                |                             |
                |                             |
       +--------v--------+          +---------v---------+
       | final_dataset.csv|          |     etl.log      |
       +------------------+          +------------------+
```

---

## 📂 Project Structure

```text
Day_12_ETL_Pipeline/
│
├── datasets/
├── database/
├── extraction/
├── transformation/
├── loading/
├── utils/
├── logs/
├── output/
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Workflow

```text
CSV / API / Database
         │
         ▼
     Extract
         │
         ▼
Clean & Transform
         │
         ▼
 Merge Datasets
         │
         ▼
Calculate Total Amount
         │
         ▼
Load to PostgreSQL
         │
         ▼
Incremental Load
         │
         ▼
 Export CSV & Logs
```

---

## ✨ Features

* Extract data from CSV, API, and PostgreSQL
* Clean and transform datasets
* Merge multiple data sources
* Load data into PostgreSQL
* Incremental loading
* Export final dataset to CSV
* Logging and exception handling
* Modular ETL architecture

---

## ▶️ How to Run

1. Create the database.

```sql
CREATE DATABASE etl_project;
```

2. Execute SQL scripts.

```bash
\i database/create_tables.sql
\i database/warehouse.sql
```

3. Update database credentials in `utils/config.py`.

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Run the ETL pipeline.

```bash
python pipeline.py
```

---

## 📤 Output

* `output/final_dataset.csv`
* `logs/etl.log`
* PostgreSQL `sales_warehouse` table

---

## 📚 Skills Demonstrated

* ETL Pipeline Development
* Data Extraction
* Data Cleaning
* Data Transformation
* Data Warehousing
* PostgreSQL Integration
* Incremental Loading
* Python & Pandas

---


