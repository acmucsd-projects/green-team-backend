from flask import request, json, jsonify, Blueprint

from ..services import nodeService

node_blueprint = Blueprint('node_blueprint', __name__, url_prefix="/nodes")

@node_blueprint.route("/", methods=["GET"])
def getAllNodes():
    nodes = nodeService.getAllNodes()
    return { "error": None, "nodes": nodes }

@node_blueprint.route("/", methods=["POST"])
def postNode():
    node = request.get_json()
    if not node:
        return {"error" : "No request body provided"}
    new_node = nodeService.postNode(node)
    return { "error": None, "node": new_node }

@node_blueprint.route("/<node_id>", methods=["GET"])
def getNode(node_id):
    node = nodeService.getNodeById(node_id)
    if not node:
        return {"error" : "Unable to fetch node from database"}
    return { "error": None, "node": node}

@node_blueprint.route("/<node_id>/children", methods=["GET"])
def getNodeAndChildren(node_id):
    nodes = nodeService.getNodeAndChildren(node_id, levels=1)
    if not nodes:
        return {"error" : "Unable to fetch nodes from database"}
    return { "error": None, "nodes": nodes}

        
