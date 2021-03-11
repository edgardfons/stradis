import numpy as np
from scipy import optimize

"""

SETS:

WAREHOUSES: CAPACITY;
VENDORS: DEMAND;
LINKS( WAREHOUSES, VENDORS): COST, VOLUME;

ENDSETS

! Here is the data;
DATA:

!set members;
WAREHOUSES = WH1 WH2 WH3 WH4 WH5 WH6;
VENDORS = V1 V2 V3 V4 V5 V6 V7 V8;
!attribute values;
CAPACITY = 60 55 51 43 41 52;
DEMAND = 35 37 22 32 41 32 43 38;
COST = 
6 2 6 7 4 2 5 9
4 9 5 3 8 5 8 2
5 2 1 9 7 4 3 3
7 6 7 3 9 2 7 1
2 3 9 5 7 2 6 5
5 5 2 2 8 1 4 3;

ENDDATA

! The objective;
MIN = @SUM( LINKS( I, J):
COST( I, J) * VOLUME( I, J));

! The demand constraints;
@FOR( VENDORS( J):
@SUM( WAREHOUSES( I): VOLUME( I, J)) =
DEMAND( J));

! The capacity constraints;
@FOR( WAREHOUSES( I):
@SUM( VENDORS( J): VOLUME( I, J)) <=
CAPACITY( I));


 scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', callback=None, options={'maxiter': 5000, 'disp': False, 'presolve': True, 'tol': 1e-12, 'autoscale': False, 'rr': True, 'bland': False}, x0=None)

"""
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

# print(len(c))
# print(A)
# print(D)

# print('[')
# print(f'len a_UB: {len(a_UB[0])}')
# for arr in a_UB:
#     print(arr)
# print(']')

# print('---------------------------------------')

# print('[')
# print(f'len a_EB: {len(a_EB[0])}')
# for arr in a_EB:
#     print(arr)
# print(']')

res = optimize.linprog(c, A_ub=a_UB, b_ub=A, A_eq=a_EB, b_eq=D, bounds=None, method='simplex')
print(res)