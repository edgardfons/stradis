from flask import render_template, request, Blueprint, flash, redirect, url_for

from app.models.turma import Turma, TurmaCreateForm, TurmaIndexForm
from app.models.professor import Professor
from app.models.disciplina import Disciplina

PAGE = 1
PER_PAGE = 5
turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/', defaults={"page": 1}) 
@turma_bp.route('/<int:page>')
def index(page):
    page = page
    per_page = PER_PAGE

    turmas_form = TurmaIndexForm()
    turmas = Turma.query

    turma = TurmaCreateForm()
    turma.professor.choices = professores()
    turma.disciplina.choices = disciplinas()

    turmas = turmas.order_by(Turma.id.desc()).paginate(page, per_page=per_page, error_out=True)

    return render_template('turmas/index.html', turmas=turmas, turmas_form=turmas_form, turma=turma, turma_tab=True)

@turma_bp.route('/new', methods=['GET', 'POST'])
def new():
    titulo_form = TurmaCreateForm()   

    if titulo_form.validate_on_submit():

        if titulo_form.codigo.data:
            turma = Turma.query.get_or_404( titulo_form.codigo.data )

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

@turma_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    turma_db = Turma.query.get_or_404( id )
    turma = TurmaCreateForm()
    turma.professor.choices = professores()

    turma_form = TurmaIndexForm()
    turmas = Turma.query.order_by(Turma.id.desc()).paginate(PAGE, per_page=PER_PAGE, error_out=True)

    return render_template('turmas/index.html', turmas=turmas, turma_form=turma_form, turma=turma, turma_tab=True)

@turma_bp.route('/<int:id>', methods=['POST'])
def delete(id):
    turma = Turma.query.get_or_404( id )

    turma.delete()

    flash('Turma excluido com sucesso!', 'success')

    return redirect(url_for('turma.index'))


def professores():
    profs = Professor.query.all()
    return list( map(lambda prof: (prof.id, prof.nome), profs) )

def disciplinas():
    discs = Disciplina.query.all()
    return list( map(lambda disc: (disc.id, disc.nome), discs) )
