from app import db 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.datetime, nullable = False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])

    def __repr__(self):
        return f'< User| {self.username} >'

    def check_password(self, password):
        return check_password_hash(self.password, password)    