import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/day8_sql_practice"
)

df = pd.read_sql_query(
    "SELECT * FROM students",
    engine
)

print(df)