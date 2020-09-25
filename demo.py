import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Fv, Gravity

engine = create_engine("mysql://root:root@localhost/Demo")
connection = engine.connect()
connection.execute(f"CREATE DATABASE IF NOT EXISTS Demo")

Session = sessionmaker(bind = engine)
session = Session()

# for n in range(1, 10):
#     fv = Fv(Name = f"FV0{n}")
#     print(f"Adding FV0{n}.")
#     session.add(fv)

# session.commit()

# for fv in session.query(Fv).all():
#     for n in range (0, 101):
#         gravityReading = random.randint(10, 17)
#         gravity = Gravity(FvId = fv.FvId, Gravity = gravityReading, Timestamp = datetime.now() - relativedelta(days = n))
#         session.add(gravity)

# session.commit()

# fv01 = session.query(Fv).filter_by(Name = "FV01").one()
# for gravity in fv01.Gravities.order_by(Gravity.Timestamp.desc()).all():
#     print(f"Timestamp: {gravity.Timestamp}, Gravity: {gravity.Gravity}")

print(session.query(Fv))
print("--------------------------------------------------------------------------------")
print(session.query(Fv).filter_by(Name = "FV01"))
