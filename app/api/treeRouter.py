from flask import request, json, jsonify, Blueprint

from ..services import treeService
from ..storage.s3 import upload_file
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

import uuid
import os

tree_blueprint = Blueprint('tree_blueprint', __name__, url_prefix="/trees")

@tree_blueprint.route("/", methods=["GET"])
def getTreesAsc():
    try:
        trees = treeService.getTreesAsc()
        return { "error": None, "trees": trees }
    except:
        return { "error": "Error fetching trees" }

@tree_blueprint.route("/<tree_id>", methods=["GET"])
def getTree(tree_id):
    try:
        tree = treeService.getTree(tree_id)
        if not tree:
            return {"error" : "Unable to fetch tree from database"}
        return { "error": None, "tree": tree }
    except:
        return { "error": "Error fetching tree" }

@tree_blueprint.route("/<tree_id>", methods=["PUT"])
def putTree(tree_id):
    try:
        body = request.get_json()
        if not body:
            return {"error" : "No request body provided"}
        tree = treeService.updateTree()
        return { "error": None, "tree": tree }
    except:
        return { "error": "Error updating tree" }

@tree_blueprint.route("/points", methods=["POST"])
def addPoints():
    try:
        body = request.get_json()
        if not body:
            return { "error" : "No request body provided" }
        tree = treeService.addPointsById(body["id"], body["points"])
        return { "error": None, "tree": tree }
    except:
        return { "error": "Error updating tree's points" }

@tree_blueprint.route("/picture", methods=["POST"])
def uploadPicture():
    try:
        file = request.files["image"]
        tree_id = request.form.get("id")
        if not file:
            return { "error" : "No file provided" }
        filename = str(uuid.uuid4())
        file.save(os.path.join("/tmp/", filename))
        file_url = upload_file(filename)
        tree = treeService.updateProfileUrl(tree_id, file_url)
        return { "message" : "File uploaded successfully", "tree": tree }
    except RequestEntityTooLarge:
        return { "error": "File size too large"}
    except:
        return { "error": "Error uploading file" }
