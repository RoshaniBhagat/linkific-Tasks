import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="day8_sql_practice",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
""")

connection.commit()

print("Table Created")

cursor.close()
connection.close()