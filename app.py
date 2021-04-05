import os
import uuid

from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from forms import LoginForm

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/professores', methods=['GET', 'POST'])
def professores():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('professores/index.html', prof_tab=True)

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