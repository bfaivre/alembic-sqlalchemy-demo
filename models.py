from sqlalchemy import Column, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Fv(Base):
    __tablename__ = "Fv"
    __table_args__ = \
    (
		UniqueConstraint("Name", name = "AK__Name"),
    )

    FvId = Column(Integer, primary_key = True)
    Name = Column(String(45), nullable = False)
    Volume = Column(Integer, nullable = True)

    Gravities = relationship("Gravity", backref = "FV", lazy = "dynamic")

class Gravity(Base):
    __tablename__ = "Gravity"
    GravityId = Column(Integer, primary_key = True)
    FvId = Column(Integer, ForeignKey("Fv.FvId"), nullable = False) 
    Gravity = Column(Float, nullable = False)
    Timestamp = Column(DATETIME(fsp = 6), nullable = False)
