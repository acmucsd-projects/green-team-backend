# from flask_seeder import Seeder
from ..models import BitByteNode
from .. import db

def seedNodes():
    nodes = {
        "node1":  BitByteNode({
            "name": "John Doe",
            "major": "Computer Science",
            "college": "Sixth",
            "class_year": 2021,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "opt_in": True,
        }),
        "node2": BitByteNode({
            "name": "Jane Doe",
            "major": "Math-CS",
            "college": "Warren",
            "class_year": 2022,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "opt_in": True,
        }),
        "node3":  BitByteNode({
            "name": "Jack Doe",
            "major": "Data Science",
            "college": "Muir",
            "class_year": 2023,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "opt_in": True,
        }),
        "node4": BitByteNode({
            "name": "Fred Ted",
            "major": "Computer Engineering",
            "college": "Sixth",
            "class_year": 2024,
            "tree_name": "Brown Tree",
            "quarter_joined": "Winter 2021",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "opt_in": True,
        }),
        "node5": BitByteNode({
            "name": "Lisa McCormick",
            "major": "Computer Science",
            "college": "ERC",
            "class_year": 2021,
            "tree_name": "Brown Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "opt_in": True,
        })
    }
        
    nodesToDelete = db.session.query(BitByteNode).all()
    for node in nodesToDelete:
        db.session.delete(node)
    db.session.commit()
    for node in nodes:
        db.session.add(nodes[node])
    db.session.commit()
    

