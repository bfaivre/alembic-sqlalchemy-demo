from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelsReflection import Fv, Gravity

engine = create_engine("mysql://root:root@localhost/Demo")
Session = sessionmaker(bind = engine)
session = Session()

# Print 10 most recent gravity readings from FV01.
fv01 = session.query(Fv).filter_by(Name = "FV01").one()
for n, gravity in enumerate(session.query(Gravity).filter_by(FvId = fv01.FvId).order_by(Gravity.Timestamp.desc()), start = 1):
    print(f"#{n} - Timestamp: {gravity.Timestamp}, Gravity: {gravity.Gravity}")
    if n == 10:
        break
