from flask import Flask
from app.config import config_by_name

def create_app(config_name):
    # Setup app development configuration
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Import all API blueprints from the __init__.py file
    import app.api

    app.register_blueprint(app.api.node_blueprint)
    app.register_blueprint(app.api.tree_blueprint)
    
    return app