from ..database.models import BitByteNode
from ..database import db

def getAllNodes():
    nodes = db.session.query(BitByteNode)
    return [node.serialize() for node in nodes]

def getNodeById(node_id):
    node = db.session.query(BitByteNode).filter_by(id=node_id).first()
    return node.serialize()

def postNode(node):
    new_node = BitByteNode(node)
    db.session.add(new_node)
    db.session.commit()
    return new_node.serialize()