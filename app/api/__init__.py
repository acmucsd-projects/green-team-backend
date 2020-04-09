from flask import Blueprint

# Define API blueprints here
node_blueprint = Blueprint('node_blueprint', __name__, url_prefix="/nodes")