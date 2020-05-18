from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from ..database.models import User
from ..database import db

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return True
    return False
