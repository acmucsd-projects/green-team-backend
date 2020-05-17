from .. import db

class BitByteNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    name = db.Column(db.String(128))
    major = db.Column(db.String(128))
    college = db.Column(db.String(128))
    class_year = db.Column(db.Integer)
    tree_name = db.Column(db.String(128))
    quarter_joined = db.Column(db.String(128))
    linkedin = db.Column(db.String(128))
    facebook = db.Column(db.String(128))
    instagram = db.Column(db.String(128))
    profile_url = db.Column(db.String(128))
    opt_in = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, node):
        self.name = node["name"]
        self.username = node["username"]
        self.major = node["major"]
        self.college = node["college"]
        self.class_year = node["class_year"]
        self.tree_name = node["tree_name"]
        self.quarter_joined = node["quarter_joined"]
        self.linkedin = node["linkedin"]
        self.facebook = node["facebook"]
        self.instagram = node["instagram"]
        self.profile_url = node["profile_url"]
        self.opt_in = node["opt_in"]

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "major": self.major,
            "college": self.college,
            "class_year": self.class_year,
            "tree_name": self.tree_name,
            "quarter_joined": self.quarter_joined,
            "linkedin": self.linkedin,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "profile_url": self.profile_url,
            "opt_in": self.opt_in
        }
