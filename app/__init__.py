from flask import Flask
from app.config import config_by_name

def create_app(config_name):
    # Setup app development configuration
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Disable strict slashes.
    # See here for more info: https://github.com/pallets/flask/issues/1783
    app.url_map.strict_slashes = False

    # Import all API blueprints from the __init__.py file
    import app.api as api

    app.register_blueprint(api.node_blueprint)
    app.register_blueprint(api.tree_blueprint)

    return app
