from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField, SelectMultipleField

from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db

NAME_LIMIT = 250
CODE_LIMIT = 10

class Disciplina(Entity):
    __tablename__="disciplina"
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    codigo = db.Column(db.String(CODE_LIMIT))
    turmas = db.relationship('Turma', backref='disciplina', lazy=True)

class DisciplinaIndexForm(EntityIndexForm):
    dia = SelectMultipleField('Dias', choices=[])

class DisciplinaCreateForm(EntityCreateForm):
    dia = SelectMultipleField('Dias', choices=[] )
