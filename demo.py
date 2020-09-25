from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Fv

engine = create_engine("mysql://root:root@localhost/Demo")
connection = engine.connect()
connection.execute(f"CREATE DATABASE IF NOT EXISTS Demo")

Session = sessionmaker(bind = engine)
session = Session()

for n in range(1, 10):
    fv = Fv(Name = f"FV0{n}")
    print(f"Adding FV0{n}.")
    session.add(fv)

session.commit()
