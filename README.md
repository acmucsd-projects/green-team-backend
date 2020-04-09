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
DB_HOST=db      // name of docker container database service, which is "db" in docker-compose.yml
DB_PORT=5432
DB_DATABASE=green_team_db
DB_USER=green_team_user
DB_PASSWORD=password

SECRET_KEY=my_secret_key
```

### File System Structure:
* `/app` - the main project folder containing everything
* `/app/api` - contains controllers for routes and Flask blueprints
* `/app/models` - contains database models (schemas) and classes to create objects
* `/app/database` - database setup, seeds might go here later
* `/app/services` - contains services that perform necessary logic between API and database
* `/app/__init__.py` - connect Flask blueprints here
* `/app/models/__init__.py` - connect new models here
 


### Notes:

* Saving files will automatically refresh server (no need to close and open containers)
* If you `pip install` any packages, make sure to type `pip freeze > requirements.txt` to save dependencies for Docker to install.
* Data in the database does not persist after closing containers