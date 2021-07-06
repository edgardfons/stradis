from app import *
from solver import *

# Constants

NUM_PROFESSORES = 26
NUM_ETAPAS = 9
NUM_TURMAS = 31
NUM_DISCIPLINAS = 40

# Creating datatbase

ctx = app.app_context()
ctx.push()

db.drop_all()
db.create_all()

print('Banco de dados recriado')

# Adding parameters

print('Adicionando horas, professores, disciplinas e turmas')

db.session.add(Horario(nome='AB_M', inicio='07:30', fim='09:10', ordem=1))
db.session.add(Horario(nome='CD_M', inicio='09:20', fim='11:00', ordem=2, utlimo_dia=True))
db.session.add(Horario(nome='AB_T', inicio='13:20', fim='15:00', ordem=3))
db.session.add(Horario(nome='CD_T', inicio='15:10', fim='16:50', ordem=4, utlimo_dia=True))
db.session.add(Horario(nome='AB_N', inicio='18:30', fim='20:10', ordem=5))
db.session.add(Horario(nome='CD_N', inicio='20:20', fim='22:40', ordem=6, utlimo_dia=True))

db.session.commit()

print('Horários cadastrados!')

db.session.add(Professor(nome='ANA LUIZA BESSA DE PAULA BARROS'))
db.session.add(Professor(nome='ANDRE LUIZ MOURA DOS SANTOS'))
db.session.add(Professor(nome='FERNANDO ANTONIO RIVAS MAXIMUS DENIS'))
db.session.add(Professor(nome='FRANCISCO EDSON PINHEIRO PESSOA'))
db.session.add(Professor(nome='GERARDO VALDISIO RODRIGUES VIANA'))
db.session.add(Professor(nome='GUSTAVO AUGUSTO LIMA DE CAMPOS'))
db.session.add(Professor(nome='JERFFESON TEIXEIRA DE SOUZA'))
db.session.add(Professor(nome='JORGE LUIZ DE CASTRO E SILVA'))
db.session.add(Professor(nome='JOSE EVERARDO BESSA MAIA'))
db.session.add(Professor(nome='LEONARDO SAMPAIO ROCHA'))
db.session.add(Professor(nome='MARCIAL PORTO FERNANDEZ'))
db.session.add(Professor(nome='MARCOS JOSE NEGREIROS GOMES'))
db.session.add(Professor(nome='MARIA ELIZABETH SUCUPIRA FURTADO'))
db.session.add(Professor(nome='MARIELA INÉS CORTÉS'))
db.session.add(Professor(nome='PAULO HENRIQUE MENDES MAIA'))
db.session.add(Professor(nome='RAFAEL LOPES GOMES'))
db.session.add(Professor(nome='ALEXANDRE VIEIRA NETO'))
db.session.add(Professor(nome='FRANCISCO CESAR TEIXEIRA'))
db.session.add(Professor(nome='JOSE LEUDO MAIA'))
db.session.add(Professor(nome='JULIO CESAR GADELHA'))
db.session.add(Professor(nome='MARCUS ANTONIUS MELO DE LEOPOLDINO'))
db.session.add(Professor(nome='THELMO PONTES DE ARAÚJO'))

db.session.commit()

print('Professores cadastrados!')

db.session.add(Disciplina(nome='INTRODUÇÃO A COMPUTAÇÃO', codigo='CT-02'))
db.session.add(Disciplina(nome='MATEMÁTICA DISCRETA', codigo='CT-03'))
db.session.add(Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL I', codigo='CT-04'))
db.session.add(Disciplina(nome='GEOMETRIA ANALÍTICA', codigo='CT-05'))
db.session.add(Disciplina(nome='INGLÊS INSTRUMENTAL', codigo='CT-06'))
db.session.add(Disciplina(nome='COMUNICAÇÃO E EXPRESSÃO', codigo='CT-07'))

db.session.add(Disciplina(nome='PROGRAMAÇÃO ESTRUTURADA E ORIENTADA A OBJETO', codigo='CT-010'))
db.session.add(Disciplina(nome='CIRCUITOS LÓGICOS DIGITAIS', codigo='CT-011'))
db.session.add(Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL II', codigo='CT-04'))
db.session.add(Disciplina(nome='LÓGICA PARA COMPUTAÇÃO', codigo='CT-012'))
db.session.add(Disciplina(nome='ÁLGEBRA LINEAR PARA COMPUTAÇÃO', codigo='CT-013'))
db.session.add(Disciplina(nome='FÍSICA PARA COMPUTAÇÃO I', codigo='CT-014'))

db.session.add(Disciplina(nome='ESTRUTURA DE DADOS I', codigo='CT-017'))
db.session.add(Disciplina(nome='CONCEITOS DE LINGUAGEM DE PROGRAMAÇÃO', codigo='CT-018'))
db.session.add(Disciplina(nome='ARQUITETURA DE COMPUTADORES', codigo='CT-019'))
db.session.add(Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL III', codigo='CT-020'))
db.session.add(Disciplina(nome='PROBABILIDADE E ESTATÍSTICA', codigo='CT-021'))
db.session.add(Disciplina(nome='FÍSICA PARA COMPUTAÇÃO II', codigo='CT-014'))

db.session.add(Disciplina(nome='ESTRUTURA DE DADOS II', codigo='CT-024'))
db.session.add(Disciplina(nome='TEORIA DOS GRAFOS', codigo='CT-025'))
db.session.add(Disciplina(nome='INTERAÇÃO HUMANO COMPUTADOR', codigo='CT-026'))
db.session.add(Disciplina(nome='SISTEMAS OPERACIONAIS', codigo='CT-027'))
db.session.add(Disciplina(nome='CÁLCULO NUMÉRICO', codigo='CT-028'))
db.session.add(Disciplina(nome='AVALIAÇÃO DE DESEMPENHO', codigo='CT-029'))

db.session.add(Disciplina(nome='BANCO DE DADOS', codigo='CT-032'))
db.session.add(Disciplina(nome='ENGENHARIA DE SOFTWARE', codigo='CT-033'))
db.session.add(Disciplina(nome='TEORIA DOS AUTÔMATOS E LINGUAGENS FORMAIS', codigo='CT-034'))
db.session.add(Disciplina(nome='PROGRAMAÇÃO PARALELA E CONCORRENTE', codigo='CT-035'))
db.session.add(Disciplina(nome='REDE DE COMPUTADORES', codigo='CT-036'))
db.session.add(Disciplina(nome='INICIAÇÃO A PESQUISA CIÊNTIFICA', codigo='CT-037'))

db.session.add(Disciplina(nome='TEORIA DA COMPLEXIDADE', codigo='CT-040'))
db.session.add(Disciplina(nome='ANÁLISE DE PROJETO DE SOFTWARE', codigo='CT-041'))
db.session.add(Disciplina(nome='TEORIA DA COMPUTAÇÃO', codigo='CT-042'))
db.session.add(Disciplina(nome='COMPUTAÇÃO GRÁFICA', codigo='CT-043'))
db.session.add(Disciplina(nome='INTELIGÊNCIA COMPUTACIONAL', codigo='CT-044'))
db.session.add(Disciplina(nome='PROGRAMAÇÃO MATEMÁTICA', codigo='CT-045'))

db.session.add(Disciplina(nome='PROJETO E ANÁLISE DE ALGORITMOS', codigo='CT-048'))
db.session.add(Disciplina(nome='INFORMÁTICA NA SOCIEDADE E ÉTICA', codigo='CT-049'))
db.session.add(Disciplina(nome='COMPILADORES', codigo='CT-050'))

db.session.add(Disciplina(nome='PESQUISA EM COMPUTAÇÃO', codigo='CT-053'))
db.session.add(Disciplina(nome='ADMINISTRAÇÃO PARA COMPUTAÇÃO', codigo='CT-054'))

db.session.commit()

print('Disciplinas cadastrados!')

db.session.add(Campus(nome='ITAPERI'))
db.session.add(Campus(nome='BAIRRO DE FÁTIMA'))

db.session.commit()

print('Capus cadastrados!')


db.session.add(Turma(codigo='1515', aulas_num=3, disciplina_id=1, professor_id=1, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1516', aulas_num=2, disciplina_id=2, professor_id=21, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1517', aulas_num=2, disciplina_id=3, professor_id=20, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1518', aulas_num=2, disciplina_id=4, professor_id=21, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1519', aulas_num=2, disciplina_id=5, professor_id=19, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1520', aulas_num=2, disciplina_id=6, professor_id=17, etapa=1, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1521', aulas_num=3, disciplina_id=7, professor_id=15, etapa=2, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1522', aulas_num=2, disciplina_id=8, professor_id=19, etapa=2, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1523', aulas_num=2, disciplina_id=9, professor_id=6, etapa=2, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1524', aulas_num=2, disciplina_id=10, professor_id=22, etapa=2, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1525', aulas_num=2, disciplina_id=11, professor_id=21, etapa=2, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1526', aulas_num=2, disciplina_id=12, professor_id=10, etapa=2, campus_id=1, geminada=True, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1527', aulas_num=2, disciplina_id=13, professor_id=16, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1528', aulas_num=2, disciplina_id=14, professor_id=9, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1529', aulas_num=2, disciplina_id=15, professor_id=20, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1530', aulas_num=2, disciplina_id=16, professor_id=8, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1531', aulas_num=2, disciplina_id=17, professor_id=12, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1532', aulas_num=2, disciplina_id=18, professor_id=5, etapa=3, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1533', aulas_num=2, disciplina_id=19, professor_id=13, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1534', aulas_num=2, disciplina_id=20, professor_id=9, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1535', aulas_num=2, disciplina_id=21, professor_id=17, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1536', aulas_num=2, disciplina_id=22, professor_id=8, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1537', aulas_num=2, disciplina_id=23, professor_id=17, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1538', aulas_num=2, disciplina_id=24, professor_id=13, etapa=4, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1539', aulas_num=2, disciplina_id=25, professor_id=4, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1540', aulas_num=2, disciplina_id=26, professor_id=11, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1541', aulas_num=2, disciplina_id=27, professor_id=16, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1542', aulas_num=2, disciplina_id=28, professor_id=14, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1543', aulas_num=2, disciplina_id=29, professor_id=7, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1544', aulas_num=2, disciplina_id=30, professor_id=15, etapa=5, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1545', aulas_num=2, disciplina_id=31, professor_id=4, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1546', aulas_num=2, disciplina_id=32, professor_id=22, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1547', aulas_num=2, disciplina_id=33, professor_id=6, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1548', aulas_num=2, disciplina_id=34, professor_id=12, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1549', aulas_num=2, disciplina_id=35, professor_id=10, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1550', aulas_num=2, disciplina_id=36, professor_id=1, etapa=6, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1551', aulas_num=2, disciplina_id=37, professor_id=16, etapa=7, campus_id=1, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1552', aulas_num=2, disciplina_id=38, professor_id=14, etapa=7, campus_id=2, periodo_letivo=PeriodoLetivo.P_20202))
db.session.add(Turma(codigo='1553', aulas_num=2, disciplina_id=39, professor_id=3, etapa=8, campus_id=2, periodo_letivo=PeriodoLetivo.P_20202))

db.session.add(TurmaIndisponibilidade(turma_id=1, horario_id=3, dia=Dia.QUI))

db.session.add(TurmaPreAgendada(turma_id=8, horario_id=5, dia=Dia.QUA))


db.session.commit()

print('Turmas cadastrados!')

conj = Conjuntos(
    days=dias_padrao(), 
    hours=Horario.query.all(),
    teachers=Professor.query.all(),
    terms=NUM_ETAPAS,
    events=Turma.query.all()
)


grade = solve(conj)

grade.nome = 'Grade de teste da UECE'

db.session.add(grade)

db.session.commit()

print('Grade de teste UECE cadastrada!')

# Closing context
ctx.pop()
