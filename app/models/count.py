# encoding: utf-8
from datetime import datetime
from app import db, app


class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    printer_id = db.Column(db.Integer, db.ForeignKey("printer.id"))
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, printer_id, count):
        self.printer_id = printer_id
        self.count = count
        self.created_at = datetime.now()
        self.deleted = False
