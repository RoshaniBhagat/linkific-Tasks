## Objective

Learn how to connect Python with PostgreSQL, execute SQL queries, use SQLAlchemy, and build simple ETL pipelines.

## Topics Covered

* PostgreSQL connection using `psycopg2`
* Execute SQL queries
* Fetch records
* Parameterized queries
* Transaction management
* Pandas with SQL
* SQLAlchemy ORM
* CRUD operations
* CSV to PostgreSQL
* API to PostgreSQL
* Database analysis
* Incremental loading

## Project Structure

```text
Day_10/
│
├── Database_Connection/
├── Pandas_SQL/
├── SQLAlchemy/
├── ETL_Pipeline/
├── datasets/
├── requirements.txt
└── README.md
```

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## Database

* Database: `day8_sql_practice`
* Host: `localhost`
* Port: `5432`

Update your PostgreSQL username and password in the Python scripts before running them.

## Run the Scripts

```bash
python Database_Connection/01_connect_postgres.py
python Pandas_SQL/01_read_sql_query.py
python SQLAlchemy/01_create_engine.py
python ETL_Pipeline/01_csv_to_postgres.py
```

Run the remaining scripts in the same way.

## Technologies Used

* Python
* PostgreSQL
* pgAdmin 4
* psycopg2
* SQLAlchemy
* Pandas
* Requests
* VS Code


