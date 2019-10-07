from app import app
from app.api.security import admin_permission
from flask import render_template
from flask_login import login_required
from app.models import Config


@app.route("/")
def user_index():
    return render_template("index.html")


@app.route("/config")
def view_config():
    return render_template("config.html")

@app.route("/counts")
def view_counts():
    return render_template("counts.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/api/entryPoint.js")
def api_entry_point():
    state = Config.query.get(1).to_dict()
    return render_template("entryPoint.js", state=state)