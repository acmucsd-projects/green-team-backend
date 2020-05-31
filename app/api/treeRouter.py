from flask import request, json, jsonify, Blueprint
from ..services.authService import auth
from ..services import treeService
from ..storage.s3 import upload_file
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from ..error.responses import sendError

import uuid
import os

tree_blueprint = Blueprint('tree_blueprint', __name__, url_prefix="/trees")

@tree_blueprint.route("/", methods=["GET"])
def getTreesAsc():
    try:
        trees = treeService.getTreesAsc()
        return { "trees": trees, "error": None }
    except:
        return sendError(500, "An error occurred while retrieving trees")

@tree_blueprint.route("/<tree_id>", methods=["GET"])
def getTree(tree_id):
    try:
        tree = treeService.getTree(tree_id)
        if not tree:
            return sendError(404, "Tree not found in database")
        return { "tree": tree, "error": None }
    except:
        return sendError(500, "An error occurred while retrieving tree")

@tree_blueprint.route("/<tree_id>", methods=["PUT"])
def putTree(tree_id):
    try:
        body = request.get_json()
        if not body:
            return sendError(400, "No request body provided")
        tree = treeService.updateTree()
        return { "tree": tree, "error": None }
    except:
        return sendError(500, "An error occurred while updating tree")

@tree_blueprint.route("/points", methods=["POST"])
@auth.login_required
def addPoints():
    try:
        body = request.get_json()
        if not body or not body.get("id", None) or not body.get("points", None):
            return sendError(400, "Missing id or points in request body")
        tree = treeService.addPointsById(body["id"], body["points"])
        return { "tree": tree, "error": None }
    except:
        return sendError(500, "An error occurred while updating points of tree")

@tree_blueprint.route("/picture", methods=["POST"])
def uploadPicture():
    try:
        file = request.files["image"]
        tree_id = request.form.get("id")
        if not file or not tree_id:
            return sendError(400, "Missing file or id in request body")
        filename = str(uuid.uuid4())
        file.save(os.path.join("/tmp/", filename))
        file_url = upload_file(filename)
        tree = treeService.updateProfileUrl(tree_id, file_url)
        return { "tree": tree, "error": None }
    except RequestEntityTooLarge:
        return sendError(400, "File size too large")
    except:
        return sendError(500, "An error occurred while updating profile picture of tree")
