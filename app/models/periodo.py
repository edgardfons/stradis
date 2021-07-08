from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.extensions import db

class Dia(IntFlag):
    DOM = auto()
    SEG = auto()
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()

class Periodo(db.Model):
    __tablename__="periodo"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT))
    inicio = db.Column(db.String(5))
    fim = db.Column(db.String(5))
    utlimo_dia = db.Column(db.Boolean, default=False, nullable=False)
    ordem = db.Column(db.Integer, default=1, nullable=False)

    def desc(self):
        return self.nome + ' ' + self.inicio + ' ' + self.fim


class HorarioSaveForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(1, 250)])
    nome = StringField('Inicio', validators=[Length(0, 5)])
    nome = StringField('Fim', validators=[Length(0, 5)])
    submit = SubmitField('Cadastrar')