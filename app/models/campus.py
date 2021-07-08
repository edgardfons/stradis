from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Campus(db.Model):
    __tablename__="campus"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)

class CampusSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')
