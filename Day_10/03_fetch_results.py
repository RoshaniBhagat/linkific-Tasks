import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="day8_sql_practice",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

cursor.execute("""
INSERT INTO students(name,age)
VALUES('Roshani',23)
""")

connection.commit()

print("Record Inserted")

cursor.close()
connection.close()