from enum import IntFlag, auto
from wtforms import StringField, IntegerField, SelectField

from .periodo import Dias
from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db

CODE_LIMIT = 10

class Config(IntFlag):
    INDISPONIVEL = auto()
    PRE_AGENDADA = auto()

class Turma(Entity):
    __tablename__="turma"
    etapa = db.Column(db.Integer, nullable=False)
    codigo = db.Column(db.String(CODE_LIMIT))
    aulas_num = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    configs = db.relationship('TurmaConfig', backref='turma', lazy=True)
    grades = db.relationship('GradeTurma', backref='turma', lazy=True)

    def indisponibilidade(self):
        return list( filter(lambda config: config.config == Config.INDISPONIVEL, self.configs) )

    def pre_agendado(self):
        return list( filter(lambda config: config.config == Config.PRE_AGENDADA, self.configs) )

class TurmaConfig(db.Model):
    __tablename__="turma_config"
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    dia = db.Column(db.Enum(Dias), nullable=False)
    periodo_id = db.Column(db.Integer, db.ForeignKey('periodo.id'), nullable=False)
    config = db.Column(db.Enum(Config), nullable=False)

class TurmaIndexForm(EntityIndexForm):
    professor = SelectField('Professor')
    disciplina = SelectField('Disciplina')

class TurmaCreateForm(EntityCreateForm):
    codigo = StringField('Código')
    professor = SelectField('Professor')
    disciplina = SelectField('Disciplina')
    etapa = IntegerField('Etapa')
    aulas_num = IntegerField('Núm. Aulas')