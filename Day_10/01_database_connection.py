import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="day8_sql_practice",
        user="postgres",
        password="1234",
        port="5432"
    )

    print("Connected Successfully!")

    connection.close()

except Exception as e:
    print("Connection Failed")
    print(e)