from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.disciplina import Disciplina, DisciplinaCreateForm, DisciplinaIndexForm, Status
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

disciplina_bp = Blueprint('disciplina', __name__)

@disciplina_bp.route('/', defaults={"page": 1}) 
@disciplina_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    disciplina = DisciplinaIndexForm()
    disciplinas = Disciplina.query

    disciplina.descricao.data = request.args.get('descricao')
    disciplina.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    disciplina.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    disciplinas = disciplinas.filter( Disciplina.descricao.ilike(sql_ilike_format(disciplina.descricao.data)) ) if disciplina.descricao.data else disciplinas
    disciplinas = disciplinas.filter( Disciplina.vencimento >= sql_date_format(disciplina.inicio.data) ) if disciplina.inicio.data else disciplinas
    disciplinas = disciplinas.filter( Disciplina.vencimento <= sql_date_format(disciplina.fim.data) ) if disciplina.fim.data else disciplinas

    disciplinas = disciplinas.order_by(Disciplina.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('disciplinas/index.html', disciplinas=disciplinas, titulo_form=disciplina)

@disciplina_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = DisciplinaCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            disciplina = Disciplina.query.get_or_404( titulo_form.codigo.data )

            disciplina.descricao=titulo_form.descricao.data, 
            disciplina.valor=titulo_form.valor.data, 
            disciplina.vencimento=titulo_form.vencimento.data,
            disciplina.status=titulo_form.status.data
        else:
            disciplina = Disciplina(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        disciplina.save()

        flash('Titúlo salvo com sucesso!', 'success')

        return redirect(url_for('disciplina.new'))

    print('Disciplina errors: ' + str(titulo_form.errors))
    return render_template('disciplinas/new.html', disciplina=titulo_form)

@disciplina_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    disciplina = Disciplina.query.get_or_404(titulo_id)
    titulo_form = DisciplinaCreateForm()

    titulo_form.from_model(disciplina)

    return render_template('disciplinas/new.html', disciplina=titulo_form)

@disciplina_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    disciplina = Disciplina.query.get_or_404(titulo_id)

    disciplina.delete()

    return redirect(url_for('disciplina.index'))