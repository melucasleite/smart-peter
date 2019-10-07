# encoding: utf-8
from app import app, db, Config
from flask import request, jsonify


@app.route("/api/config", methods=["GET"])
def api_config_get():
    config = Config.query.get(1)
    if not config:
        config = Config("", "", "")
        db.session.commit()
    return jsonify({"config": config.to_dict()}), 200


@app.route("/api/config", methods=["POST"])
def api_config_post():
    args = request.form
    name = args["name"]
    api = args["api"]
    token = args["token"]
    config = Config.query.get(1)
    if not config:
        config = Config(name, api, token)
        db.session.add(config)
        db.session.commit()
    config.name = name
    config.api = api
    config.token = token
    db.session.commit()
    return jsonify({"message": "OK."}), 200
