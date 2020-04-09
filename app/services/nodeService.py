from ..models import Node
from ..database import db

def getAllNodes():
    nodes = db.session.query(Node)
    return [node.serialize() for node in nodes]


def getNodeById(node_id):
    node = db.session.query(Node).filter_by(id=node_id).first()
    return node.serialize()

def postNode(node):
    new_node = Node(node["value"], node["children"])
    db.session.add(new_node)
    db.session.commit()
    return new_node.serialize()