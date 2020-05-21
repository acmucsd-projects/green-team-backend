from ..database.models import BitByteTree
from ..database.models import BitByteNode
from ..database import db

from ..services import nodeService

def getTreesAsc():
    trees = db.session.query(BitByteTree).order_by(BitByteTree.name).all()
    for i in range(len(trees)):
        trees[i] = trees[i].serialize()
        nodes = nodeService.getNodeAndChildren(trees[i]["root_id"])
        trees[i]["nodes"] = nodes
    return trees

def getTree(tree_id):
    tree = db.session.query(BitByteTree).filter_by(id=tree_id).first()
    if not tree:
        return None

    nodes = nodeService.getNodeAndChildren(tree.root_id)

    tree = tree.serialize()
    tree["nodes"] = nodes

    return tree

def updateTree(tree_id, body):
    # TODO: add error handling
    tree = db.session.query(BitByteTree).filter_by(id=tree_id).update(body)
    return tree

def addPointsById(tree_id, points):
    tree = db.session.query(BitByteTree).filter_by(id=tree_id).first()
    tree.points += points
    db.session.commit()
    return tree.serialize()

def updateProfileUrl(tree_id, url):
    tree = db.session.query(BitByteTree).filter_by(id=tree_id).first()
    tree.profile_picture_url = url
    db.session.commit()
    return tree.serialize()
