from app.extensions import db
from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, SubmitField
from sqlalchemy.ext.declarative import declared_attr

class Entity(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def instituicao_id(cls):
        return db.Column(db.Integer, db.ForeignKey('instituicao.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class EntityIndexForm(FlaskForm):
    id = IntegerField('#')

class EntityCreateForm(FlaskForm):
    id = HiddenField()
    submit = SubmitField('Cadastrar')