from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Dias(IntFlag):
    DOM = auto()
    SEG = auto()
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()

class Periodo(db.Model):
    __tablename__= "periodo"
    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.Integer, nullable=False)
    fim = db.Column(db.Integer, nullable=False)
    dia = db.Column(db.Integer, nullable=False)

    def desc(self):
        return self.dia + ' ' + self.inicio + ' ' + self.fim

class PeriodoIndexForm(FlaskForm):
    dia = SelectMultipleField('Dias', choices=[])

class PeriodoCreateForm(FlaskForm):
    id = HiddenField()
    dia = SelectMultipleField('Dias', choices=[] )
