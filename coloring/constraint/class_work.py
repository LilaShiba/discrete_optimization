import constraint
import json

problem = constraint.Problem()

# We're letting VARIABLES 11 through 99 have an interval of [1..9]
for i in range(1, 10):
    problem.addVariables(range(i * 10 + 1, i * 10 + 10), range(1, 10))

# We're adding the constraint that all values in a row must be different
# 11 through 19 must be different, 21 through 29 must be all different,...
for i in range(1, 10):
    problem.addConstraint(constraint.AllDifferentConstraint(), range(i * 10 + 1, i * 10 + 10))
