from .. import db
from ..models import User
from werkzeug.security import generate_password_hash
def seedUsers():
    Users = [
        User("admin", generate_password_hash("admin"))
    ]

    db.session.query(User).delete()
    db.session.bulk_save_objects(Users)
    db.session.commit()
