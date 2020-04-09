from flask import Flask
from app.config import config_by_name

def create_app(config_name):
    # Setup app development configuration
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Import all API blueprints from their respective files
    from app.api.nodeRouter import node_blueprint

    app.register_blueprint(node_blueprint)
    
    return app