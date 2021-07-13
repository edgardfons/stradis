from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.periodo import Periodo, PeriodoCreateForm, PeriodoIndexForm
from app.extensions import db
from app.utils import sql_date_format, sql_ilike_format, parse_date

PAGE = 1
PER_PAGE = 5
periodo_bp = Blueprint('periodo', __name__)

@periodo_bp.route('/', defaults={"page": 1}) 
@periodo_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = PER_PAGE

    periodo_form = PeriodoIndexForm()
    periodos = Periodo.query

    periodo_form.dia.data = request.args.get('dia')

    periodos = periodos.order_by(Periodo.id.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('periodos/index.html', periodos=periodos, periodo_form=periodo_form, periodo=PeriodoCreateForm(), prof_tab=True)

@periodo_bp.route('', methods=['POST'])
def new():
    print('Edgard esteve aqui!')
    periodo_form = PeriodoCreateForm()   

    if periodo_form.validate_on_submit():

        if periodo_form.id.data:
            periodo = Periodo.query.get_or_404( periodo_form.id.data )

            periodo.descricao=periodo_form.nome.data
        else:
            periodo = Periodo(
                dia=periodo_form.dia.data,
                inicio=periodo_form.inicio.data,
                fim=periodo_form.fim.data
            )

        periodo.save()

        flash('Periodo salvo com sucesso!', 'success')

        return redirect(url_for('periodo.index'))

    return render_template('periodos/index.html', periodo=periodo_form)

@periodo_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):

    periodo = Periodo.query.get_or_404( id )

    periodo_form = PeriodoIndexForm()
    periodos = Periodo.query.order_by(Periodo.id.desc()).paginate(PAGE, per_page=PER_PAGE, error_out=True)

    return render_template('periodos/index.html', periodos=periodos, periodo_form=periodo_form, periodo=PeriodoCreateForm(periodo), prof_tab=True)

@periodo_bp.route('/<int:id>', methods=['POST'])
def delete(id):

    periodo = Periodo.query.get_or_404( id )

    periodo.delete()

    flash('Periodo excluido com sucesso!', 'success')

    return redirect(url_for('periodo.index'))