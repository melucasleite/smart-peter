from app import app
from flask import redirect, jsonify, url_for


@app.errorhandler(403)
def error_handler_forbidden(e):
    return redirect(url_for('login'))


@app.errorhandler(401)
def error_handler_api_unauthorized(e):
    return jsonify({"message": "Unauthorized."}), 401
