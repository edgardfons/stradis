from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.professor import Professor, ProfessorCreateForm, ProfessorIndexForm
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/', defaults={"page": 1}) 
@professor_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    professor = ProfessorIndexForm()
    professores = Professor.query

    professor.descricao.data = request.args.get('descricao')
    professor.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    professor.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    professores = professores.filter( Professor.descricao.ilike(sql_ilike_format(professor.descricao.data)) ) if professor.descricao.data else professores
    professores = professores.filter( Professor.vencimento >= sql_date_format(professor.inicio.data) ) if professor.inicio.data else professores
    professores = professores.filter( Professor.vencimento <= sql_date_format(professor.fim.data) ) if professor.fim.data else professores

    professores = professores.order_by(Professor.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('professores/index.html', professores=professores, titulo_form=professor)

@professor_bp.route('/', methods=['POST'])
def new():
    titulo_form = ProfessorCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            professor = Professor.query.get_or_404( titulo_form.codigo.data )

            professor.descricao=titulo_form.descricao.data, 
            professor.valor=titulo_form.valor.data, 
            professor.vencimento=titulo_form.vencimento.data,
            professor.status=titulo_form.status.data
        else:
            professor = Professor(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        professor.save()

        flash('Professor salvo com sucesso!', 'success')

        return redirect(url_for('professor.new'))

    print('Professor errors: ' + str(titulo_form.errors))
    return render_template('professores/new.html', professor=titulo_form)

@professor_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    professor = Professor.query.get_or_404(titulo_id)
    titulo_form = ProfessorCreateForm()

    titulo_form.from_model(professor)

    return render_template('professores/new.html', professor=titulo_form)

@professor_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    professor = Professor.query.get_or_404(titulo_id)

    professor.delete()

    return redirect(url_for('professor.index'))