from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Turma(db.Model):
    __tablename__="turma"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), nullable=False)
    geminada = db.Column(db.Boolean, default=False, nullable=False)
    aulas_num = db.Column(db.Integer, default=2, nullable=False)
    etapa = db.Column(db.Integer, nullable=False)
    periodo_letivo = db.Column(db.Enum(PeriodoLetivo), nullable=False)
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    indisponibilidade = db.relationship('TurmaIndisponibilidade', backref='turma', lazy=True)
    pre_agendado = db.relationship('TurmaPreAgendada', backref='turma', lazy=True)

class TurmaIndisponibilidade(db.Model):
    __tablename__="turma_indisponibilidade"
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'), nullable=False)
    dia = db.Column(db.Enum(Dia), nullable=False)

class TurmaPreAgendada(db.Model):
    __tablename__="turma_preagendada"
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'), nullable=False)
    dia = db.Column(db.Enum(Dia), nullable=False)
