from flask import request, json, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from ..services import treeService

auth = HTTPBasicAuth()
tree_blueprint = Blueprint('tree_blueprint', __name__, url_prefix="/trees")

@auth.verify_password
def verify_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return None

    if username in users and check_password_hash(user.username, password):
        return username

@tree_blueprint.route("/<tree_id>", methods=["GET"])
def getTree(tree_id):
    nodes = treeService.getTree(tree_id)
    if not nodes:
        return {"error" : "Unable to fetch tree from database"}
    return jsonify(nodes)

@tree_blueprint.route("/points", methods=["POST"])
@auth.login_required
def addPoints():
    body = request.get_json()
    if not body:
        return "Error: No request body provided"
    nodes = treeService.addPointsById(body["id"], body["points"])
    return jsonify(nodes)
