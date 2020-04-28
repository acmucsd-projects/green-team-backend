from ..database.models import BitByteNode
from ..database.models import BitByteTree
from ..database.models import Connection
from ..database import db

def getAllNodes():
    nodes = db.session.query(BitByteNode)
    return [node.serialize() for node in nodes]

def getNodeById(node_id):
    node = db.session.query(BitByteNode).filter_by(id=node_id).first()
    return node.serialize()

def postNode(node):  
    parent_id = node.get("parent_id", None)
    tree_id = db.session.query(BitByteTree.id).filter_by(name=node["tree_name"]).first()
    
    new_node = BitByteNode(node)
    db.session.add(new_node)
    db.session.flush()              # to access new_node.id

    # create new Tree if doesnt exist, otherwise add to that tree
    if not tree_id:
        new_tree = BitByteTree(node["tree_name"], new_node.id)
        db.session.add(new_tree)
    
    # create new Connection if Bit/Byte has parent
    if parent_id:
        new_connection = Connection(new_node.id, parent_id)
        db.session.add(new_connection)

    db.session.commit()    
   
    return new_node.serialize()