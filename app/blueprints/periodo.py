from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.periodo import Periodo, PeriodoCreateForm, PeriodoIndexForm
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

periodo_bp = Blueprint('periodo', __name__)

@periodo_bp.route('/', defaults={"page": 1}) 
@periodo_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = 10

    periodo = PeriodoIndexForm()
    periodos = Periodo.query

    periodo.descricao.data = request.args.get('descricao')
    periodo.inicio.data = parse_date(request.args.get('inicio')) if request.args.get('inicio') else '' 
    periodo.fim.data = parse_date(request.args.get('fim')) if request.args.get('fim') else '' 

    periodos = periodos.filter( Periodo.descricao.ilike(sql_ilike_format(periodo.descricao.data)) ) if periodo.descricao.data else periodos
    periodos = periodos.filter( Periodo.vencimento >= sql_date_format(periodo.inicio.data) ) if periodo.inicio.data else periodos
    periodos = periodos.filter( Periodo.vencimento <= sql_date_format(periodo.fim.data) ) if periodo.fim.data else periodos

    periodos = periodos.order_by(Periodo.codigo.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('periodos/index.html', periodos=periodos, titulo_form=periodo)

@periodo_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = PeriodoCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            periodo = Periodo.query.get_or_404( titulo_form.codigo.data )

            periodo.descricao=titulo_form.descricao.data, 
            periodo.valor=titulo_form.valor.data, 
            periodo.vencimento=titulo_form.vencimento.data,
            periodo.status=titulo_form.status.data
        else:
            periodo = Periodo(
                descricao=titulo_form.descricao.data, 
                valor=titulo_form.valor.data, 
                vencimento=titulo_form.vencimento.data,
                status=titulo_form.status.data
            )

        periodo.save()

        flash('Titúlo salvo com sucesso!', 'success')

        return redirect(url_for('periodo.new'))

    print('Periodo errors: ' + str(titulo_form.errors))
    return render_template('periodos/new.html', periodo=titulo_form)

@periodo_bp.route('/edit/<int:titulo_id>')
def view(titulo_id):
    periodo = Periodo.query.get_or_404(titulo_id)
    titulo_form = PeriodoCreateForm()

    titulo_form.from_model(periodo)

    return render_template('periodos/new.html', periodo=titulo_form)

@periodo_bp.route('/delete/<int:titulo_id>', methods=['POST'])
def delete(titulo_id):
    periodo = Periodo.query.get_or_404(titulo_id)

    periodo.delete()

    return redirect(url_for('periodo.index'))