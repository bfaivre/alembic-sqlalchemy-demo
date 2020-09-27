import os
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Fv, Gravity

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))
engine = create_engine(f'mysql://{os.environ.get("USER")}:{os.environ.get("PASSWORD")}@{os.environ.get("SERVER")}/{os.environ.get("DATABASE")}')
connection = engine.connect()

Session = sessionmaker(bind = engine)
session = Session()

################################################################################
# Uncomment the following block to create FV01 - FV09 in the Fv table.
################################################################################
# for n in range(1, 10):
#     fv = Fv(Name = f"FV0{n}")
#     print(f"Adding FV0{n}.")
#     session.add(fv)

# session.commit()

################################################################################
# Uncomment the following block to add 100 random gravity readings per FV.
################################################################################
# for fv in session.query(Fv).all():
#     for n in range (0, 101):
#         gravityReading = random.randint(10, 17)
#         gravity = Gravity(FvId = fv.FvId, Gravity = gravityReading, Timestamp = datetime.now() - relativedelta(days = n))
#         session.add(gravity)

# session.commit()

################################################################################
# Uncomment the following block to print all the gravities for FV01 in order.
################################################################################
# fv01 = session.query(Fv).filter_by(Name = "FV01").one()
# for gravity in fv01.Gravities.order_by(Gravity.Timestamp.desc()).all():
#     print(f"Timestamp: {gravity.Timestamp}, Gravity: {gravity.Gravity}")

################################################################################
# Uncomment the following block to print the SQL that is created for you.
################################################################################
# print(session.query(Fv))
# print("--------------------------------------------------------------------------------")
# print(session.query(Fv).filter_by(Name = "FV01"))
