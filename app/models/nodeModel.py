from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql

from ..database import db

class Node(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(128))
    children = db.Column(postgresql.ARRAY(db.Integer))

    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def serialize(self):
        return {
            "id": self.id,
            "value": self.value,
            "children": self.children
        }
