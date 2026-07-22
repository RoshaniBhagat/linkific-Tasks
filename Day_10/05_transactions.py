import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="day8_sql_practice",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

try:

    cursor.execute("""
    INSERT INTO students(name,age)
    VALUES('John',20)
    """)

    connection.commit()

    print("Committed")

except:

    connection.rollback()

    print("Rolled Back")

finally:

    cursor.close()
    connection.close()