from .. import db
from ..models import User

def seedUsers():
    Users = [
        User("admin", "admin")
    ]

    db.session.query(User).delete()
    db.session.bulk_save_objects(Users)
    db.session.commit()
