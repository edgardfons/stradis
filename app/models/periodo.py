from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError

from .entity import Entity, EntityCreateForm, EntityIndexForm
from app.extensions import db

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

class Periodo(Entity):
    __tablename__= "periodo"
    inicio = db.Column(db.Integer, nullable=False)
    fim = db.Column(db.Integer, nullable=False)
    dia = db.Column(db.Enum(Dias), nullable=False)

    def desc(self):
        return self.dia + ' ' + self.inicio + ' ' + self.fim

class PeriodoIndexForm(EntityIndexForm):
    dia = SelectMultipleField('Dias', choices=Dias.select_list())

class PeriodoCreateForm(EntityCreateForm):
    dia = SelectMultipleField('Dias', choices=Dias.select_list())
