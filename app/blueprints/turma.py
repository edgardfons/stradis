from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.turma import Turma, TurmaCreateForm, TurmaIndexForm, Status
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/', defaults={"page": 1}) 
@turma_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    turma = TurmaIndexForm()
    turmas = Turma.query

    turma.descricao.data = request.args.get('descricao')
    turma.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    turma.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    turmas = turmas.filter( Turma.descricao.ilike(sql_ilike_format(turma.descricao.data)) ) if turma.descricao.data else turmas
    turmas = turmas.filter( Turma.vencimento >= sql_date_format(turma.inicio.data) ) if turma.inicio.data else turmas
    turmas = turmas.filter( Turma.vencimento <= sql_date_format(turma.fim.data) ) if turma.fim.data else turmas

    turmas = turmas.order_by(Turma.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('turmas/index.html', turmas=turmas, titulo_form=turma)

@turma_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = TurmaCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            turma = Turma.query.get_or_404( titulo_form.codigo.data )

            turma.descricao=titulo_form.descricao.data, 
            turma.valor=titulo_form.valor.data, 
            turma.vencimento=titulo_form.vencimento.data,
            turma.status=titulo_form.status.data
        else:
            turma = Turma(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        turma.save()

        flash('Titúlo salvo com sucesso!', 'success')

        return redirect(url_for('turma.new'))

    print('Turma errors: ' + str(titulo_form.errors))
    return render_template('turmas/new.html', turma=titulo_form)

@turma_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    turma = Turma.query.get_or_404(titulo_id)
    titulo_form = TurmaCreateForm()

    titulo_form.from_model(turma)

    return render_template('turmas/new.html', turma=titulo_form)

@turma_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    turma = Turma.query.get_or_404(titulo_id)

    turma.delete()

    return redirect(url_for('turma.index'))