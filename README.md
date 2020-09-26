A simple demo of using Alembic and SQLAlchemy. Create an empty database named "Demo" in your environment.

1. Clone the repository:

`$ git clone https://github.com/bfaivre/alembic-sqlalchemy-demo`

2. Change directory into it:

`$ cd alembic-sqlalchemy-demo`

3. Create a virtual environment:

`$ python -m venv venv`

4. Activate the newly created virtual environment (Windows):

`$ .\venv\Scripts\Activate`

5. Install pip packages:

`(venv) $ pip install -r requirements.txt`

6. Initialize Alembic:

`(venv) $ alembic init alembic`

7. Edit alembic.ini and set sqlalchemy.url for your environment. For example mysql://root:root@localhost/Demo for MariaDB/MySQL, username "root", password "root, server "localhost" and database "Demo".

8. Edit env.py in the alembic folder. Comment out "target_metadata = None" and add the following below:

```import os
import sys
sys.path.append(os.getcwd())
import models
target_metadata = models.Base.metadata
```

9. Create the initial database migration script:

`(venv) $ alembic revision --autogenerate -m "Initial migration.".`

10. Run the the initial database migration script to create the tables:

`(venv) $ alembic upgrade head`

11. Add this point the database "Demo" should now contain a table for "Fv", "Gravity" and "alembic_version" and can modify and run demo.py and demoReflection.py as simple examples:

`(venv) $ python demo.py`
`(venv) $ python demoReflection.py`
