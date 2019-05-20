import constraint
# study + time = grades

problem = constraint.Problem()
problem.addVariables('SGT', range(1,10))
problem.addVariables('UDYIMERA', range(10))

def sum(s,t,u,d,y,i,m,e,g,r,a):
    if (s*10000+t*1000+u*100+d*10+y) + (t*10000+i*1000+m*100+e*10+s) == g*100000+r*10000+a*1000+d*100+e*10+s:
        return True

problem.addConstraint(sum, "STUDYIMEGRA")
# All the characters must represent different digits,
# there's a built-in constraint for that
problem.addConstraint(constraint.AllDifferentConstraint())
solution = problem.getSolution()
print(solution)
