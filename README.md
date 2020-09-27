# A simple demo of using Alembic and SQLAlchemy.

## Prerequisites

This demo assumes you have access to a MariaDB or MySQL database. Create an empty database named "Demo" on your server.

## Steps

1. Clone the repository:

```
$ git clone https://github.com/bfaivre/alembic-sqlalchemy-demo
```

2. Change directory into it:

```
$ cd alembic-sqlalchemy-demo
```

3. Create a virtual environment:

```
$ python -m venv venv
```

4. Activate the newly created virtual environment (Windows):

```
$ .\venv\Scripts\activate
```

5. Install pip packages:

```
(venv) $ pip install -r requirements.txt
```

6. Edit .env and set DATABASE, PASSWORD, SERVER and USER variables for your MariaDB/MySQL server. For example: 

```
DATABASE=Demo
PASSWORD=root
SERVER=localhost
USER=root
```

7. Initialize Alembic:

```
(venv) $ alembic init alembic
```

8. Edit alembic.ini and set sqlalchemy.url for your environment. For example mysql://root:root@localhost/Demo for MariaDB/MySQL, username "root", password "root, server "localhost" and database "Demo".

9. Edit env.py in the alembic folder to read our models.py file for generating scripts. Comment out "target_metadata = None" and add the following below:

```
import os
import sys
sys.path.append(os.getcwd())
import models
target_metadata = models.Base.metadata
```

10. Take a look at the models.py file. We have defined a simple table named "Fv". Create the initial database migration script based off of the models.py file:

```
(venv) $ alembic revision --autogenerate -m "Initial migration."
```

10. Run the the initial database migration script to create the "Fv" table:

```
(venv) $ alembic upgrade head
```

11. At this point the database "Demo" should now contain a table for "Fv" and "alembic_version". You'll also notice that a script has been created in folder alembic/versions if you want to inspect/modify the upgrade and/or downgrade commands.

12. Edit models.py and uncomment the following lines to add a new table named "Gravity":

```
    # Gravities = relationship("Gravity", backref = "FV", lazy = "dynamic")

# class Gravity(Base):
#     __tablename__ = "Gravity"
#     GravityId = Column(Integer, primary_key = True)
#     FvId = Column(Integer, ForeignKey("Fv.FvId"), nullable = False) 
#     Gravity = Column(Float, nullable = False)
#     Timestamp = Column(DATETIME(fsp = 6), nullable = False)
```

13. Let's create our next database migration script to add the changes to our database from the modification of the models.py file in the step above:

```
(venv) $ alembic revision --autogenerate -m "Added Gravity table."
```

14. Let's run the alembic upgrade command to update our database with the Gravity table:

```
(venv) $ alembic upgrade head
```

15. Refresh your database and confirm that the Gravity table was added.

16. To downgrade to the previous version of the database (without the Gravity table), run the alembic downgrade command:

```
(venv) $ alembic downgrade -1
```

17. Confirm that the Gravity table was removed.

18. Run the alembic upgrade command one more time to prepare for using the SQLAlchemy demo scripts:

```
(venv) $ alembic upgrade head
```

19. At this point the database "Demo" should now contain a table for "Fv", "Gravity" and "alembic_version". Now you can modify and run demo.py to show some simple examples and demoReflection.py to demonstrate the use of SQLAlchemy if you don't have a models file that you've been maintaining for a database that you'd like to manipulate using SQLAlchemy and Python:

```
(venv) $ python demo.py
(venv) $ python demoReflection.py
```
