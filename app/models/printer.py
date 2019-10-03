# encoding: utf-8
from datetime import datetime

from app import db, app
import json
from app.utils.json_serial import json_serial


class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    model = db.Column(db.String(180))
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)
