from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.disciplina import Disciplina, DisciplinaCreateForm, DisciplinaIndexForm
from app.utils import sql_ilike_format

PAGE = 1
PER_PAGE = 5
disciplina_bp = Blueprint('disciplina', __name__)

@disciplina_bp.route('/', defaults={"page": 1}) 
@disciplina_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = PER_PAGE

    disciplina_form = DisciplinaIndexForm()
    disciplinas = Disciplina.query

    disciplina_form.nome.data = request.args.get('nome')
    disciplina_form.codigo.data = request.args.get('codigo')

    disciplinas = disciplinas.filter( Disciplina.nome.ilike(sql_ilike_format(disciplina_form.nome.data)) ) if disciplina_form.nome.data else disciplinas
    disciplinas = disciplinas.filter( Disciplina.codigo.ilike(sql_ilike_format(disciplina_form.codigo.data)) ) if disciplina_form.codigo.data else disciplinas

    disciplinas = disciplinas.order_by(Disciplina.id.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('disciplinas/index.html', disciplinas=disciplinas, disciplina_form=disciplina_form, disciplina=DisciplinaCreateForm(), disc_tab=True)

@disciplina_bp.route('', methods=['POST'])
def new():
    disciplina_form = DisciplinaCreateForm()   

    if disciplina_form.validate_on_submit():

        if disciplina_form.id.data:
            disciplina = Disciplina.query.get_or_404( disciplina_form.id.data )

            disciplina.nome=disciplina_form.nome.data
            disciplina.codigo=disciplina_form.codigo.data
        else:
            disciplina = Disciplina(
                nome=disciplina_form.nome.data,
                codigo=disciplina_form.codigo.data
            )

        disciplina.save()

        flash('Disciplina salvo com sucesso!', 'success')

        return redirect(url_for('disciplina.index'))

    return render_template('disciplinaes/index.html', disciplina=disciplina_form)

@disciplina_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):

    disciplina = Disciplina.query.get_or_404( id )

    disciplina_form = DisciplinaIndexForm()
    disciplinaes = Disciplina.query.order_by(Disciplina.id.desc()).paginate(PAGE, per_page=PER_PAGE, error_out=True)

    return render_template('disciplinaes/index.html', disciplinaes=disciplinas, disciplina_form=disciplina_form, disciplina=DisciplinaCreateForm(disciplina), prof_tab=True)

@disciplina_bp.route('/<int:id>', methods=['POST'])
def delete(id):

    disciplina = Disciplina.query.get_or_404( id )

    disciplina.delete()

    flash('Disciplina excluido com sucesso!', 'success')

    return redirect(url_for('disciplina.index'))