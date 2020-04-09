from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.models import db

# Create development app (can change to "prod" for production)
application = create_app("dev")

# Create all database models
import app.models
db.init_app(application)
db.create_all(app=application)

# Set up manager and migration functionality
manager = Manager(application)
migrate = Migrate(application, db)

manager.add_command("db", MigrateCommand)

@manager.command
def run():
    application.run(host='0.0.0.0')

if __name__ == "__main__":
    manager.run()

