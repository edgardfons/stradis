import numpy as np
from scipy import optimize

def create_random_conflict_matrix(len):
  print("Hello from a function") 

# Creating the sets
num_days = 5
days_of_week = np.arange(num_days, dtype=int).tolist()
num_hours = 6
hours_of_day = np.arange(num_hours, dtype=int).tolist()
final_of_day = [1, 3, 5]
hours_days = ["M_AB", "M_CD", "A_AB", "A_CD", "N_AB", "N_CD"]

num_teachers = 10
teachers = np.arange(num_teachers, dtype=int).tolist()
num_terms = 9
terms = np.arange(num_terms, dtype=int).tolist()

num_events = 10
events = np.arange(num_events, dtype=int).tolist()


matrix = create_random_conflict_matrix(num_events)