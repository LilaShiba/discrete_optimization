#https://stackabuse.com/constraint-programming-with-python-constraint/
import constraint
# send + more = money
problem = constraint.Problem()

problem.addVariables("SM", range(1, 10))
problem.addVariables("ENDORY", range(10))

# Telling Python that we need SEND + MORE = MONEY
def sum_constraint(s, e, n, d, m, o, r, y):
    if (s*1000 + e*100 + n*10 + d) + (m*1000 + o*100 + r*10 + e)== m*10000 + o*1000 + n*100 + e*10 + y:
        return True

# Adding our custom constraint. The
# order of variables is important!
problem.addConstraint(sum_constraint, "SENDMORY")


# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())


solutions = problem.getSolutions()

print(solutions)
