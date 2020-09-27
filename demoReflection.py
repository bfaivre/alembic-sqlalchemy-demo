import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelsReflection import Fv, Gravity

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))
engine = create_engine(f'mysql://{os.environ.get("USER")}:{os.environ.get("PASSWORD")}@{os.environ.get("SERVER")}/{os.environ.get("DATABASE")}')
Session = sessionmaker(bind = engine)
session = Session()

# Print 10 most recent gravity readings from FV01.
fv01 = session.query(Fv).filter_by(Name = "FV01").one()
for n, gravity in enumerate(session.query(Gravity).filter_by(FvId = fv01.FvId).order_by(Gravity.Timestamp.desc()), start = 1):
    print(f"#{n} - Timestamp: {gravity.Timestamp}, Gravity: {gravity.Gravity}")
    if n == 10:
        break
