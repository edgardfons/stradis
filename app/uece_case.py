from .models.periodo import Periodo, Dias
from .models.professor import Professor
from .models.disciplina import Disciplina
from .models.turma import Turma, TurmaConfig, Config
from .solver import *

# Constants

NUM_PROFESSORES = 26
NUM_ETAPAS = 9
NUM_TURMAS = 31
NUM_DISCIPLINAS = 40

# Adding parameters

def periodos():
    Periodo(nome='AB_M', inicio=730, fim=910).save()
    Periodo(nome='CD_M', inicio=920, fim=1100).save()
    Periodo(nome='AB_T', inicio=1320, fim=1500).save()
    Periodo(nome='CD_T', inicio=1510, fim=1650).save()
    Periodo(nome='AB_N', inicio=1830, fim=2010).save()
    Periodo(nome='CD_N', inicio=2020, fim=2240).save()

    print('Horários cadastrados!')

def professores():
    Professor(nome='ANA LUIZA BESSA DE PAULA BARROS').save()
    Professor(nome='ANDRE LUIZ MOURA DOS SANTOS').save()
    Professor(nome='FERNANDO ANTONIO RIVAS MAXIMUS DENIS').save()
    Professor(nome='FRANCISCO EDSON PINHEIRO PESSOA').save()
    Professor(nome='GERARDO VALDISIO RODRIGUES VIANA').save()
    Professor(nome='GUSTAVO AUGUSTO LIMA DE CAMPOS').save()
    Professor(nome='JERFFESON TEIXEIRA DE SOUZA').save()
    Professor(nome='JORGE LUIZ DE CASTRO E SILVA').save()
    Professor(nome='JOSE EVERARDO BESSA MAIA').save()
    Professor(nome='LEONARDO SAMPAIO ROCHA').save()
    Professor(nome='MARCIAL PORTO FERNANDEZ').save()
    Professor(nome='MARCOS JOSE NEGREIROS GOMES').save()
    Professor(nome='MARIA ELIZABETH SUCUPIRA FURTADO').save()
    Professor(nome='MARIELA INÉS CORTÉS').save()
    Professor(nome='PAULO HENRIQUE MENDES MAIA').save()
    Professor(nome='RAFAEL LOPES GOMES').save()
    Professor(nome='ALEXANDRE VIEIRA NETO').save()
    Professor(nome='FRANCISCO CESAR TEIXEIRA').save()
    Professor(nome='JOSE LEUDO MAIA').save()
    Professor(nome='JULIO CESAR GADELHA').save()
    Professor(nome='MARCUS ANTONIUS MELO DE LEOPOLDINO').save()
    Professor(nome='THELMO PONTES DE ARAÚJO').save()

    print('Professores cadastrados!')

def disciplinas():
    Disciplina(nome='INTRODUÇÃO A COMPUTAÇÃO', codigo='CT-02').save()
    Disciplina(nome='MATEMÁTICA DISCRETA', codigo='CT-03').save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL I', codigo='CT-04').save()
    Disciplina(nome='GEOMETRIA ANALÍTICA', codigo='CT-05').save()
    Disciplina(nome='INGLÊS INSTRUMENTAL', codigo='CT-06').save()
    Disciplina(nome='COMUNICAÇÃO E EXPRESSÃO', codigo='CT-07').save()

    Disciplina(nome='PROGRAMAÇÃO ESTRUTURADA E ORIENTADA A OBJETO', codigo='CT-010').save()
    Disciplina(nome='CIRCUITOS LÓGICOS DIGITAIS', codigo='CT-011').save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL II', codigo='CT-04').save()
    Disciplina(nome='LÓGICA PARA COMPUTAÇÃO', codigo='CT-012').save()
    Disciplina(nome='ÁLGEBRA LINEAR PARA COMPUTAÇÃO', codigo='CT-013').save()
    Disciplina(nome='FÍSICA PARA COMPUTAÇÃO I', codigo='CT-014').save()

    Disciplina(nome='ESTRUTURA DE DADOS I', codigo='CT-017').save()
    Disciplina(nome='CONCEITOS DE LINGUAGEM DE PROGRAMAÇÃO', codigo='CT-018').save()
    Disciplina(nome='ARQUITETURA DE COMPUTADORES', codigo='CT-019').save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL III', codigo='CT-020').save()
    Disciplina(nome='PROBABILIDADE E ESTATÍSTICA', codigo='CT-021').save()
    Disciplina(nome='FÍSICA PARA COMPUTAÇÃO II', codigo='CT-014').save()

    Disciplina(nome='ESTRUTURA DE DADOS II', codigo='CT-024').save()
    Disciplina(nome='TEORIA DOS GRAFOS', codigo='CT-025').save()
    Disciplina(nome='INTERAÇÃO HUMANO COMPUTADOR', codigo='CT-026').save()
    Disciplina(nome='SISTEMAS OPERACIONAIS', codigo='CT-027').save()
    Disciplina(nome='CÁLCULO NUMÉRICO', codigo='CT-028').save()
    Disciplina(nome='AVALIAÇÃO DE DESEMPENHO', codigo='CT-029').save()

    Disciplina(nome='BANCO DE DADOS', codigo='CT-032').save()
    Disciplina(nome='ENGENHARIA DE SOFTWARE', codigo='CT-033').save()
    Disciplina(nome='TEORIA DOS AUTÔMATOS E LINGUAGENS FORMAIS', codigo='CT-034').save()
    Disciplina(nome='PROGRAMAÇÃO PARALELA E CONCORRENTE', codigo='CT-035').save()
    Disciplina(nome='REDE DE COMPUTADORES', codigo='CT-036').save()
    Disciplina(nome='INICIAÇÃO A PESQUISA CIÊNTIFICA', codigo='CT-037').save()

    Disciplina(nome='TEORIA DA COMPLEXIDADE', codigo='CT-040').save()
    Disciplina(nome='ANÁLISE DE PROJETO DE SOFTWARE', codigo='CT-041').save()
    Disciplina(nome='TEORIA DA COMPUTAÇÃO', codigo='CT-042').save()
    Disciplina(nome='COMPUTAÇÃO GRÁFICA', codigo='CT-043').save()
    Disciplina(nome='INTELIGÊNCIA COMPUTACIONAL', codigo='CT-044').save()
    Disciplina(nome='PROGRAMAÇÃO MATEMÁTICA', codigo='CT-045').save()

    Disciplina(nome='PROJETO E ANÁLISE DE ALGORITMOS', codigo='CT-048').save()
    Disciplina(nome='INFORMÁTICA NA SOCIEDADE E ÉTICA', codigo='CT-049').save()
    Disciplina(nome='COMPILADORES', codigo='CT-050').save()

    Disciplina(nome='PESQUISA EM COMPUTAÇÃO', codigo='CT-053').save()
    Disciplina(nome='ADMINISTRAÇÃO PARA COMPUTAÇÃO', codigo='CT-054').save()

def turmas():
    Turma(codigo='1515', aulas_num=3, disciplina_id=1, professor_id=1, etapa=1, 
        configs=[ TurmaConfig(dia=Dias.SEG,periodo_id=1,config=Config.INDISPONIVEL),TurmaConfig(dia=Dias.SEG,periodo_id=2,config=Config.INDISPONIVEL) ]).save()
    Turma(codigo='1516', aulas_num=2, disciplina_id=2, professor_id=21, etapa=1).save()
    Turma(codigo='1517', aulas_num=2, disciplina_id=3, professor_id=20, etapa=1).save()
    Turma(codigo='1518', aulas_num=2, disciplina_id=4, professor_id=21, etapa=1).save()
    Turma(codigo='1519', aulas_num=2, disciplina_id=5, professor_id=19, etapa=1).save()
    Turma(codigo='1520', aulas_num=2, disciplina_id=6, professor_id=17, etapa=1).save()
    Turma(codigo='1521', aulas_num=3, disciplina_id=7, professor_id=15, etapa=2).save()
    Turma(codigo='1522', aulas_num=2, disciplina_id=8, professor_id=19, etapa=2).save()
    Turma(codigo='1523', aulas_num=2, disciplina_id=9, professor_id=6, etapa=2).save()
    Turma(codigo='1524', aulas_num=2, disciplina_id=10, professor_id=22, etapa=2).save()
    Turma(codigo='1525', aulas_num=2, disciplina_id=11, professor_id=21, etapa=2).save()
    Turma(codigo='1526', aulas_num=2, disciplina_id=12, professor_id=10, etapa=2).save()
    Turma(codigo='1527', aulas_num=2, disciplina_id=13, professor_id=16, etapa=3).save()
    Turma(codigo='1528', aulas_num=2, disciplina_id=14, professor_id=9, etapa=3).save()
    Turma(codigo='1529', aulas_num=2, disciplina_id=15, professor_id=20, etapa=3).save()
    Turma(codigo='1530', aulas_num=2, disciplina_id=16, professor_id=8, etapa=3).save()
    Turma(codigo='1531', aulas_num=2, disciplina_id=17, professor_id=12, etapa=3).save()
    Turma(codigo='1532', aulas_num=2, disciplina_id=18, professor_id=5, etapa=3).save()
    Turma(codigo='1533', aulas_num=2, disciplina_id=19, professor_id=13, etapa=4).save()
    Turma(codigo='1534', aulas_num=2, disciplina_id=20, professor_id=9, etapa=4).save()
    Turma(codigo='1535', aulas_num=2, disciplina_id=21, professor_id=17, etapa=4).save()
    Turma(codigo='1536', aulas_num=2, disciplina_id=22, professor_id=8, etapa=4).save()
    Turma(codigo='1537', aulas_num=2, disciplina_id=23, professor_id=17, etapa=4).save()
    Turma(codigo='1538', aulas_num=2, disciplina_id=24, professor_id=13, etapa=4).save()
    Turma(codigo='1539', aulas_num=2, disciplina_id=25, professor_id=4, etapa=5).save()
    Turma(codigo='1540', aulas_num=2, disciplina_id=26, professor_id=11, etapa=5).save()
    Turma(codigo='1541', aulas_num=2, disciplina_id=27, professor_id=16, etapa=5).save()
    Turma(codigo='1542', aulas_num=2, disciplina_id=28, professor_id=14, etapa=5).save()
    Turma(codigo='1543', aulas_num=2, disciplina_id=29, professor_id=7, etapa=5).save()
    Turma(codigo='1544', aulas_num=2, disciplina_id=30, professor_id=15, etapa=5).save()
    Turma(codigo='1545', aulas_num=2, disciplina_id=31, professor_id=4, etapa=6).save()
    Turma(codigo='1546', aulas_num=2, disciplina_id=32, professor_id=22, etapa=6).save()
    Turma(codigo='1547', aulas_num=2, disciplina_id=33, professor_id=6, etapa=6).save()
    Turma(codigo='1548', aulas_num=2, disciplina_id=34, professor_id=12, etapa=6).save()
    Turma(codigo='1549', aulas_num=2, disciplina_id=35, professor_id=10, etapa=6).save()
    Turma(codigo='1550', aulas_num=2, disciplina_id=36, professor_id=1, etapa=6).save()
    Turma(codigo='1551', aulas_num=2, disciplina_id=37, professor_id=16, etapa=7).save()
    Turma(codigo='1552', aulas_num=2, disciplina_id=38, professor_id=14, etapa=7).save()
    Turma(codigo='1553', aulas_num=2, disciplina_id=39, professor_id=3, etapa=8).save()

# TurmaIndisponibilidade(turma_id=1, horario_id=3, dia=Dia.QUI))

# TurmaPreAgendada(turma_id=8, horario_id=5, dia=Dia.QUA))

    print('Turmas cadastrados!')

def gerar():

    periodos()
    professores()

    disciplinas()
    turmas()
    conj = Conjuntos(
        days=Dias.padroes(), 
        hours=Periodo.query.all(),
        teachers=Professor.query.all(),
        terms=NUM_ETAPAS,
        events=Turma.query.all()
    )


    grade = solve(conj)
    
    grade.semestre_letivo = '20202'
    grade.save()

    print('Grade de teste UECE cadastrada!')