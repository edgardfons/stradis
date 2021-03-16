import numpy as np
from pulp import *


# Creating the sets
num_days = 5
days_of_week = "MON TUE WED THU FRI".split()
num_hours = 6
hours_days = "M_AB M_CD A_AB A_CD N_AB N_CD".split()
final_of_day = "M_CD A_CD N_CD".split()

num_teachers = 10
teachers = "T0 T1 T2 T3 T4 T5 T6 T7 T8 T9".split()
num_terms = 4
terms = "TR0 TR1 TR2 TR3".split()

num_events = 10
num_events_simples = 8
num_events_geminado = 2
events = "0 1 2 3 4 5 6 7 8 9".split()
events_simples = "0 1 3 5 6 7 8 9".split()
events_geminados = "2 4".split()

# num_teachers * num_events
events_teacher = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
]

# num_terms * num_events
events_terms = [
  [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

# Passing the parameter

envent_conflict_weight = 1000
idle_weight = 10
exceding_weight = 1

# num_events
events_number = [2, 2, 3, 2, 2, 1, 2, 2, 1, 2]

# num_events * num_days * num_hours
events_availability = [
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ],
  [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
  ]
]

# num_events * num_days * num_hours
events_pre_schedule = [
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
  ]
]

# num_events * num_events
events_conflict = [
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 8, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

# num_events * num_events
events_campus = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Adding model elemets

events_conflict = makeDict([events,events], events_conflict, 0)
events_number = makeDict([events], events_number, 0)
events_availability = makeDict([events,days_of_week,hours_days], events_availability, 0)
teacher_events = {
  "T0": ["0"],
  "T1": ["1"],
  "T2": ["2"],
  "T3": ["3"],
  "T4": ["4"],
  "T5": ["5"],
  "T6": ["6"],
  "T7": ["7"],
  "T8": ["8"],
  "T9": ["9"]
}
term_events = {
  "TR0": ["0", "5", "6"],
  "TR1": ["1", "8"],
  "TR2": ["2", "9"],
  "TR3": ["3", "4", "7"],
}
events_pre_schedule = makeDict([events,days_of_week,hours_days], events_pre_schedule, 0)
events_campus = makeDict([events,events], events_campus, 0)

prob = LpProblem("UniversityCourseTimetabling", LpMinimize)

# Varibles
conflict = LpVariable.dicts("Conflicted", (events, events, days_of_week, hours_days), 0, 1, LpInteger)
scheduled = LpVariable.dicts("Scheduled", (events, days_of_week, hours_days), 0, 1, LpInteger)
per_hour_scheduled = LpVariable.dicts("PreHourScheduled", (events, hours_days), 0, 1, LpInteger)
start_events_geminados_schedule = LpVariable.dicts("StarEventsGeminados", (events, days_of_week, hours_days), 0, 1, LpInteger)
term_min_day_hour_event = LpVariable.dicts("TermMinDayHourEvent", (terms, days_of_week, hours_days), 0, 1, LpInteger)
idle_temr_day_hour = LpVariable.dicts("IdleTermDayHour", (terms, days_of_week, hours_days), 0, 1, LpInteger)
exceding_temr_day_hour = LpVariable.dicts("ExcedingEventsTermDayHour", (terms, days_of_week, hours_days), 0, None, LpInteger)

# Aux indexes
conflict_indexes = [ (e1, e2, d, h) for e1 in events for e2 in events if events.index(e1) > events.index(e2) and events_conflict[e1][e2] == 1 for d in days_of_week for h in hours_days ]
scheduled_indexes = [ (e1, d, h) for e1 in events for d in days_of_week for h in hours_days ]
hour_day_indexes = [ (d, h) for d in days_of_week for h in hours_days ]
events_simples_days_indexes = [ (es, d) for es in events_simples for d in days_of_week if days_of_week.index(d) < len(days_of_week) - 1]
events_simples_days_indexes_2 = [ (es, d1, d2) for es in events_simples if events_number[es] == 2 for d1 in days_of_week for d2 in days_of_week if days_of_week.index(d2) >= days_of_week.index(d1) + 3]
events_simples_hours = [ (es, h) for es in events_simples for h in hours_days ]
events_geminados_days_hours_not_final = [ (eg, d, h) for eg in events_geminados for d in days_of_week for h in hours_days if h not in final_of_day ]
events_days_hours_campus = [ (e1, e2, d, h) for e1 in events for e2 in events if events.index(e1) > events.index(e2) and events_campus[e1][e2] > 0 for d in days_of_week for h in hours_days if h not in final_of_day ]
term_days_hours = [ (t, d, h) for t in terms for d in days_of_week for h in hours_days ]
term_days_hours_2 = [ (t, d, h1, h2, h3) for t in terms for d in days_of_week for h1 in hours_days for h2 in hours_days for h3 in hours_days if hours_days.index(h1) < hours_days.index(h2) and hours_days.index(h2) < hours_days.index(h3)]

# Objective function
prob += lpSum([envent_conflict_weight*conflict[e1][e2][d][h]*events_conflict[e1][e2] for e1 in events for e2 in events if events.index(e1) > events.index(e2) for d in days_of_week for h in hours_days]) + lpSum([idle_weight*idle_temr_day_hour[t][d][h] for t in terms for d in days_of_week for h in hours_days]) + lpSum([exceding_weight*exceding_temr_day_hour[t][d][h] for t in terms for d in days_of_week for h in hours_days]), "Sum_to_avoid_conflicts_excedings_idles"

# (1)
for e in events:
  prob += lpSum([scheduled[e][d][h] for (d, h) in hour_day_indexes]) == events_number[e], "Sum_num_event_%s_equals_to_%s" % (e, str(events_number[e]))

# (2)
for (e, d, h) in scheduled_indexes:
  prob += scheduled[e][d][h] <= events_availability[e][d][h], "Event_%s_is_available_in_%s_%s" % (e, d, h)

# (3)
for t in teacher_events:
  prob += lpSum([scheduled[et][d][h] for et in teacher_events[t] for (d, h) in hour_day_indexes]) <= 1, "Teacher_%s_conflict_in_%s_event_at_%s_%s" % (t, str(teacher_events[t]), d, h)

# (4)
for (e, d, h) in scheduled_indexes:
  prob += scheduled[e][d][h] >= events_pre_schedule[e][d][h], "Event_%s_is_pre_scheduled_in_%s_%s" % (e, d, h)

# (5)
for (es, d) in events_simples_days_indexes:
  prob += lpSum([scheduled[e][d][h] + scheduled[e][ days_of_week[ days_of_week.index(d) + 1 ] ][h] for h in hours_days]) <= 1, "Event_%s_is_scheduled_%s_and_not_in_%s" % (es, d, days_of_week[ days_of_week.index(d) + 1 ])

# (6)
for (es, d1, d2) in events_simples_days_indexes_2:
  prob += lpSum([scheduled[e][d1][h] + scheduled[e][d2][h] for h in hours_days]) <= 1, "Event_%s_is_scheduled_%s_and_not_in_%s_or_after" % (es, d1, d2)

# (7)
for (es, h) in events_simples_hours:
  prob += events_number[es] * per_hour_scheduled[es][h] == lpSum([scheduled[es][d][h] for d in days_of_week]), "Event_%s_pre_scheduled_to_%s_in_day_%s" % (es, h, d)

# (8)
for (eg, d, h) in events_geminados_days_hours_not_final:
  prob += start_events_geminados_schedule[eg][d][h] <= scheduled[eg][d][h], "Event_geminado_%s_starts_%s_at_%s" % (eg, h, d)

# (9)
for (eg, d, h) in events_geminados_days_hours_not_final:
  prob += start_events_geminados_schedule[eg][d][h] <= scheduled[eg][d][ hours_days[hours_days.index(h) + 1] ], "Event_geminado_%s_ends_%s_at_%s" % (eg, hours_days[hours_days.index(h) + 1], d)

# (10)
for eg in events_geminados:
  prob += lpSum( [start_events_geminados_schedule[eg][d][h] for d in days_of_week for h in hours_days if h not in final_of_day] ) == 1, "Event_geminado_%s_occours_only_once"%eg

# (11)
for (e1, e2, d, h) in events_days_hours_campus:
  prob += scheduled[e1][d][h] + scheduled[e2][d][h] <= 1, "Events_%s_and_%s_in_different_campus_at_%s_%s_not_sequential" % (e1, e2, d, h)

# (12)
for (t, d, h) in term_days_hours:
  for e in term_events[t]:
    prob += term_min_day_hour_event[t][d][h] >= scheduled[e][d][h], "Event_%s_is_scheduled_in_term_%s_at_%s_%s" % (e, t, d, h)

# (13)
for (t, d, h) in term_days_hours:
  prob += term_min_day_hour_event[t][d][h] <= lpSum([scheduled[e][d][h] for e in term_events[t]]), "N_Events_are_scheduled_in_term_%s_at_%s_%s" % (t, d, h)

# (14)
for (t, d, h1, h2, h3) in term_days_hours_2:
  prob += idle_temr_day_hour[t][d][h2] >= term_min_day_hour_event[t][d][h1] + term_min_day_hour_event[t][d][h3] - term_min_day_hour_event[t][d][h2] - 1

# (15)
for (e1, e2, d, h) in conflict_indexes:
  prob += scheduled[e1][d][h] + scheduled[e2][d][h] <= 1 + conflict[e1][e2][d][h], "Activating_conflict_in_events_%s_and_%s_day_%s_and_hour_%s" % (e1, e2, d, h) 

# (16)
for (t, d, h) in term_days_hours:
  prob += lpSum([ scheduled[e][d][h] for e in term_events[t] ]) <= 2 + exceding_temr_day_hour[t][d][h], "2+_Events_are_scheduled_in_term_%s_at_%s_%s" % (t, d, h) # Arbitrary


# The problem data is written to an .lp file
prob.writeLP("UniversityCouseTimetabling.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve(GLPK(msg = 0))

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
# for v in prob.variables():
#   print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen    
print( "Total undesirable value = ", value(prob.objective) )