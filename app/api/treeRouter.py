from flask import request, json, jsonify, Blueprint

from ..services import treeService

tree_blueprint = Blueprint('tree_blueprint', __name__, url_prefix="/trees")

@tree_blueprint.route("/<tree_id>", methods=["GET"])
def getTree(tree_id):
    nodes = treeService.getTree(tree_id)
    if not nodes:
        return "Error: Unable to fetch nodes from database"
    return jsonify(nodes)
        
