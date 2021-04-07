from flask_sqlalchemy import SQLAlchemy
from enum import Enum, IntFlag, auto

NAME_LIMIT = 250

db = SQLAlchemy()
   
class GradeCurricular(Enum):
    G_20081 = auto()
    G_20151 = auto()

class PeriodoLetivo(Enum):
    P_20202 = auto()

class Dia(IntFlag):
    DOM = auto()
    SEG = auto()
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()

class Professor(db.Model):
    __tablename__="professor"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)

class Curso(db.Model):
    __tablename__="curso"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)

class Disciplina(db.Model):
    __tablename__="disciplina"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    grade_curricular = db.Column(db.Enum(GradeCurricular))

class Campus(db.Model):
    __tablename__="campus"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)


class Horario(db.Model):
    __tablename__="horario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT))
    inicio = db.Column(db.String(5))
    fim = db.Column(db.String(5))
    utlimo_dia = db.Column(db.Boolean, default=False, nullable=False)

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

