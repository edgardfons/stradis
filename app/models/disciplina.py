from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Disciplina(db.Model):
    __tablename__="disciplina"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    grade_curricular = db.Column(db.Enum(GradeCurricular))
    turmas = db.relationship('Turma', backref='disciplina', lazy=True)

class DisciplinaSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    submit = SubmitField('Cadastrar')
