from flask_sqlalchemy import SQLAlchemy
from .. import db

class BitByteNode(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    major = db.Column(db.String(128))
    college = db.Column(db.String(128))
    class_year = db.Column(db.Integer)
    tree_name = db.Column(db.String(128))
    quarter_joined = db.Column(db.String(128))
    linkedin = db.Column(db.String(128))
    facebook = db.Column(db.String(128))
    instagram = db.Column(db.String(128))
    child_node_1 = db.Column(db.Integer)
    child_node_2 = db.Column(db.Integer)

    def __init__(self, name, major, college, 
        class_year, tree_name, quarter_joined,
        linkedin, facebook, instagram, child_node_1, child_node_2):
        self.name = name
        self.major = major
        self.college = college
        self.class_year = class_year
        self.tree_name = tree_name
        self.quarter_joined = quarter_joined
        self.linkedin = linkedin
        self.facebook = facebook
        self.instagram = instagram
        self.child_node_1 = child_node_1
        self.child_node_2 = child_node_2
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "major": self.major,
            "college": self.college,
            "class_year": self.class_year,
            "tree_name": self.tree_name,
            "quarter_joined": self.quarter_joined,
            "linkedin": self.linkedin,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "child_node_1": self.child_node_1,
            "child_node_2": self.child_node_2
        }
