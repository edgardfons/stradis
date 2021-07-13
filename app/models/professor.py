from enum import Enum, IntFlag, auto
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db

NAME_LIMIT = 250

class Professor(Entity):
    __tablename__="professor"
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    turmas = db.relationship('Turma', backref='professor', lazy=True)

class ProfessorIndexForm(EntityIndexForm):
    nome = StringField('Nome', validators=[Length(1, NAME_LIMIT)])

class ProfessorCreateForm(EntityCreateForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, NAME_LIMIT)])
    submit = SubmitField('Cadastrar')