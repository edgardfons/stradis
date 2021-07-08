from enum import Enum, IntFlag, auto
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, DateField, DecimalField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

NAME_LIMIT = 250

from app.extensions import db

class Professor(db.Model):
    __tablename__="professor"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)
    turmas = db.relationship('Turma', backref='professor', lazy=True)

class ProfessorIndexForm(FlaskForm):
    descricao = StringField('Descrição', validators=[Length(0, 60)])
    inicio = DateField('Inicio', format='%d/%m/%Y')
    fim = DateField('Fim', format='%d/%m/%Y')

class ProfessorCreateForm(FlaskForm):
    codigo = HiddenField()
    descricao = StringField('Descrição', validators=[DataRequired(), Length(1, 60)])
    vencimento = DateField('Vencimento', format='%d/%m/%Y', validators=[DataRequired()])
    valor = DecimalField('Valor', validators=[DataRequired()])
    submit = SubmitField('Salvar')

    def from_model(self, titulo):
        self.status.default = titulo.status.name
        self.process()

        self.codigo.data = titulo.codigo
        self.descricao.data = titulo.descricao
        self.vencimento.data = titulo.vencimento
        self.valor.data = titulo.valor


    def validate_vencimento(self, field):
        if (not self.codigo) and date.today() > field.data:
            raise ValidationError('Vencimento não pode ser em data passada!')

    def validate_valor(self, field):
        if field.data > 1000000000.00:
            raise ValidationError('Valor do titulo não pode ser maior que R$ 1.000.000.000,00')