Backend API for Green Team ACM Side Projects

### Required Dependencies:

1. Python 3 & pip: [Link]
(https://www.python.org/downloads/)
2. Docker:
    * Mac/Linux/Windows 10 Pro: [Link](https://docs.docker.com/get-docker/)
    * Windows 10 Home: I recommend getting WSL 2, its basically a Linux distro on Windows and reduces the number of hiccups/setup issues you'll have when programming. [Get WSL 2 and Docker here](https://code.visualstudio.com/blogs/2020/03/02/docker-in-wsl2)
3. docker-compose: To spin up server + database easily. [Installation Instructions](https://docs.docker.com/compose/install/)

### Build Instructions:

1. Clone repository to local machine: `git clone https://github.com/acmucsd/green-team-backend.git`
2. Navigate to project directory `cd green-team-backend`
3. Create Python virtual environment so pip installs aren't global. [Explanation + Installation guide](https://docs.python.org/3/tutorial/venv.html)
4. Create a `.env` file to be able to connect to the database.
    * Do `cp .env.example .env` to rename the example file
    * Copy the `.env` configuration from below
5. Run `docker-compose up -d --build` to spin up server and PostgreSQL database containers
6. Run `docker-compose down` to shut down containers

#### Example .env file

```
DB_HOST=db
DB_PORT=5432
DB_DATABASE=green_team_db
DB_USER=green_team_user
DB_PASSWORD=password

SECRET_KEY=my_secret_key
ENVIRONMENT=development

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=

```

### File System Structure:
* `/app` - the main project folder containing everything
* `/app/api` - contains controllers for routes and Flask blueprints
* `/app/database` - database setup and models, seeds may come here later
* `/app/database/models` - create and export new models here
* `/app/services` - contains services that perform necessary logic between API and database
* `/app/__init__.py` - connect Flask blueprints here
 
### Migrating Database Tables

To write migrations to update the development/staging/production tables, follow these steps:

1. Add all necessary model updates to the Model classes
2. If using Docker, enter the container's shell by typing `docker exec -it <CONTAINER_ID> bash`. Skip this step if not using Docker
3. `python manage.py db migrate -m "<migration changes>"` - this creates a new migration with the schema changes that have not yet been added in the tables by comparing those schemas to the ones in the `app/database/models`.
4. `python manage.py db upgrade` to run the migrations locally. 

### Seeding Database Tables

To seed the development database tables with initial data, follow these steps (skip to step 4 if not running on the docker containers):

1. `docker-compose up -d --build` to start the local database and app
2. `docker ps` to view the CONTAINER ID of the backend app (not the database). Copy the CONTAINER ID of that container.
3. `docker exec -it <CONTAINER_ID> bash` to open the bash shell of the container
4. `python manage.py seed` to seed the tables

### Notes:

* Saving files will automatically refresh server (no need to close and open containers)
* If you `pip install` any packages, make sure to type `pip freeze > requirements.txt` to save dependencies for Docker to install.
* Data in the database persists after stopping containers (`docker-compose stop`)
