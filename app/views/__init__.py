from app import app
from app.api.security import admin_permission
from flask import render_template
from flask_login import login_required


@app.route("/")
@login_required
def user_index():
    return render_template("admin/index.html")


@app.route("/finances")
@admin_permission.require(http_exception=403)
def finances():
    return render_template("admin/finances.html")


@app.route("/login")
def login():
    return render_template("admin/login.html")


@app.route("/register")
def register():
    return render_template("admin/register.html")


@app.route("/students")
def students():
    return render_template("admin/students.html")


@app.route("/students/review")
def students_review():
    return render_template("admin/students-review.html")


@app.route("/lectures")
def lectures():
    return render_template("admin/lectures.html")


@app.route("/settings/lectures")
@admin_permission.require(http_exception=403)
def settings_lectures():
    return render_template("admin/settings/lectures.html")


@app.route("/settings")
@admin_permission.require(http_exception=403)
def settings():
    return render_template("admin/settings/settings.html")


@app.route("/settings/profile")
@admin_permission.require(http_exception=403)
def settings_profile():
    return render_template("admin/settings/profile.html")


@app.route("/settings/password")
@admin_permission.require(http_exception=403)
def settings_password():
    return render_template("admin/settings/password.html")


@app.route("/settings/skills_and_remarks")
@admin_permission.require(http_exception=403)
def settings_skills_and_remarks():
    return render_template("admin/settings/skills_and_remarks.html")


@app.route("/settings/teachers")
@admin_permission.require(http_exception=403)
def settings_teachers():
    return render_template("admin/settings/teachers.html")


@app.route("/settings/level")
@admin_permission.require(http_exception=403)
def settings_level():
    return render_template("admin/settings/level.html")


@app.route("/student-signin")
@login_required
def student_signin():
    return render_template("student-signin.html")
