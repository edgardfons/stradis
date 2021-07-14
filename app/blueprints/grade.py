from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.grade import Grade, GradeCreateForm, GradeIndexForm
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

from app.models.periodo import Periodo, Dias

PAGE = 1
PER_PAGE = 5
grade_bp = Blueprint('grade', __name__)

@grade_bp.route('/', defaults={"page": 1}) 
@grade_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = PER_PAGE

    grade_form = GradeIndexForm()
    grades = Grade.query

    grades = grades.order_by(Grade.id.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('grades/index.html', grades=grades, grade_form=grade_form, grade_tab=True)

@grade_bp.route('', methods=['POST'])
def new():
    
    grade_form = GradeCreateForm()   

    if grade_form.validate_on_submit():

        conj = Conjuntos(
            days=Dias.padroes(), 
            hours=Periodo.query.all(),
            teachers=Professor.query.all(),
            terms=NUM_ETAPAS,
            events=Turma.query.all()
        )

        grade = solve(conj)
    
        grade.semestre_letivo = grade_form.semestre.data
        grade.save()

        flash('Grade salvo com sucesso!', 'success')

        return redirect(url_for('grade.index'))

    return render_template('gradees/index.html', grade=grade_form)

@grade_bp.route('/view/<int:id>', methods=['GET'])
def view(id):

    grade = Grade.query.get_or_404( id )
    entradas = {}
    periodos = Periodo.query.order_by(Periodo.inicio.asc()).all()

    for ent in grade.entradas:
        if not ent.dia in entradas.keys():
            entradas[ent.dia] = {}

        if not ent.periodo.id in entradas[ent.dia].keys():
            entradas[ent.dia][ent.periodo.id] = []
        
        entradas[ent.dia][ent.periodo.id].append( ent.turma )

    return render_template('grades/view.html', dias=Dias.padroes(), entradas=entradas, periodos=periodos, grade=grade, grade_tab=True)

@grade_bp.route('/<int:id>', methods=['POST'])
def delete(id):

    grade = Grade.query.get_or_404( id )

    grade.delete()

    flash('Grade excluido com sucesso!', 'success')

    return redirect(url_for('grade.index'))