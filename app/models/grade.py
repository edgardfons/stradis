from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class GradeCurricular(Enum):
    G_20081 = auto()
    G_20151 = auto()
    
class Grade(db.Model):
    __tablename__="grade"
    id = db.Column(db.Integer, primary_key=True)
    criada = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    nome = db.Column(db.String(NAME_LIMIT))
    professores = db.Column(db.Integer, nullable=False)
    turmas = db.Column(db.Integer, nullable=False)
    entradas = db.relationship('GradeEntrada', backref='grade', lazy=True, cascade="all, delete-orphan")

class GradeEntrada(db.Model):
    __tablename__="grade_entrada"
    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Enum(Dia), nullable=False)
    horario = db.Column(db.String(260), nullable=False)
    disciplina = db.Column(db.String(255), nullable=False)
    professor = db.Column(db.String(255), nullable=False)
    ordem = db.Column(db.Integer, nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)

    def __str__(self):
        return "Disciplina: %s | Professor: %s | Dia: %s | Hora: %s" % (self.disciplina, self.professor, self.dia.name, self.horario)
