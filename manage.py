from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_seeder import FlaskSeeder

from app import create_app
from app.database import db
from app.database.seeds import seedTables
import os

# Create development app (change dev environments in .env file)
application = create_app(os.environ["ENVIRONMENT"])

# Create all database models
import app.database.models

db.init_app(application)
db.create_all(app=application)

# Set up seeder
seeder = FlaskSeeder()
seeder.init_app(app, db)

# Set up manager and migration functionality
manager = Manager(application)
migrate = Migrate(application, db)

manager.add_command("db", MigrateCommand)

@manager.command
def run():
    application.run(host='0.0.0.0')

@manager.command
def seed():
    seedTables()

if __name__ == "__main__":
    manager.run()

