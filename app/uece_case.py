from .models.periodo import Periodo, Dias
from .models.professor import Professor
from .models.disciplina import Disciplina
from .models.turma import Turma, TurmaConfig, Config
from app.models.instituicao import Instituicao
from .solver import *

# Constants

NUM_PROFESSORES = 26
NUM_ETAPAS = 9
NUM_TURMAS = 31
NUM_DISCIPLINAS = 40

# Adding parameters

def instituicao():
    instituicao = Instituicao()
    instituicao.save()

    return instituicao
    
def periodos(inst):
    Periodo(nome='AB_M', inicio=730, fim=910, instituicao_id=inst.id).save()
    Periodo(nome='CD_M', inicio=920, fim=1100, instituicao_id=inst.id).save()
    Periodo(nome='AB_T', inicio=1320, fim=1500, instituicao_id=inst.id).save()
    Periodo(nome='CD_T', inicio=1510, fim=1650, instituicao_id=inst.id).save()
    Periodo(nome='AB_N', inicio=1830, fim=2010, instituicao_id=inst.id).save()
    Periodo(nome='CD_N', inicio=2020, fim=2240, instituicao_id=inst.id).save()

    print('Horários cadastrados!')

def professores(inst):
    Professor(nome='ANA LUIZA BESSA DE PAULA BARROS', instituicao_id=inst.id).save()
    Professor(nome='ANDRE LUIZ MOURA DOS SANTOS', instituicao_id=inst.id).save()
    Professor(nome='FERNANDO ANTONIO RIVAS MAXIMUS DENIS', instituicao_id=inst.id).save()
    Professor(nome='FRANCISCO EDSON PINHEIRO PESSOA', instituicao_id=inst.id).save()
    Professor(nome='GERARDO VALDISIO RODRIGUES VIANA', instituicao_id=inst.id).save()
    Professor(nome='GUSTAVO AUGUSTO LIMA DE CAMPOS', instituicao_id=inst.id).save()
    Professor(nome='JERFFESON TEIXEIRA DE SOUZA', instituicao_id=inst.id).save()
    Professor(nome='JORGE LUIZ DE CASTRO E SILVA', instituicao_id=inst.id).save()
    Professor(nome='JOSE EVERARDO BESSA MAIA', instituicao_id=inst.id).save()
    Professor(nome='LEONARDO SAMPAIO ROCHA', instituicao_id=inst.id).save()
    Professor(nome='MARCIAL PORTO FERNANDEZ', instituicao_id=inst.id).save()
    Professor(nome='MARCOS JOSE NEGREIROS GOMES', instituicao_id=inst.id).save()
    Professor(nome='MARIA ELIZABETH SUCUPIRA FURTADO', instituicao_id=inst.id).save()
    Professor(nome='MARIELA INÉS CORTÉS', instituicao_id=inst.id).save()
    Professor(nome='PAULO HENRIQUE MENDES MAIA', instituicao_id=inst.id).save()
    Professor(nome='RAFAEL LOPES GOMES', instituicao_id=inst.id).save()
    Professor(nome='ALEXANDRE VIEIRA NETO', instituicao_id=inst.id).save()
    Professor(nome='FRANCISCO CESAR TEIXEIRA', instituicao_id=inst.id).save()
    Professor(nome='JOSE LEUDO MAIA', instituicao_id=inst.id).save()
    Professor(nome='JULIO CESAR GADELHA', instituicao_id=inst.id).save()
    Professor(nome='MARCUS ANTONIUS MELO DE LEOPOLDINO', instituicao_id=inst.id).save()
    Professor(nome='THELMO PONTES DE ARAÚJO', instituicao_id=inst.id).save()

    print('Professores cadastrados!')

def disciplinas(inst):
    Disciplina(nome='INTRODUÇÃO A COMPUTAÇÃO', codigo='CT-02', instituicao_id=inst.id).save()
    Disciplina(nome='MATEMÁTICA DISCRETA', codigo='CT-03', instituicao_id=inst.id).save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL I', codigo='CT-04', instituicao_id=inst.id).save()
    Disciplina(nome='GEOMETRIA ANALÍTICA', codigo='CT-05', instituicao_id=inst.id).save()
    Disciplina(nome='INGLÊS INSTRUMENTAL', codigo='CT-06', instituicao_id=inst.id).save()
    Disciplina(nome='COMUNICAÇÃO E EXPRESSÃO', codigo='CT-07', instituicao_id=inst.id).save()

    Disciplina(nome='PROGRAMAÇÃO ESTRUTURADA E ORIENTADA A OBJETO', codigo='CT-010', instituicao_id=inst.id).save()
    Disciplina(nome='CIRCUITOS LÓGICOS DIGITAIS', codigo='CT-011', instituicao_id=inst.id).save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL II', codigo='CT-012', instituicao_id=inst.id).save()
    Disciplina(nome='LÓGICA PARA COMPUTAÇÃO', codigo='CT-013', instituicao_id=inst.id).save()
    Disciplina(nome='ÁLGEBRA LINEAR PARA COMPUTAÇÃO', codigo='CT-014', instituicao_id=inst.id).save()
    Disciplina(nome='FÍSICA PARA COMPUTAÇÃO I', codigo='CT-015', instituicao_id=inst.id).save()

    Disciplina(nome='ESTRUTURA DE DADOS I', codigo='CT-017', instituicao_id=inst.id).save()
    Disciplina(nome='CONCEITOS DE LINGUAGEM DE PROGRAMAÇÃO', codigo='CT-018', instituicao_id=inst.id).save()
    Disciplina(nome='ARQUITETURA DE COMPUTADORES', codigo='CT-019', instituicao_id=inst.id).save()
    Disciplina(nome='CÁLCULO DIFERENCIAL E INTEGRAL III', codigo='CT-020', instituicao_id=inst.id).save()
    Disciplina(nome='PROBABILIDADE E ESTATÍSTICA', codigo='CT-021', instituicao_id=inst.id).save()
    Disciplina(nome='FÍSICA PARA COMPUTAÇÃO II', codigo='CT-023', instituicao_id=inst.id).save()

    Disciplina(nome='ESTRUTURA DE DADOS II', codigo='CT-024', instituicao_id=inst.id).save()
    Disciplina(nome='TEORIA DOS GRAFOS', codigo='CT-025', instituicao_id=inst.id).save()
    Disciplina(nome='INTERAÇÃO HUMANO COMPUTADOR', codigo='CT-026', instituicao_id=inst.id).save()
    Disciplina(nome='SISTEMAS OPERACIONAIS', codigo='CT-027', instituicao_id=inst.id).save()
    Disciplina(nome='CÁLCULO NUMÉRICO', codigo='CT-028', instituicao_id=inst.id).save()
    Disciplina(nome='AVALIAÇÃO DE DESEMPENHO', codigo='CT-029', instituicao_id=inst.id).save()

    Disciplina(nome='BANCO DE DADOS', codigo='CT-032', instituicao_id=inst.id).save()
    Disciplina(nome='ENGENHARIA DE SOFTWARE', codigo='CT-033', instituicao_id=inst.id).save()
    Disciplina(nome='TEORIA DOS AUTÔMATOS E LINGUAGENS FORMAIS', codigo='CT-034', instituicao_id=inst.id).save()
    Disciplina(nome='PROGRAMAÇÃO PARALELA E CONCORRENTE', codigo='CT-035', instituicao_id=inst.id).save()
    Disciplina(nome='REDE DE COMPUTADORES', codigo='CT-036', instituicao_id=inst.id).save()
    Disciplina(nome='INICIAÇÃO A PESQUISA CIÊNTIFICA', codigo='CT-037', instituicao_id=inst.id).save()

    Disciplina(nome='TEORIA DA COMPLEXIDADE', codigo='CT-040', instituicao_id=inst.id).save()
    Disciplina(nome='ANÁLISE DE PROJETO DE SOFTWARE', codigo='CT-041', instituicao_id=inst.id).save()
    Disciplina(nome='TEORIA DA COMPUTAÇÃO', codigo='CT-042', instituicao_id=inst.id).save()
    Disciplina(nome='COMPUTAÇÃO GRÁFICA', codigo='CT-043', instituicao_id=inst.id).save()
    Disciplina(nome='INTELIGÊNCIA COMPUTACIONAL', codigo='CT-044', instituicao_id=inst.id).save()
    Disciplina(nome='PROGRAMAÇÃO MATEMÁTICA', codigo='CT-045', instituicao_id=inst.id).save()

    Disciplina(nome='PROJETO E ANÁLISE DE ALGORITMOS', codigo='CT-048', instituicao_id=inst.id).save()
    Disciplina(nome='INFORMÁTICA NA SOCIEDADE E ÉTICA', codigo='CT-049', instituicao_id=inst.id).save()
    Disciplina(nome='COMPILADORES', codigo='CT-050', instituicao_id=inst.id).save()

    Disciplina(nome='PESQUISA EM COMPUTAÇÃO', codigo='CT-053', instituicao_id=inst.id).save()
    Disciplina(nome='ADMINISTRAÇÃO PARA COMPUTAÇÃO', codigo='CT-054', instituicao_id=inst.id).save()

def turmas_block(inst):
    horarios = Periodo.query.filter_by(instituicao_id=inst.id).order_by(Periodo.id).all()
    return [ TurmaConfig(dia=d, periodo_id=horarios[4].id, config=Config.INDISPONIVEL) for d in Dias.padroes() ] + [ TurmaConfig(dia=d, periodo_id=horarios[5].id, config=Config.INDISPONIVEL) for d in Dias.padroes() ]

def turmas(inst):

    professores = Professor.query.filter_by(instituicao_id=inst.id).order_by(Professor.id).all()
    disciplinas = Disciplina.query.filter_by(instituicao_id=inst.id).order_by(Disciplina.id).all()

    Turma(codigo='1515', aulas_num=3, disciplina_id=disciplinas[0].id, professor_id=professores[0].id, etapa=1, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1516', aulas_num=2, disciplina_id=disciplinas[1].id, professor_id=professores[20].id, etapa=1, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1517', aulas_num=2, disciplina_id=disciplinas[2].id, professor_id=professores[19].id, etapa=1, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1518', aulas_num=2, disciplina_id=disciplinas[3].id, professor_id=professores[20].id, etapa=1, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1519', aulas_num=2, disciplina_id=disciplinas[4].id, professor_id=professores[18].id, etapa=9, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1520', aulas_num=2, disciplina_id=disciplinas[5].id, professor_id=professores[16].id, etapa=1, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1521', aulas_num=3, disciplina_id=disciplinas[6].id, professor_id=professores[14].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1522', aulas_num=2, disciplina_id=disciplinas[7].id, professor_id=professores[18].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1523', aulas_num=2, disciplina_id=disciplinas[8].id, professor_id=professores[5].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1524', aulas_num=2, disciplina_id=disciplinas[9].id, professor_id=professores[21].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1525', aulas_num=2, disciplina_id=disciplinas[10].id, professor_id=professores[20].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1526', aulas_num=2, disciplina_id=disciplinas[11].id, professor_id=professores[9].id, etapa=2, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1527', aulas_num=2, disciplina_id=disciplinas[12].id, professor_id=professores[15].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1528', aulas_num=2, disciplina_id=disciplinas[13].id, professor_id=professores[8].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1529', aulas_num=2, disciplina_id=disciplinas[14].id, professor_id=professores[19].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1530', aulas_num=2, disciplina_id=disciplinas[15].id, professor_id=professores[7].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1531', aulas_num=2, disciplina_id=disciplinas[16].id, professor_id=professores[11].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1532', aulas_num=2, disciplina_id=disciplinas[17].id, professor_id=professores[4].id, etapa=3, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1533', aulas_num=2, disciplina_id=disciplinas[18].id, professor_id=professores[12].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1534', aulas_num=2, disciplina_id=disciplinas[19].id, professor_id=professores[8].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1535', aulas_num=2, disciplina_id=disciplinas[20].id, professor_id=professores[16].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1536', aulas_num=2, disciplina_id=disciplinas[21].id, professor_id=professores[7].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1537', aulas_num=2, disciplina_id=disciplinas[22].id, professor_id=professores[16].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1538', aulas_num=2, disciplina_id=disciplinas[23].id, professor_id=professores[12].id, etapa=4, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1539', aulas_num=2, disciplina_id=disciplinas[24].id, professor_id=professores[3].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1540', aulas_num=2, disciplina_id=disciplinas[25].id, professor_id=professores[10].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1541', aulas_num=2, disciplina_id=disciplinas[26].id, professor_id=professores[15].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1542', aulas_num=2, disciplina_id=disciplinas[27].id, professor_id=professores[13].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1543', aulas_num=2, disciplina_id=disciplinas[28].id, professor_id=professores[6].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1544', aulas_num=2, disciplina_id=disciplinas[29].id, professor_id=professores[14].id, etapa=5, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1545', aulas_num=2, disciplina_id=disciplinas[30].id, professor_id=professores[3].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1546', aulas_num=2, disciplina_id=disciplinas[31].id, professor_id=professores[21].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1547', aulas_num=2, disciplina_id=disciplinas[32].id, professor_id=professores[5].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1548', aulas_num=2, disciplina_id=disciplinas[33].id, professor_id=professores[11].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1549', aulas_num=2, disciplina_id=disciplinas[34].id, professor_id=professores[9].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1550', aulas_num=2, disciplina_id=disciplinas[35].id, professor_id=professores[0].id, etapa=6, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1551', aulas_num=2, disciplina_id=disciplinas[36].id, professor_id=professores[15].id, etapa=7, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1552', aulas_num=2, disciplina_id=disciplinas[37].id, professor_id=professores[13].id, etapa=7, configs=turmas_block(inst), instituicao_id=inst.id).save()
    Turma(codigo='1553', aulas_num=2, disciplina_id=disciplinas[38].id, professor_id=professores[2].id, etapa=8, configs=turmas_block(inst), instituicao_id=inst.id).save()

    print('Turmas cadastrados!')

def gerar():

    inst = instituicao()
    periodos(inst)
    professores(inst)

    disciplinas(inst)
    turmas(inst)
    conj = Conjuntos(
        days=Dias.padroes(), 
        hours=Periodo.query.filter_by(instituicao_id=inst.id).all(),
        teachers=Professor.query.filter_by(instituicao_id=inst.id).all(),
        terms=NUM_ETAPAS,
        events=Turma.query.filter_by(instituicao_id=inst.id).all()
    )


    grade = solve(conj)
    
    grade.semestre_letivo = '20202'
    grade.instituicao_id = inst.id

    grade.save()

    print('Grade de teste UECE cadastrada!')