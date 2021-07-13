from app.extensions import db
from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField

class Entity(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

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