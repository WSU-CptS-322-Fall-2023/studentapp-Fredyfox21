from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = Config.STATIC_FOLDER
app.template_folder = Config.TEMPLATE_FOLDER

db = SQLAlchemy(app)
bootstrap =Bootstrap(app)

login = LoginManager(app)
login.login_view= 'login'

moment = Moment(app)

from app.Controller import routes, errors
from app.Model import models
