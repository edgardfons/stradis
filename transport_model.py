import numpy as np
from scipy import optimize

num_warehouse = 6
num_vendors = 8
A = [60, 55, 51, 43, 41, 52]
D = [35, 37, 22, 32, 41, 32, 43, 38]
C = [
    [6, 2, 6, 7, 4, 2, 5, 9],
    [4, 9, 5, 3, 8, 5, 8, 2],
    [5, 2, 1, 9, 7, 4, 3, 3],
    [7, 6, 7, 3, 9, 2, 7, 1],
    [2, 3, 9, 5, 7, 2, 6, 5],
    [5, 5, 2, 2, 8, 1, 4, 3]
]

c = np.array(C).flat[0:(num_warehouse*num_vendors)]

# Create A_ub 2-D array of ones ans zeros in the correct places
range_warehouse = np.arange(num_warehouse)
range_vendors = np.arange(num_vendors)
a_UB=[ np.concatenate( (np.zeros(num_vendors * num, dtype=int), np.ones(num_vendors, dtype=int), np.zeros(num_vendors * (num_warehouse - 1 - num), dtype=int)), dtype=int ).flat[0:(num_warehouse*num_vendors)].tolist() for num in range_warehouse]
a_EB=[ np.array(np.concatenate( (  np.zeros(num, dtype=int), np.array([1], dtype=int), np.zeros(num_vendors - 1 - num, dtype=int)  ), dtype=int ).flat[0:(num_vendors)].tolist() * num_warehouse).flat[0:(num_warehouse*num_vendors)].tolist() for num in range_vendors]

# Solve model and show simplified results
res = optimize.linprog(c, A_ub=a_UB, b_ub=A, A_eq=a_EB, b_eq=D, bounds=None, method='simplex')
print(res)