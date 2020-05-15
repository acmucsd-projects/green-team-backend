from .. import db
from ..models import ParentChildConnection

def seedConnections():
    connections = [
        ParentChildConnection(2, 1), 
        ParentChildConnection(3, 1), 
        ParentChildConnection(5, 4)
    ]

    db.session.query(ParentChildConnection).delete()
    db.session.bulk_save_objects(connections)
    db.session.commit()