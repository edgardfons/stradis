from pulp import *

def simpleLP():

    problem = LpProblem("schedulerClasses", LpMaximize)    

    cf0 = 450
    cf1 = 420
    cf2 = 400
    f0 = 2000
    f1 = 1500
    f2 = 1000

    goal = 80000
    max_num_days = 30
    num_factory = 3

    factory_days = LpVariable.dicts("factoryDays", list(range(num_factory)), 0, 30, cat="Continuous")

    # goal constraint
    c1 = factory_days[0]*f0 + factory_days[1]*f1 + factory_days[2] * f2 >= goal

    # production constraints
    c2 = factory_days[0]*f0 <= 2*factory_days[1]*f1
    c3 = factory_days[0]*f0 <= 2*factory_days[2]*f2
    c4 = factory_days[1]*f1 <= 2*factory_days[2]*f2
    c5 = factory_days[1]*f1 <= 2*factory_days[0]*f0
    c6 = factory_days[2]*f2 <= 2*factory_days[1]*f1
    c7 = factory_days[2]*f2 <= 2*factory_days[0]*f0

    # adding the constraints to the problem
    problem += c1
    problem += c2
    problem += c3
    problem += c4
    problem += c5
    problem += c6
    problem += c7

    problem += -factory_days[0]*cf0*f0 - factory_days[1]*cf1*f1 - factory_days[2]*cf2*f2

    print(problem)

    problem.solve()

    for i in range(3):
        print(f"Factory {i}: {factory_days[i].varValue}")

def egMyModel():
    