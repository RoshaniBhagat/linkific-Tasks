import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="day8_sql_practice",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

name="Amit"
age=25

cursor.execute(
    "INSERT INTO students(name,age) VALUES(%s,%s)",
    (name,age)
)

connection.commit()

print("Inserted")

cursor.close()
connection.close()