from .. import db

class Connection(db.Model):
    node_id = db.Column(db.Integer, db.ForeignKey("bit_byte_node.id"), primary_key=True)
    parent_node_id = db.Column(db.Integer, db.ForeignKey("bit_byte_node.id"))

    def __init__(self, node_id, parent_node_id):
        self.node_id = node_id
        self.parent_node_id = parent_node_id