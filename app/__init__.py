from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from app.config import Config

app = Flask(__name__)
from app import routes

app.config.from_object(Config)
db =SQLAlchemy(app)
migrate = Migrate(app, db)


