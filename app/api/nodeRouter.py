from flask import request, json, jsonify, Blueprint
from ..services.authService import auth
from ..services import nodeService
from ..error.responses import sendError

node_blueprint = Blueprint('node_blueprint', __name__, url_prefix="/nodes")

@node_blueprint.route("/", methods=["GET"])
def getAllNodes():
    try:
        nodes = nodeService.getAllNodes()
        return { "nodes": nodes, "error": None }
    except:
        return sendError(500, "An error occurred while retrieving nodes")
@node_blueprint.route("/", methods=["POST"])
@auth.login_required
def postNode():
    try:
        node = request.get_json()
        if not node:
            return sendError(400, "No request body provided")
        new_node = nodeService.postNode(node)
        return { "node": new_node, "error": None, }
    except:
        return sendError(500, "Error creating new node")

@node_blueprint.route("/<node_id>", methods=["GET"])
def getNode(node_id):
    try:
        node = nodeService.getNodeById(node_id)
        if not node:
            return sendError(404, "Node not found in database")
        return { "node": node, "error": None }
    except:
        return sendError(500, "An error occurred while retrieving node")

@node_blueprint.route("/<node_id>/children", methods=["GET"])
def getNodeAndChildren(node_id):
    try:
        nodes = nodeService.getNodeAndChildren(node_id, levels=1)
        if not nodes:
            return sendError(404, "Nodes not found in database")
        return { "nodes": nodes, "error": None }
    except:
        return sendError(500, "An error occurred while retrieving nodes")