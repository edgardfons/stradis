import os
import uuid
import click

from flask import Flask, render_template, flash, redirect, url_for, request
from forms import *
from models import *

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/stradis_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grades')
def grades():

    grades = Grade.query.all()

    return render_template('grades/index.html', grades=grades, grade_tab=True)

@app.route('/grades/<int:id>')
def grades_view(id):

    grade = Grade.query.get_or_404(id)

    return render_template('grades/view.html', grade=grade, grade_tab=True)

    
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
    save_form = TurmaSaveForm()

    if request.method == 'POST' and save_form.validate():
        turma = Turma(nome=save_form.nome.data)
        db.session.add(turma)
        db.session.commit()
        flash('Turma salva com sucesso!', 'success')
        return redirect(url_for('turmas'))

    turmas = Turma.query.all()

    return render_template('turmas/index.html', turma_tab=True, turmas=turmas, save_form=save_form)

@app.route('/cursos', methods=['GET', 'POST'])
def cursos():
    save_form = CursoSaveForm()

    if request.method == 'POST' and save_form.validate():
        curso = Curso(nome=save_form.nome.data)
        db.session.add(curso)
        db.session.commit()
        flash('Curso salva com sucesso!', 'success')
        return redirect(url_for('cursos'))

    cursos = Curso.query.all()

    return render_template('cursos/index.html', curso_tab=True, cursos=cursos, save_form=save_form)

@app.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    save_form = DisciplinaSaveForm()

    if request.method == 'POST' and save_form.validate():
        disciplina = Disciplina(nome=save_form.nome.data)
        db.session.add(disciplina)
        db.session.commit()
        flash('Disciplina salva com sucesso!', 'success')
        return redirect(url_for('disciplinas'))

    disciplinas = Disciplina.query.all()

    return render_template('disciplinas/index.html', disc_tab=True, disciplinas=disciplinas, save_form=save_form)

@app.route('/horarios', methods=['GET', 'POST'])
def horarios():
    save_form = HorarioSaveForm()

    if request.method == 'POST' and save_form.validate():
        horario = Horario(nome=save_form.nome.data,inicio=save_form.inicio.data,fim=save_form.fim.data)
        db.session.add(horario)
        db.session.commit()
        flash('Disciplina salva com sucesso!', 'success')
        return redirect(url_for('disciplinas'))

    horarios = Horario.query.all()

    return render_template('horarios/index.html', hora_tab=True, horarios=horarios, save_form=save_form)