# encoding: utf-8
from datetime import datetime

from app import db, app
import json
from app.utils.json_serial import json_serial


class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pat = db.Column(db.String(180))
    model = db.Column(db.String(180))
    name = db.Column(db.String(180))
    ip = db.Column(db.String(180))
    crawler = db.Column(db.String(180))
    location = db.Column(db.String(180))

    count = db.Column(db.Integer)

    created_at = db.Column(db.DateTime)
    last_count = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, pat, model, name, ip, crawler, location):
        self.pat = pat
        self.model = model
        self.name = name
        self.ip = ip
        self.crawler = crawler
        self.location = location
        self.count = 0
        self.created_at = datetime.now()
        self.last_count = datetime.now()
        self.deleted = False

    def to_dict(self):
        return {
            "pat": self.pat,
            "model": self.model,
            "name": self.name,
            "ip": self.ip,
            "crawler": self.crawler,
            "location": self.location,
            "count": self.count,
            "created_at": self.created_at.isoformat(),
            "last_count": self.last_count.isoformat()
        }
