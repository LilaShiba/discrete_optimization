# import module to use constraint programing
# constraint programming is declarative. One describes the solution
# Problem:
# Find all (x,y) where x ∈ {1,2,3} and 0 <= y < 10, and x + y >= 5

import constraint

problem = constraint.Problem()
problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))

def our_constraint(x,y):
    if (x + y) >= 5:
        return True

problem.addConstraint(our_constraint, ['x','y'])
solutions = problem.getSolutions()
print(solutions)
