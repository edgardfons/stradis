from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.curso import Curso, CursoCreateForm, CursoIndexForm, Status
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

curso_bp = Blueprint('curso', __name__)

@curso_bp.route('/', defaults={"page": 1}) 
@curso_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    curso = CursoIndexForm()
    cursos = Curso.query

    curso.descricao.data = request.args.get('descricao')
    curso.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    curso.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    cursos = cursos.filter( Curso.descricao.ilike(sql_ilike_format(curso.descricao.data)) ) if curso.descricao.data else cursos
    cursos = cursos.filter( Curso.vencimento >= sql_date_format(curso.inicio.data) ) if curso.inicio.data else cursos
    cursos = cursos.filter( Curso.vencimento <= sql_date_format(curso.fim.data) ) if curso.fim.data else cursos

    cursos = cursos.order_by(Curso.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('cursos/index.html', cursos=cursos, titulo_form=curso)

@curso_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = CursoCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            curso = Curso.query.get_or_404( titulo_form.codigo.data )

            curso.descricao=titulo_form.descricao.data, 
            curso.valor=titulo_form.valor.data, 
            curso.vencimento=titulo_form.vencimento.data,
            curso.status=titulo_form.status.data
        else:
            curso = Curso(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        curso.save()

        flash('Titúlo salvo com sucesso!', 'success')

        return redirect(url_for('curso.new'))

    print('Curso errors: ' + str(titulo_form.errors))
    return render_template('cursos/new.html', curso=titulo_form)

@curso_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    curso = Curso.query.get_or_404(titulo_id)
    titulo_form = CursoCreateForm()

    titulo_form.from_model(curso)

    return render_template('cursos/new.html', curso=titulo_form)

@curso_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    curso = Curso.query.get_or_404(titulo_id)

    curso.delete()

    return redirect(url_for('curso.index'))