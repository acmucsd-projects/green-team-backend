from .. import db

# Supports easily pulling up entire trees and storing common information
class BitByteTree(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    root_id = db.Column(db.Integer, db.ForeignKey("bit_byte_tree.id"))
    # add points, badges, tree description, etc. if confirmed feature

    def __init__(self, name, root_id):
        self.name = name
        self.root_id = root_id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "root_id": self.root_id
        }