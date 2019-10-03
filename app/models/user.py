# encoding: utf-8
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy.dialects.mysql import JSON

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(180), unique=True)
    password = db.Column(db.String(180))
    cellphone = db.Column(db.String(180))
    photo = db.Column(db.String(180))
    roles = db.Column(db.JSON)
    # control
    deleted = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, name, email, password, cellphone, photo, roles):
        self.name = name
        self.email = email
        self.password = password
        self.cellphone = cellphone
        self.photo = photo
        self.roles = roles
        self.deleted = False
        self.blocked = False
        self.created_at = datetime.now()
