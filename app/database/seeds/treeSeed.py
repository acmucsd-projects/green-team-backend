from .. import db
from ..models import BitByteTree

def seedTrees():
    trees = [
        BitByteTree("Green Tree", 1, "We are green"),
        BitByteTree("Brown Tree", 4, "We are brown")
    ]

    db.session.query(BitByteTree).delete()
    db.session.bulk_save_objects(trees)
    db.session.commit()