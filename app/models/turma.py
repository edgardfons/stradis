from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Config(IntFlag):
    INDISPONIVEL = auto()
    PRE_AGENDADA = auto()

class Turma(db.Model):
    __tablename__="turma"
    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    configs = db.relationship('TurmaConfig', backref='turma', lazy=True)

class TurmaConfig(db.Model):
    __tablename__="turma_config"
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodo.id'), nullable=False)
    config = db.Column(db.Enum(Config), nullable=False)

class TurmaIndexForm(FlaskForm):
    dia = SelectField('Dias', choices=[])

class TurmaCreateForm(FlaskForm):
    id = HiddenField()
    dia = SelectField('Dias', choices=[] )