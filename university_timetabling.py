import numpy as np
from scipy import optimize

def call_simplex(results):
  print(f'Rodando {results.nit}')


# Creating the sets
num_days = 5
days_of_week = [0, 1, 2, 3, 4]
num_hours = 6
hours_of_day = [0, 1, 2, 3, 4, 5]
final_of_day = [1, 3, 5]
hours_days = ["M_AB", "M_CD", "A_AB", "A_CD", "N_AB", "N_CD"]

num_teachers = 10
teachers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_terms = 4
terms = [0, 1, 2, 3]

num_events = 10
num_events_simples = 8
num_events_geminado = 2
events = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
  [0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
'''

MIN c'x

s.t

  A_ub * x <= b_ub
  A_eb * x <= b_eb
  l <= x <= u


'''

# Creating the upper bounds

num_scheduled = (num_events * num_days * num_hours)
num_enforce_schedule = (num_events * num_hours)
num_start_event_geminado = (num_events * num_days * num_hours) 
num_idle_periods = (num_terms * num_days * num_hours)
num_conflicts = (num_events * num_events * num_days * num_hours)
num_exits_term = (num_terms * num_days * num_hours)
num_exceding_upper_bounds = (num_terms * num_days * num_hours)

num_days_hours = num_days * num_hours

num_variables = ( 
  num_scheduled +
  num_enforce_schedule +
  num_start_event_geminado +
  num_idle_periods +
  num_conflicts + 
  num_exits_term
)

ones_bounds = [(0,1)] * num_variables

none_bounds = [(0,None)] * num_exceding_upper_bounds
num_variables += num_exceding_upper_bounds

bounds = np.concatenate( (np.array(ones_bounds), np.array(none_bounds)) ).tolist()

# Creating the C vector
'''

x' = [ x: |E|*|D|*|H| | f: |E|*|H| | g: |E|*|D|*|H| | -b: |M|*|D|*|H| | -c: |E|*|E|*|D|*|H| | y: |M|*|D|*|H| | -q: |M|*|D|*|H| ]

'''

first_zeros_num = num_scheduled + num_enforce_schedule + num_start_event_geminado

c_vector = np.concatenate( (

  np.zeros(first_zeros_num, dtype=int),
  np.full(num_idle_periods, idle_weight, dtype=int),
  np.array([ envent_conflict_weight * events_conflict[i][j] if i > j else 0 for h in range(num_hours) for d in range(num_days) for j in range(num_events) for i in range(num_events) ]),
  np.zeros(num_exits_term, dtype=int),
  np.full(num_exceding_upper_bounds, exceding_weight, dtype=int)

), dtype=int).tolist()

# print("c: ")
# print(c_vector)

# Contraints modeleing (equal bounding)
indexes_equal_bounds = []
res_equal_bounds = []


# (1)



indexes_equal_bounds = np.zeros((num_events, num_variables), dtype=int)
for a in range(num_events):
  for b in range(num_days_hours):
    indexes_equal_bounds[a][(num_days_hours * a) + b] = 1

res_equal_bounds = np.concatenate( (np.array(res_equal_bounds, dtype=int), np.array(events_number, dtype=int)), dtype=int)


# (7)

indexes_equal_bounds_aux = np.zeros((num_events_simples * num_hours, num_variables), dtype=int)

i = 0 # Matrix transversiong needs improving
for a in events_simples:
  for b in range(num_hours):

    j = num_scheduled + (a * num_hours) + b
    indexes_equal_bounds_aux[i][j] = events_number[a]

    # print(f'Number {events_number[a]} assign to postion f_{a}{b}')

    for d in range(num_days):
      w = (a * num_days * num_hours) + (d * num_hours) + b
      indexes_equal_bounds_aux[i][w] = -1
      # print(f'Number -1 assign to postion x_{a}{d}{b}')

    i = i + 1


res_equal_bounds = np.concatenate( (np.array(res_equal_bounds, dtype=int), np.zeros(num_events_simples * num_hours, dtype=int)), dtype=int)
indexes_equal_bounds = np.concatenate( (np.array(indexes_equal_bounds, dtype=int), indexes_equal_bounds_aux), dtype=int)

# (10)

indexes_equal_bounds_aux = np.zeros((num_events_geminado, num_variables), dtype=int)
i = 0
for a in events_geminados:
  for d in range(num_days):
    for h in range(num_hours):
      j = num_scheduled + num_enforce_schedule + (a * num_days * num_hours) + (d * num_hours) + h

      if h not in final_of_day:
        indexes_equal_bounds_aux[i][j] = 1
        # print(f'Number 1 assign to postion g_{a}{d}{h}')

  i = i + 1


res_equal_bounds = np.concatenate( (np.array(res_equal_bounds, dtype=int), np.ones(num_events_geminado, dtype=int)), dtype=int)
indexes_equal_bounds = np.concatenate( (np.array(indexes_equal_bounds, dtype=int), indexes_equal_bounds_aux), dtype=int)

# Contraints modeleing (unequal bounding)

indexes_unequal_bounds = []
res_unequal_bounds = []

# (2)

size = num_events * num_days * num_hours
indexes_unequal_bounds_aux = np.zeros((size, num_variables), dtype=int)
i = 0
for a in events_geminados:
  for d in range(num_days):
    for h in range(num_hours):
      j = num_scheduled + num_enforce_schedule + (a * num_days * num_hours) + (d * num_hours) + h

      if h not in final_of_day:
        indexes_equal_bounds_aux[i][j] = 1
        # print(f'Number 1 assign to postion x_{a}{d}{h}')

  i = i + 1

events_availability
res_unequal_bounds = np.concatenate( (np.array(res_unequal_bounds, dtype=int), np.ones(num_events_geminado, dtype=int)), dtype=int)
indexes_unequal_bounds = np.concatenate( (np.array(indexes_unequal_bounds, dtype=int), indexes_unequal_bounds_aux), dtype=int)



print("Numder of variables: " + str(len(c_vector)))

print("indexes_equal_bounds size: " + str(indexes_equal_bounds.shape))

print("res_equal_bounds size: " + str(res_equal_bounds.shape))

print("indexes_unequal_bounds size: " + str(indexes_unequal_bounds.shape))

print("res_unequal_bounds size: " + str(res_unequal_bounds.shape))


# Solve model and show simplified results
res = optimize.linprog(c_vector, A_eq=indexes_equal_bounds, b_eq=res_equal_bounds, bounds=bounds, method='simplex', callback=call_simplex)
print(res)




