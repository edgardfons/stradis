import numpy as np
from pulp import *


# Creating the sets
num_days = 5
days_of_week = "MON TUE WEND THU FRI".split()
num_hours = 6
hours_days = "M_AB M_CD A_AB A_CD N_AB N_CD".split()
final_of_day = "M_CD A_CD N_CD".split()

num_teachers = 10
teachers = "T0 T1 T2 T3 T4 T5 T6 T7 T8 T9".split()
num_terms = 4
terms = [0, 1, 2, 3]

num_events = 10
num_events_simples = 8
num_events_geminado = 2
events = "0 1 2 3 4 5 6 7 8 9".split()
events_simples = [0, 1, 3, 5, 6, 7, 8, 9]
events_geminados = [2, 4]

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
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
events_pre_schedule = makeDict([events,days_of_week,hours_days], events_pre_schedule, 0)

prob = LpProblem("UniversityCourseTimetabling", LpMinimize)

conflict = LpVariable.dicts("Conflicted", (events, events, days_of_week, hours_days), 0, 1, LpInteger)
scheduled = LpVariable.dicts("Scheduled", (events, days_of_week, hours_days), 0, 1, LpInteger)

conflict_indexes = [ (e1, e2, d, h) for e1 in events for e2 in events for d in days_of_week for h in hours_days ]
scheduled_indexes = [ (e1, d, h) for e1 in events for d in days_of_week for h in hours_days ]
hour_day_indexes = [ (d, h) for d in days_of_week for h in hours_days ]

# Objective function
prob += lpSum([envent_conflict_weight*conflict[e1][e2][d][h]*events_conflict[e1][e2] for (e1, e2, d, h) in conflict_indexes if e1 > e2]), "Sum_to_avoid_conflicts"

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

# (15)
for (e1, e2, d, h) in conflict_indexes:
  if e1 > e2 and events_conflict[e1][e2] == 1:
    prob += scheduled[e1][d][h] + scheduled[e2][d][h] <= 1 + conflict[e1][e2][d][h], "Activating_conflict_in_events_%s_and_%s_day_%s_and_hour_%s" % (e1, e2, d, h) 


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