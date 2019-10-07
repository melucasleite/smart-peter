# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Printer


@app.route("/api/printer", methods=["GET"])
def api_printers_get():
    printers = Printer.query.filter_by(deleted=False).all()
    response = {"printers": map(lambda x: x.to_dict(), printers)}
    return jsonify(response)


@app.route("/api/printer", methods=["POST"])
def api_printer_post():
    args = request.form
    name = args["name"]
    crawler = args["crawler"]
    pat = args["pat"]
    model = args["model"]
    ip = args["ip"]
    printer = Printer(pat, model, name, ip, crawler, "")
    db.session.add(printer)
    db.session.commit()
    return jsonify({"message": "OK"})
