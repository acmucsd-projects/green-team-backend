from flask import request, json, jsonify, Blueprint

from ..services import treeService
from ..storage.s3 import upload_file

tree_blueprint = Blueprint('tree_blueprint', __name__, url_prefix="/trees")

@tree_blueprint.route("/<tree_id>", methods=["GET"])
def getTree(tree_id):
    nodes = treeService.getTree(tree_id)
    if not nodes:
        return {"error" : "Unable to fetch tree from database"}
    return jsonify(nodes)

@tree_blueprint.route("/points", methods=["POST"])
def addPoints():
    body = request.get_json()
    if not body:
        return "Error: No request body provided"
    nodes = treeService.addPointsById(body["id"], body["points"])
    return jsonify(nodes)

@tree_blueprint.route("/picture", methods=["POST"])
def uploadPicture():
    file = request.get_json()
    if not file:
        return "Error: No file provided"
    file_url = upload_file(file) 

