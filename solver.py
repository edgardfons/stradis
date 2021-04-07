'''

Testes do solver

1 teste: UECE
2 teste: Random generated 

'''
import numpy as np
from models import *


EVENT_CONFLCT_WEIGHT = 1000
IDLE_CONFLICT_WEIGHT = 100
EXCEDING_WEIGHT = 10

class Conjuntos:

    def __init__(self, days=None, hours=None, teachers=None, terms=None, events=None):
        self.days = days
        self.hours = hours
        self.teachers = teachers
        self.terms = terms
        self.events = events

    def dias(self):
        return list( map(lambda dia: str(dia.value), self.days) )

    # Convert list of objects (Horario) to list of ints string (ids)
    def horarios(self):
        return list( map(lambda hora: str(hora.id), self.hours) )

    # Convert list of objects (Professor) to list of ints string (ids)
    def professores(self):
        return list( map(lambda prof: str(prof.id), self.teachers) )

    def etapas(self):
        return [str(i) for i in range(self.terms)]

    def turmas(self):
        return list( map(lambda prof: str(prof.id), self.events) )

    def turmas_simples(self):
        return list( map(lambda prof: str(prof.id), list(filter(lambda ev: not ev.geminada, self.events))) )

    def turmas_geminados(self):
        return list( map(lambda prof: str(prof.id), list(filter(lambda ev: ev.geminada, self.events))) )

    def turmas_professor(self):
        return list( map(lambda prof: str(prof.id), list(filter(lambda ev: not ev.geminada, self.events))) )

    def turmas_geminados(self):
        return list( map(lambda prof: str(prof.id), list(filter(lambda ev: ev.geminada, self.events))) )

class Parametros:

    def __init__(self, dias, horarios, professores, etapas, eventos):
        self.dias = dias
        self.horarios = horarios
        self.professores = professores
        self.etapas = etapas
        self.eventos = eventos

    def dias(self):
        return self.dias

def dias_padrao():
    '''
        Retorna dias uteis representados pelo enum Dia
    '''
    exclu = Dia.DOM | Dia.SAB
    days = list( filter(lambda dia: dia not in exclu, list(Dia)) )

    return days


# Criar entradas e parametros
# Utilizar ids como identicadores a serem usados no solver
# exclu = Dia.DOM | Dia.SAB
# days = list( map(lambda dia: str(dia.value), list(filter(lambda dia: dia not in exclu, list(Dia)))) )

# hours = [ 
#     Horario(nome='AB_M'),
#     Horario(nome='CD_M', utlimo_dia=True),
#     Horario(nome='AB_T'), 
#     Horario(nome='CD_T', utlimo_dia=True),
#     Horario(nome='AB_N'),
#     Horario(nome='CD_N', utlimo_dia=True)
# ]
# final_hours = list(filter(lambda horario: horario.utlimo_dia, hours))

# hours = list( map(lambda hora: hora.nome, hours) )
# final_hours = list( map(lambda hora: hora.nome, final_hours) )

# 26 professores
# professores = [ Professor(nome="Prof_%s"%i) for i in range(NUM_PROFESSORES) ]
# professores = [ str(i) for i in range(NUM_PROFESSORES) ]

# 9 periodos letivos
# etapas = range(NUM_ETAPAS)
# etapas = [ str(i) for i in range(NUM_ETAPAS) ]

# 31 turmas (27 simples e 4 geminadas)
# events = [ str(i) for i in range(NUM_TURMAS) ]
# events_geminados = "4 5 9 14".split()
# events_simples = list( filter(lambda i: i not in events_geminados, events) )