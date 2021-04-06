import os
import uuid
import click

from flask import Flask, render_template, flash, redirect, url_for, request
from forms import *
from models import *

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/stradis"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/professores', methods=['GET', 'POST'])
def professores():
    save_form = ProfessorSaveForm()

    if request.method == 'POST' and save_form.validate():
        professor = Professor(nome=save_form.nome.data)
        db.session.add(professor)
        db.session.commit()
        flash('Professor(a) salvo com sucesso!', 'success')
        return redirect(url_for('professores'))

    professores = Professor.query.all()

    return render_template('professores/index.html', prof_tab=True, professores=professores, save_form=save_form)

@app.route('/turmas', methods=['GET', 'POST'])
def turmas():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('turmas/index.html')

@app.route('/salas', methods=['GET', 'POST'])
def salas():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('salas/index.html')

@app.route('/cursos', methods=['GET', 'POST'])
def cursos():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('cursos/index.html')

@app.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('disciplinas/index.html')