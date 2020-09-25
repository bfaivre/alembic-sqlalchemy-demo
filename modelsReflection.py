from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an engine and session.
engine = create_engine("mysql://root:root@localhost/Demo")
session = Session(engine)

# Modify the names of the relationship collections. 
def _name_for_collection_relationship(base, local_cls, referred_cls, constraint):
    # The default implementation is:
    # return referred_cls.__name__.lower() + "_collection"
    return referred_cls.__name__[:-1] + "ies"

# Do not lower case scalar relationship names. 
def _name_for_scalar_relationship(base, local_cls, referred_cls, constraint):
    # The default implementation is:
    # return referred_cls.__name__.lower()
    return referred_cls.__name__

# You can use the following snippet to view the name of a class that is reflected.
# from sqlalchemy.inspection import inspect
# for item in inspect(Base.classes.<classname>).relationships.items():
#     print(item)

# Reflect the schemas listed below.
automapBase = automap_base()
automapBase.metadata.reflect(engine)
automapBase.prepare(name_for_collection_relationship = _name_for_collection_relationship, name_for_scalar_relationship = _name_for_scalar_relationship)

# Map the classes matching the name of the table.
Fv = automapBase.classes.Fv
Gravity = automapBase.classes.Gravity
