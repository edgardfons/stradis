from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField, SelectMultipleField

from .periodo import Dias
from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db
    
class Grade(Entity):
    __tablename__="grade"
    criada = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    semestre_letivo = db.Column(db.String(5), nullable=False)
    entradas = db.relationship('GradeTurma', backref='grade', lazy=True, cascade="all, delete-orphan")

class GradeTurma(db.Model):
    __tablename__="grade_turma"
    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Enum(Dias), nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodo.id'), nullable=False)

class GradeIndexForm(EntityIndexForm):
    dia = SelectMultipleField('Dias', choices=[])

class GradeCreateForm(EntityCreateForm):
    dia = SelectMultipleField('Dias', choices=[] )
