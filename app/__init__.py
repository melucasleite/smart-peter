# encoding=utf-8
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_required
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.utils import error_handlers
from app.views import *
from app.jobs.count import count


scheduler = BackgroundScheduler()
# jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
scheduler.start()
scheduler.add_job(count, id="count", replace_existing=True,
                  trigger="interval", seconds=5*60)
