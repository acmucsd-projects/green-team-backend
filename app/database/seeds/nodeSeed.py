from ..models import BitByteNode
from .. import db

def seedNodes():
    nodes = [
        BitByteNode({
            "name": "John Doe",
            "username": "johnnythough",
            "major": "Computer Science",
            "college": "Sixth",
            "class_year": 2021,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "profile_url": "https://www.acmucsd.org",
            "opt_in": True,
        }),
        BitByteNode({
            "name": "Jane Doe",
            "username": "janeythough",
            "major": "Math-CS",
            "college": "Warren",
            "class_year": 2022,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "profile_url": "https://www.acmucsd.org",
            "opt_in": True,
        }),
        BitByteNode({
            "name": "Jack Doe",
            "username": "jackiethough",
            "major": "Data Science",
            "college": "Muir",
            "class_year": 2023,
            "tree_name": "Green Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "profile_url": "https://www.acmucsd.org",
            "opt_in": True,
        }),
        BitByteNode({
            "name": "Fred Ted",
            "username": "itsfredtheted",
            "major": "Computer Engineering",
            "college": "Sixth",
            "class_year": 2024,
            "tree_name": "Brown Tree",
            "quarter_joined": "Winter 2021",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "profile_url": "https://www.acmucsd.org",
            "opt_in": True,
        }),
        BitByteNode({
            "name": "Lisa McCormick",
            "username": "averywhiteusername",
            "major": "Computer Science",
            "college": "ERC",
            "class_year": 2021,
            "tree_name": "Brown Tree",
            "quarter_joined": "Winter 2020",
            "linkedin": "https://www.linkedin.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "profile_url": "https://www.acmucsd.org",
            "opt_in": True,
        })
    ]
        
    db.session.query(BitByteNode).delete()
    db.session.bulk_save_objects(nodes)
    db.session.commit()
    

