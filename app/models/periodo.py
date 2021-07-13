from enum import IntFlag, auto
from wtforms import SelectMultipleField

from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db

NAME_LIMIT = 50

class Dias(IntFlag):
    DOM = auto()
    SEG = auto()
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()

    @staticmethod
    def select_list():
        return map(lambda dia: (dia.value, dia.name), list(Dias))

    @staticmethod
    def padroes():
        return (Dias.SEG, Dias.TER, Dias.QUA, Dias.QUI, Dias.SEX)


class Periodo(Entity):
    __tablename__= "periodo"
    nome = db.Column(db.String(NAME_LIMIT))
    inicio = db.Column(db.Integer, nullable=False)
    fim = db.Column(db.Integer, nullable=False)
    grades = db.relationship('GradeTurma', backref='periodo', lazy=True)

    def desc(self):
        return str(self.inicio) + '-' + str(self.fim)

class PeriodoIndexForm(EntityIndexForm):
    dia = SelectMultipleField('Dias', choices=Dias.select_list())

class PeriodoCreateForm(EntityCreateForm):
    dia = SelectMultipleField('Dias', choices=Dias.select_list())
