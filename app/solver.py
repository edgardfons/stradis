import numpy as np
import re

from pulp import *
from time import perf_counter

from .models.grade import *

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
        return list( map(lambda dia: dia.name, self.days) )

    # Convert list of objects (Horario) to list of ints string (ids)
    def horarios(self):
        return list( map(lambda hora: str(hora.id), self.hours) )

    # Convert list of objects (Professor) to list of ints string (ids)
    def professores(self):
        return list( map(lambda prof: str(prof.id), self.teachers) )

    def etapas(self):
        return [str(i + 1) for i in range(self.terms)]

    def turmas(self):
        return list( map(lambda event: str(event.id), self.events) )

    def turmas_simples(self):
        # return list( map(lambda event: str(event.id), list(filter(lambda ev: not ev.geminada, self.events))) )
        return list( map(lambda event: str(event.id), self.events) )

    def turmas_professor(self):
        
        turm_prof = { prof:[] for prof in self.professores() }

        for event in self.events:
            turm_prof[str(event.professor_id)].append(str(event.id))

        return turm_prof

    def turmas_etapa(self):
        
        turm_etapa = { etapa:[] for etapa in self.etapas() }

        for event in self.events:
            turm_etapa[str(event.etapa)].append(str(event.id))
           
        return turm_etapa

    def turmas_disponibilidade(self):
        
        disp = [[ [1] * len(self.horarios()) for i in range(len(self.dias())) ] for j in range(len(self.events))]
        
        for event_index, event in enumerate(self.events):

            indis = list( map(lambda ind: (ind.dia.name, str(ind.horario_id)), event.indisponibilidade() ) )
            
            for day_index, day in enumerate(self.dias()):

                for hour_index, hour in enumerate(self.horarios()):
                    
                    if (day, hour) in indis:
                        disp[event_index][day_index][hour_index] = 0
              
        return disp

    def turmas_preagendadas(self):
        
        agend = [[ [0] * len(self.horarios()) for i in range(len(self.dias())) ] for j in range(len(self.events))]

        for event_index, event in enumerate(self.events):

            pre_agen = list( map(lambda ind: (str(ind.dia.name), str(ind.horario_id)),  event.pre_agendado() ) )

            for day_index, day in enumerate(self.dias()):

                for hour_index, hour in enumerate(self.horarios()):

                    if (day, hour) in pre_agen:
                        agend[event_index][day_index][hour_index] = 1

        return agend

    def turmas_conflitos(self):
        
        len_events = len(self.events)
        conflict = [ [0] * len_events for i in range(len_events)]        
        
        for j in range(len_events):

            ev2 = self.events[j]

            for i in range(j+1, len_events):
                
                ev1 = self.events[i]

                if ev1.etapa == ev2.etapa:
                    conflict[i][j] = 1
                

        return conflict

    def turmas_num(self):
        return [event.aulas_num for event in self.events]

def solve(conj):

    # Creating the sets
    days_of_week = conj.dias()
    hours_days = conj.horarios()

    teachers = conj.professores()
    terms = conj.etapas()

    events = conj.turmas()
    events_simples = conj.turmas_simples()
    events_number = conj.turmas_num()
    events_availability = conj.turmas_disponibilidade()
    events_pre_schedule = conj.turmas_preagendadas()
    events_conflict = conj.turmas_conflitos()

    # Adding model elemets
    teacher_events = conj.turmas_professor()
    term_events = conj.turmas_etapa()

    events_conflict = makeDict([events,events], events_conflict, 0)
    events_number = makeDict([events], events_number, 0)
    events_availability = makeDict([events,days_of_week,hours_days], events_availability, 0)
    events_pre_schedule = makeDict([events,days_of_week,hours_days], events_pre_schedule, 0)

    prob = LpProblem("UniversityCourseTimetabling", LpMinimize)

    # Váriaveis
    conflict = LpVariable.dicts("Conflicted", (events, events, days_of_week, hours_days), 0, 1, LpInteger)
    scheduled = LpVariable.dicts("Scheduled", (events, days_of_week, hours_days), 0, 1, LpInteger)
    pre_hour_scheduled = LpVariable.dicts("PreHourScheduled", (events, hours_days), 0, 1, LpInteger)
    term_min_day_hour_event = LpVariable.dicts("TermMinDayHourEvent", (terms, days_of_week, hours_days), 0, 1, LpInteger)
    idle_term_day_hour = LpVariable.dicts("IdleTermDayHour", (terms, days_of_week, hours_days), 0, 1, LpInteger)
    exceding_term_day_hour = LpVariable.dicts("ExcedingEventsTermDayHour", (terms, days_of_week, hours_days), 0, None, LpInteger)

    # Indexes auxiliares
    conflict_indexes = [ (e1, e2, d, h) for e1 in events for e2 in events if events.index(e1) > events.index(e2) and events_conflict[e1][e2] == 1 for d in days_of_week for h in hours_days ]
    scheduled_indexes = [ (e, d, h) for e in events for d in days_of_week for h in hours_days ]
    hour_day_indexes = [ (d, h) for d in days_of_week for h in hours_days ]
    teacher_hour_day = [ (t, d, h) for t in teachers for d in days_of_week for h in hours_days ]
    teacher_day = [ (t, d) for t in teachers for d in days_of_week ]
    events_simples_days_indexes = [ (es, d) for es in events_simples for d in days_of_week if days_of_week.index(d) < len(days_of_week) - 1]
    events_simples_days_indexes_2 = [ (es, d1, d2) for es in events_simples if events_number[es] == 2 for d1 in days_of_week for d2 in days_of_week if days_of_week.index(d2) >= days_of_week.index(d1) + 3]
    events_simples_hours = [ (es, h) for es in events_simples for h in hours_days ]
    term_days_hours = [ (t, d, h) for t in terms for d in days_of_week for h in hours_days ]
    term_days_hours_2 = [ (t, d, h1, h2, h3) for t in terms for d in days_of_week for h1 in hours_days for h2 in hours_days for h3 in hours_days if hours_days.index(h1) < hours_days.index(h2) and hours_days.index(h2) < hours_days.index(h3)]

    # Objective function
    prob += lpSum([EVENT_CONFLCT_WEIGHT*conflict[e1][e2][d][h]*events_conflict[e1][e2] for e1 in events for e2 in events if events.index(e1) > events.index(e2) for d in days_of_week for h in hours_days]) + lpSum([IDLE_CONFLICT_WEIGHT*idle_term_day_hour[t][d][h] for t in terms for d in days_of_week for h in hours_days]) + lpSum([EXCEDING_WEIGHT*exceding_term_day_hour[t][d][h] for t in terms for d in days_of_week for h in hours_days]), "Sum_to_avoid_conflicts_excedings_idles"

    # (1) x
    for e in events:
        prob += lpSum([scheduled[e][d][h] for (d, h) in hour_day_indexes]) == events_number[e], "Sum_num_event_%s_equals_to_%s" % (e, events_number[e])

    # (2) x
    for (e, d, h) in scheduled_indexes:
        prob += scheduled[e][d][h] <= events_availability[e][d][h], "Event_%s_is_available_in_%s_%s" % (e, d, h)

    # (3) x
    for (t, d, h) in teacher_hour_day:
        prob += lpSum([scheduled[et][d][h] for et in teacher_events[t]]) <= 1, "Teacher_%s_conflict_in_%s_event_at_%s_%s" % (t, teacher_events[t], d, h)
    
    # (5) x
    for (es, d) in events_simples_days_indexes:
        prob += lpSum( [ (scheduled[es][d][h] + scheduled[es][ days_of_week[ days_of_week.index(d) + 1 ] ][h]) for h in hours_days]) <= 1, "Event_%s_is_scheduled_%s_and_not_in_%s" % (es, d, days_of_week[ days_of_week.index(d) + 1 ])

    # (6) x
    for (es, d1, d2) in events_simples_days_indexes_2:
        prob += lpSum([ (scheduled[es][d1][h] + scheduled[es][d2][h]) for h in hours_days]) <= 1, "Event_%s_is_scheduled_%s_and_not_in_%s_or_after" % (es, d1, d2)

    # (7) x
    for (es, h) in events_simples_hours:
        prob += events_number[es] * pre_hour_scheduled[es][h] == lpSum([scheduled[es][d][h] for d in days_of_week]), "Event_%s_pre_scheduled_to_%s_in_day_%s" % (es, h, d)

    # (8) x
    for (t, d, h) in term_days_hours:
        for e in term_events[t]:
            prob += term_min_day_hour_event[t][d][h] >= scheduled[e][d][h], "Event_%s_is_scheduled_in_term_%s_at_%s_%s" % (e, t, d, h)

    # (9) x
    for (t, d, h) in term_days_hours:
        prob += term_min_day_hour_event[t][d][h] <= lpSum([scheduled[e][d][h] for e in term_events[t]]), "N_Events_are_scheduled_in_term_%s_at_%s_%s" % (t, d, h)

    # (10) x
    for (t, d, h1, h2, h3) in term_days_hours_2:
        prob += idle_term_day_hour[t][d][h2] >= term_min_day_hour_event[t][d][h1] + term_min_day_hour_event[t][d][h3] - term_min_day_hour_event[t][d][h2] - 1, "Idle_time_%s_%s_in_term_%s_between_%s_%s" % (d, h2, t, h1, h3)

    # (11) x
    for (e1, e2, d, h) in conflict_indexes:
        prob += scheduled[e1][d][h] + scheduled[e2][d][h] <= 1 + conflict[e1][e2][d][h], "Activating_conflict_in_events_%s_and_%s_day_%s_and_hour_%s" % (e1, e2, d, h) 

    # (12) x
    for (t, d, h) in term_days_hours:
        prob += lpSum([ scheduled[e][d][h] for e in term_events[t] ]) <= 2 + exceding_term_day_hour[t][d][h], "Two_more_Events_are_scheduled_in_term_%s_at_%s_%s" % (t, d, h) # Arbitrary

    # The problem data is written to an .lp file
    prob.writeLP("UniversityCouseTimetabling.lp")

    # Obter valores inteiros
    prob.roundSolution()

    t1_start = perf_counter() 
    # The problem is solved using PuLP's choice of Solver
    prob.solve(GLPK(msg = 0))

    t1_stop = perf_counter()

    print("Duração do processamento: %s segundos" % "{:3.2f}".format(t1_stop-t1_start) ) 


    if LpStatus[prob.status] != 'Optimal':
        print('Solução otima não encontrada.')


    return timetable( list(filter( lambda vari: vari.name.find("Scheduled") == 0 and vari.varValue != 0, prob.variables() )), conj )


def timetable(variables, conj):
 
    grade_entradas = []
    # scheduled = [[ [0] * len(conj.horarios()) for i in range(len(conj.dias())) ] for j in range(len(conj.turmas()))]

    for v in variables:
        regex = re.compile(r'Scheduled_(\d+)_(DOM|SEG|TER|QUA|QUI|SEX|SAB)_(\d+)')
        ids = regex.match(v.name)
        
        event_index = conj.turmas().index(ids.group(1))
        day_index = conj.dias().index(ids.group(2))
        hour_index = conj.horarios().index(ids.group(3))

        # scheduled[event_index][day_index][hour_index] = 1
        grade_entradas.append( 
            GradeTurma(
                dia=conj.days[day_index],
                periodo_id=conj.hours[hour_index].id,
                turma_id=conj.events[event_index].id
            )
         )

    return Grade(entradas=grade_entradas)

