from ..database.models import BitByteTree
from ..database.models import BitByteNode
from ..database.models import Connection
from ..database import db

from ..services import nodeService

def getTree(tree_id):
    tree = db.session.query(BitByteTree).filter_by(id=tree_id).first()
    if not tree:
        return None

    nodes = nodeService.getNodeAndChildren(tree.root_id)
    
    tree = tree.serialize()
    tree["nodes"] = nodes

    return tree