from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

NAME_LIMIT = 250

from app.extensions import db

class Professor(db.Model):
    __tablename__="professor"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    turmas = db.relationship('Turma', backref='professor', lazy=True)

class ProfessorIndexForm(FlaskForm):
    nome = StringField('Nome', validators=[Length(1, NAME_LIMIT)])

class ProfessorCreateForm(FlaskForm):
    id = HiddenField()
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 60)])