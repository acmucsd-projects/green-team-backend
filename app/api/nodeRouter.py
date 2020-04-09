from app.api import node_blueprint
from flask import request, json, jsonify

from ..services import nodeService

@node_blueprint.route("/", methods=["GET"])
def getAllNodes():
    nodes = nodeService.getAllNodes()
    return jsonify(nodes)

@node_blueprint.route("/<node_id>", methods=["GET"])
def getNode(node_id):
    node = nodeService.getNodeById(node_id)
    return jsonify(node)

@node_blueprint.route("/", methods=["POST"])
def postNode():
    node = request.get_json()
    if node:
        new_node = nodeService.postNode(node)
        return jsonify(new_node)
    else:
        return "Error: No request body provided"
