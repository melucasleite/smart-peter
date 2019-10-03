# encoding: utf-8
from itsdangerous import URLSafeTimedSerializer
import os
import sys

from flask import render_template, request, redirect, url_for, flash, current_app, session, abort, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_principal import Permission, RoleNeed, identity_loaded, UserNeed, Principal, identity_changed, Identity, \
    AnonymousIdentity
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db, User

reload(sys)
sys.setdefaultencoding("utf-8")


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


# Flask-Principal
principals = Principal(app, skip_static=True)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar essa página.'

admin_permission = Permission(RoleNeed('admin'))


@app.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    args = request.form
    try:
        email = ts.loads(token, salt="recover-key", max_age=259200)
    except:
        abort(404)
    if request.method == 'POST':
        if args.get('password1') == args.get('password2'):
            user = User.query.filter_by(deleted=False).filter_by(
                email=email).first_or_404()
            new_password = generate_password_hash(
                args.get('password1'), method='sha256')
            user.password = new_password
            db.session.commit()
            flash('Senha alterada com sucesso!', "success")
            return redirect('/login')
    return render_template('security/reset.html', token=token)


@app.route("/api/security/login", methods=["POST"])
def api_user_login():
    args = request.form
    email = args.get('email')
    password = args.get('password')
    user = User.query.filter_by(
        deleted=False).filter_by(email=email).first()
    if not user:
        return jsonify({"message": "Não foi encontrado um usuário com esse e-mail."}), 400
    if user.password != password:
        return jsonify({"message": "Senha incorreta."}), 400
    login_user(user)
    identity_changed.send(current_app._get_current_object(),
                          identity=Identity(user.id))
    return jsonify({"message": "Login realizado com sucesso."}), 200


@app.route("/api/security/signup", methods=["POST"])
def api_user_signup():
    args = request.form
    name = args.get('name')
    email = args.get('email')
    cellphone = args.get('cellphone', "")
    password = args.get('password')
    secret = args.get('secret')
    photo = "/static/assets/images/users/default.jpg"
    roles = ["admin"]
    if secret != app.config["SECRET_KEY"]:
        return jsonify({"message": "Unauthorized."}), 401
    if not name or not email or not password:
        return jsonify({"message": "Missing mandatory fields."}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "There is a user with this e-mail."}), 400
    user = User(name, email, password, cellphone, photo, roles)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User Created."}), 200


@app.route("/api/security/forgot", methods=["POST"])
def api_user_forgot():
    args = request.form
    email = request.form.get("email")
    user = User.query.filter_by(deleted=False).filter_by(
        email=email).first()
    if not user:
        return jsonify({"message": "Não foi encontrado um usuário com esse e-mail."}), 400
    else:
        send_reset_password(user)
        return jsonify({"message": "Enviamos um e-mail de recuperação de senha para {}.".format(user.email)}), 200


@app.route("/api/security/password_recover")
def api_user_password_recover():
    return "not_implemented", 200


@app.route('/api/security/logout')
def logout():
    print "fired"
    for key in ['identity.id', 'identity.auth_type']:
        session.pop(key, None)
    logout_user()
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    return jsonify({"message": "User Logged Out."}), 200


def send_reset_password(user):
    email = user.email

    token = ts.dumps(email, salt='recover-key')
    recover_url = url_for('reset_with_token', token=token, _external=True)

    send_email(email, 'Recupere sua senha',
               html=render_template('email/recover.html', recover_url=recover_url))


@login_manager.user_loader
def load_user(user_id):
    if user_id:
        try:
            return User.query.filter_by(deleted=False).filter_by(id=int(user_id)).first()
        except ValueError:
            pass


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    user = current_user

    identity.user = user
    if hasattr(user, 'id'):
        identity.provides.add(UserNeed(user.id))

    if hasattr(user, 'roles'):
        for role in user.roles:
            identity.provides.add(RoleNeed(role))
