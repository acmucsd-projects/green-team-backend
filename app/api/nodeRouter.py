from flask import request, json, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from ..database.models import User
from ..database import db
from ..services import nodeService

auth = HTTPBasicAuth()
node_blueprint = Blueprint('node_blueprint', __name__, url_prefix="/nodes")

@auth.verify_password
def verify_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return None

    if username in users and check_password_hash(user.username, password):
        return username

@node_blueprint.route("/", methods=["GET"])
def getAllNodes():
    nodes = nodeService.getAllNodes()
    return jsonify(nodes)

@node_blueprint.route("/", methods=["POST"])
@auth.login_required
def postNode():
    node = request.get_json()
    if not node:
        return {"error" : "No request body provided"}
    new_node = nodeService.postNode(node)
    return jsonify(new_node)

@node_blueprint.route("/<node_id>", methods=["GET"])
def getNode(node_id):
    node = nodeService.getNodeById(node_id)
    if not node:
        return {"error" : "Unable to fetch node from database"}
    return jsonify(node)

@node_blueprint.route("/<node_id>/children", methods=["GET"])
def getNodeAndChildren(node_id):
    nodes = nodeService.getNodeAndChildren(node_id, levels=1)
    if not nodes:
        return {"error" : "Unable to fetch nodes from database"}
    return jsonify(nodes)
