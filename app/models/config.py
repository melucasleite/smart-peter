from app import db


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    api = db.Column(db.String(180))
    token = db.Column(db.String(180))

    def __init__(self, name, api, token):
        self.name = name
        self.api = api
        self.token = token

    def to_dict(self):
        return {
            "name": self.name,
            "api": self.api,
            "token": self.token
        }
