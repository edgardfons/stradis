from flask import request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()