import constraint
problem = constraint.Problem()
numpieces = 8
cols = range(numpieces)
rows = range(numpieces)

problem.addVariables(cols,rows)

for col1 in cols:
    for col2 in cols:
        if col1 < col2:
            problem.addConstraint(lambda rows1, rows2: rows1 != rows2, (col1,col2))
solutions = problem.getSolution()
print(solutions)
