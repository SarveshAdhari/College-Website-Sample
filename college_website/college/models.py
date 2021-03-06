from enum import unique
from flask_login import UserMixin
from college import db, login_manager



@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    email = db.Column(db.String(100),unique=True, nullable = False)
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"