from .. import db
from ..models import ParentChildConnection

def seedConnections():
    connections = {
        "connection21": ParentChildConnection(2, 1),
        "connection31": ParentChildConnection(3, 1),
        "connection54": ParentChildConnection(5, 4),
    }

    connectionsToDelete = db.session.query(ParentChildConnection).all()
    for connection in connectionsToDelete:
        db.session.delete(connection)
    
    for connection in connections:
        db.session.add(connections[connection])
    db.session.commit()