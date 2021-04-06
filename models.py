from flask_sqlalchemy import SQLAlchemy

NAME_LIMIT = 250

db = SQLAlchemy()
   
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

class Campus(db.Model):
    __tablename__="campus"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)

class Turma(db.Model):
    __tablename__="turma"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(NAME_LIMIT), nullable=False)