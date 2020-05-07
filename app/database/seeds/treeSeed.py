from .. import db
from ..models import BitByteTree

def seedTrees():
    trees = {
        "tree1": BitByteTree("Green Tree", 1),
        "tree2": BitByteTree("Brown Tree", 4)
    }

    treesToDelete = db.session.query(BitByteTree).all()
    for tree in treesToDelete:
        db.session.delete(tree)
    
    for tree in trees:
        db.session.add(trees[tree])
    db.session.commit()