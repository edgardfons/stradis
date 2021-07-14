from enum import IntFlag, auto
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db
from app.utils import format_hour

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
        return format_hour(self.inicio) + '-' + format_hour(self.fim)

class PeriodoIndexForm(EntityIndexForm):
    nome = StringField('Nome')
    inicio = StringField('Início', validators=[Regexp('^[0-9]{2}:[0-9]{2}$')])
    fim = StringField('Fim', validators=[Regexp('^[0-9]{2}:[0-9]{2}$')])

class PeriodoCreateForm(EntityCreateForm):
    nome = StringField('Nome')
    inicio = StringField('Início', validators=[DataRequired(), Regexp('^[0-9]{2}:[0-9]{2}$')])
    fim = StringField('Fim', validators=[DataRequired(), Regexp('^[0-9]{2}:[0-9]{2}$')])
