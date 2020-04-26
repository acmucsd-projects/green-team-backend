from flask import request, json, jsonify, Blueprint

from ..services import nodeService

node_blueprint = Blueprint('node_blueprint', __name__, url_prefix="/nodes")

@node_blueprint.route("/", methods=["GET"])
def getAllNodes():
    nodes = nodeService.getAllNodes()
    return jsonify(nodes)

@node_blueprint.route("/", methods=["POST"])
def postNode():
    node = request.get_json()
    if not node:
        return "Error: No request body provided"
    new_node = nodeService.postNode(node)
    return jsonify(new_node)

@node_blueprint.route("/<node_id>", methods=["GET"])
def getNode(node_id):
    node = nodeService.getNodeById(node_id)
    return jsonify(node)

@node_blueprint.route("/points", methods=["POST"])
def addPoints():
    body = request.get_json()
    if not body:
        return "Error: No request body provided"
    node = nodeService.addPointsById(body["id"], body["points"])
    return jsonify(node)
