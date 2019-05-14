import constraint
# two + two = four
problem = constraint.Problem()

problem.addVariables("TF", range(1, 10))
problem.addVariables("WOUR", range(10))

# Telling Python that we need TWO + TWO = FOUR
def sum_constraint(t, w, o, f, u, r):
    if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
        return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(sum_constraint, "TWOFUR")


# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())


solutions = problem.getSolutions()

print(solutions)
