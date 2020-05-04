from .. import db

# Supports easily pulling up entire trees and storing common information
class BitByteTree(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    points = db.Column(db.Integer, default=0)
    root_id = db.Column(db.Integer, db.ForeignKey("bit_byte_node.id"))
    # add badges, tree description, etc. if confirmed feature

    def __init__(self, name, root_id):
        self.name = name
        self.points = 0
        self.root_id = root_id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "points": self.points,
            "root_id": self.root_id
        }
