from ..database.models import BitByteNode
from ..database.models import BitByteTree
from ..database.models import ParentChildConnection
from ..database import db

from sqlalchemy import literal

def getAllNodes():
    nodes = db.session.query(BitByteNode)
    return [node.serialize() for node in nodes]

def getNodeById(node_id):
    node = db.session.query(BitByteNode, ParentChildConnection.parent_node_id)\
        .outerjoin(ParentChildConnection, ParentChildConnection.node_id == BitByteNode.id)\
        .filter(BitByteNode.id == node_id).first()
    
    if not node:
        return None

    # returns: {'BitByteNode': <BitByteNode object>, 'parent_node_id': int}
    # need to flatten to proper dict
    node = node._asdict()
    node.update(node.pop("BitByteNode").serialize())
    node["level"] = 0
    
    return node

def getNodeAndChildren(node_id, **kwargs):
    levels = kwargs.get('levels', None)

    root_node = getNodeById(node_id)

    if not root_node:
        return None
    
    parent = db.session.query(ParentChildConnection, BitByteNode, literal(1).label('level'))\
        .join(BitByteNode, ParentChildConnection.node_id == BitByteNode.id)\
        .filter(ParentChildConnection.parent_node_id == node_id).cte(name='parent_for', recursive=True)

    children = parent.union_all(
        db.session.query(ParentChildConnection, BitByteNode, (parent.c.level + 1).label('level'))\
            .join(BitByteNode, ParentChildConnection.node_id == BitByteNode.id)\
            .filter(ParentChildConnection.parent_node_id == parent.c.node_id)
    )

    if levels:
        children_nodes = db.session.query(children).filter(children.c.level <= levels).all()
    else:
        children_nodes = db.session.query(children).all()
    
    if not children_nodes:
        return [root_node]

    # children_nodes is list w/ elements of type NamedTuple, 
    # so use built-in func _asdict()
    nodes = [node._asdict() for node in children_nodes]
    nodes.insert(0, root_node)

    # remove extra node_id needed in recursive calls for children nodes
    for node in nodes:
        node.pop("node_id", None)
    
    return nodes

def postNode(node):  
    parent_id = node.get("parent_id", None)
    tree_id = db.session.query(BitByteTree.id).filter_by(name=node["tree_name"]).first()
    
    new_node = BitByteNode(node)
    db.session.add(new_node)
    db.session.flush()              # to access new_node.id

    # create new Tree if doesnt exist, otherwise add to that tree
    if not tree_id:
        new_tree = BitByteTree(node["tree_name"], new_node.id, "No description")
        db.session.add(new_tree)
    
    # create new ParentChildConnection if Bit/Byte has parent
    if parent_id:
        new_connection = ParentChildConnection(new_node.id, parent_id)
        db.session.add(new_connection)

    db.session.commit()    
   
    return new_node.serialize()