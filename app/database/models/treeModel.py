from .. import db
import datetime

# Supports easily pulling up entire trees and storing common information
class BitByteTree(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    points = db.Column(db.Integer, default=0)
    root_id = db.Column(db.Integer, db.ForeignKey("bit_byte_node.id"))
    year = db.Column(db.Integer, default=datetime.date.today().year)
    profile_picture_url = db.Column(db.String(256))
    description = db.Column(db.Text)

    def __init__(self, name, root_id, description):
        self.name = name
        self.points = 0
        self.root_id = root_id
        self.year = year
        self.description = description

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "points": self.points,
            "root_id": self.root_id,
            "year": self.year,
            "profile_picture_url": self.profile_picture_url,
            "description": self.description
        }
