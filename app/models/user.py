# encoding: utf-8
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.dialects.mysql import JSON

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    user = db.Column(db.String(180), unique=True)
    password = db.Column(db.String(180))
    # control
    blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password
        self.blocked = False
        self.created_at = datetime.now()
