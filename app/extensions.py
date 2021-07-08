from flask import request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
babel = Babel()
csrf = CSRFProtect()