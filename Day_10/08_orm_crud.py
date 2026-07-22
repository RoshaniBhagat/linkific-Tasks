from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/day8_sql_practice"
)

Base = declarative_base()

class Employee(Base):
    __tablename__="employee"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

Session=sessionmaker(bind=engine)
session=Session()

employee=Employee(name="Alice",age=30)

session.add(employee)
session.commit()

employees=session.query(Employee).all()

for emp in employees:
    print(emp.id,emp.name,emp.age)