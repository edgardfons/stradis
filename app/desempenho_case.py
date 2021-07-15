import random

from .models.periodo import Periodo, Dias
from .models.professor import Professor
from .models.disciplina import Disciplina
from .models.turma import Turma, TurmaConfig, Config
from .solver import *

from faker import Faker

fake = Faker('pt_BR')
# Adding parameters

PROF_TURMA_LIMIT = 2

def periodos():
    Periodo(nome='AB_M', inicio=730, fim=910).save()
    Periodo(nome='CD_M', inicio=920, fim=1100).save()
    Periodo(nome='AB_T', inicio=1320, fim=1500).save()
    Periodo(nome='CD_T', inicio=1510, fim=1650).save()
    Periodo(nome='AB_N', inicio=1830, fim=2010).save()
    Periodo(nome='CD_N', inicio=2020, fim=2240).save()

    print('Horários cadastrados!')

def professores(num):
    for i in range(num):
        Professor(nome=fake.name()).save()

    print(str(num) + ' professores cadastrados!')

def disciplinas(num):
    for i in range(num):
        Disciplina(nome='Disciplina-' + str(num+1)).save()

    print(str(num) + ' disciplinas cadastradas!')




def turmas_block():
    return [ TurmaConfig(dia=d, periodo_id=5, config=Config.INDISPONIVEL) for d in Dias.padroes() ] + [ TurmaConfig(dia=d, periodo_id=6, config=Config.INDISPONIVEL) for d in Dias.padroes() ]


def turmas(etapas):
    discs = Disciplina.query.all()
    discs_size = len(discs)
    discs_ids = list(map(lambda disc: disc.id, discs))
    discs_3_aulas = [ discs_ids[fake.random_int(0, discs_size-1)] for x in range(int(etapas / 2)) ]

    profs = Professor.query.all()
    profs_size = len(profs)
    profs_ids = list(map(lambda prof: prof.id, profs))
    profs_map = {prof.id: 0 for prof in profs}

    random.shuffle(discs)
    etapa = 1
 
    for disc in discs:

        prof_id = 0
        random.shuffle(profs_ids)

        if etapa > etapas:
            etapa = 1

        for candit in profs_ids:
            if profs_map[candit] < PROF_TURMA_LIMIT:
                prof_id = candit
                break
                
        Turma(codigo=str(fake.random_int(1000, 2000)),            
            disciplina_id=disc.id, 
            professor_id=prof_id, 
            aulas_num = 3 if disc.id in discs_3_aulas else 2, 
            etapa = etapa, 
            configs=[]).save()

        profs_map[prof_id] = profs_map[prof_id] + 1
        etapa = etapa + 1
            
    print('Turmas cadastradas!')

def gerar(num_professores, num_disciplinas, num_etapas):

    print('Divisão em ' + str(num_etapas) + ' etapas!')

    periodos()
    professores(num_professores)
    disciplinas(num_disciplinas)
    turmas(num_etapas)

    conj = Conjuntos(
        days=Dias.padroes(), 
        hours=Periodo.query.all(),
        teachers=Professor.query.all(),
        terms=num_etapas,
        events=Turma.query.all()
    )

    print('Computando solução!')

    grade = solve(conj)
    
    grade.semestre_letivo = '125'

    grade.save()

    print('Grade de teste UECE cadastrada!')