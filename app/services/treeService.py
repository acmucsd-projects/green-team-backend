from ..database.models import BitByteTree
from ..database.models import BitByteNode
from ..database.models import Connection
from ..database import db

from ..services import nodeService

from sqlalchemy.orm import aliased

def getTree(tree_id):
    root_id = db.session.query(BitByteTree.root_id).filter_by(id=tree_id).first()
    
    if not root_id:
        return None
    
    root_node = nodeService.getNodeById(root_id)
    root_node["parent_node_id"] = None

    non_recursive_clause = db.session.query(Connection, BitByteNode)\
        .join(BitByteNode, Connection.node_id == BitByteNode.id)\
        .filter(Connection.parent_node_id == root_id).cte(name='parent_for', recursive=True)

    with_recursive = non_recursive_clause.union_all(
        db.session.query(Connection, BitByteNode)\
            .join(BitByteNode, Connection.node_id == BitByteNode.id)\
            .filter(Connection.parent_node_id == non_recursive_clause.c.node_id)
    )

    children_nodes = db.session.query(with_recursive).all()
    
    # children_nodes is list w/ elements of type NamedTuple, 
    # so use built-in func _asdict()
    nodes = ([(node._asdict()) for node in children_nodes])

    # remove extra node_id needed in recursive calls for children nodes
    for node in nodes:
        del node["node_id"]

    nodes.insert(0, root_node)
    
    return nodes