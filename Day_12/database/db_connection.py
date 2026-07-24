import psycopg2


def get_connection():
    """
    Create and return a PostgreSQL database connection.
    """

    connection = psycopg2.connect(
        host="localhost",
        database="etl_project",
        user="postgres",
        password="1234",
        port="5432"
    )

    return connection