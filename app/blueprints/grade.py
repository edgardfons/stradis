from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.grade import Grade, GradeCreateForm, GradeIndexForm
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

grade_bp = Blueprint('grade', __name__)

@grade_bp.route('/', defaults={"page": 1}) 
@grade_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    grade = GradeIndexForm()
    grades = Grade.query

    grade.descricao.data = request.args.get('descricao')
    grade.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    grade.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    grades = grades.filter( Grade.descricao.ilike(sql_ilike_format(grade.descricao.data)) ) if grade.descricao.data else grades
    grades = grades.filter( Grade.vencimento >= sql_date_format(grade.inicio.data) ) if grade.inicio.data else grades
    grades = grades.filter( Grade.vencimento <= sql_date_format(grade.fim.data) ) if grade.fim.data else grades

    grades = grades.order_by(Grade.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('grades/index.html', grades=grades, titulo_form=grade)

@grade_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = GradeCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            grade = Grade.query.get_or_404( titulo_form.codigo.data )

            grade.descricao=titulo_form.descricao.data, 
            grade.valor=titulo_form.valor.data, 
            grade.vencimento=titulo_form.vencimento.data,
            grade.status=titulo_form.status.data
        else:
            grade = Grade(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        grade.save()

        flash('Titúlo salvo com sucesso!', 'success')

        return redirect(url_for('grade.new'))

    print('Grade errors: ' + str(titulo_form.errors))
    return render_template('grades/new.html', grade=titulo_form)

@grade_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    grade = Grade.query.get_or_404(titulo_id)
    titulo_form = GradeCreateForm()

    titulo_form.from_model(grade)

    return render_template('grades/new.html', grade=titulo_form)

@grade_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    grade = Grade.query.get_or_404(titulo_id)

    grade.delete()

    return redirect(url_for('grade.index'))