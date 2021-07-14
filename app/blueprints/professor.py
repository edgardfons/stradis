from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.professor import Professor, ProfessorCreateForm, ProfessorIndexForm
from app.utils import sql_ilike_format

PAGE = 1
PER_PAGE = 5
professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/', defaults={"page": 1}) 
@professor_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = PER_PAGE

    professor_form = ProfessorIndexForm()
    professores = Professor.query

    professor_form.nome.data = request.args.get('nome')

    professores = professores.filter( Professor.nome.ilike(sql_ilike_format(professor_form.nome.data)) ) if professor_form.nome.data else professores

    professores = professores.order_by(Professor.id.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('professores/index.html', professores=professores, professor_form=professor_form, professor=ProfessorCreateForm(), prof_tab=True)

@professor_bp.route('', methods=['POST'])
def new():
    professor_form = ProfessorCreateForm()   

    if professor_form.validate_on_submit():

        if professor_form.id.data:
            professor = Professor.query.get_or_404( professor_form.id.data )

            professor.nome=professor_form.nome.data
        else:
            professor = Professor(
                nome=professor_form.nome.data
            )

        professor.save()

        flash('Professor salvo com sucesso!', 'success')

        return redirect(url_for('professor.index'))

    return render_template('professores/index.html', professor=professor_form)

@professor_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):

    professor = Professor.query.get_or_404( id )

    professor_form = ProfessorIndexForm()
    professores = Professor.query.order_by(Professor.id.desc()).paginate(PAGE, per_page=PER_PAGE, error_out=True)

    return render_template('professores/index.html', professores=professores, professor_form=professor_form, professor=ProfessorCreateForm(professor), prof_tab=True)

@professor_bp.route('/<int:id>', methods=['POST'])
def delete(id):

    professor = Professor.query.get_or_404( id )

    professor.delete()

    flash('Professor excluido com sucesso!', 'success')

    return redirect(url_for('professor.index'))