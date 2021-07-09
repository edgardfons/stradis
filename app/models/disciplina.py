from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

NAME_LIMIT = 250

class Disciplina(db.Model):
    __tablename__="disciplina"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)

class DisciplinaIndexForm(FlaskForm):
    dia = SelectMultipleField('Dias', choices=[])

class DisciplinaCreateForm(FlaskForm):
    id = HiddenField()
    dia = SelectMultipleField('Dias', choices=[] )
