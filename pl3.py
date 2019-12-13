import pulp as p 
  
# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMaximize)  
  
# Create problem Variables  
x1 = p.LpVariable("x1", lowBound = 0,cat = 'Binary')   
x2 = p.LpVariable("x2", lowBound = 0,cat = 'Binary')  
x3 = p.LpVariable("x3", lowBound = 0,cat = 'Binary')   
x4 = p.LpVariable("x4", lowBound = 0,cat = 'Binary')  
# Objective Function 
Lp_prob +=  9*x1+5*x2+6*x3+4*x4    
  
# Constraints: 
Lp_prob += 6*x1+3*x2+5*x3+2*x4<=10
Lp_prob += x3 + x4 <= 1
Lp_prob += -x1 +x3 <=0
Lp_prob += -x2 +x4 <=0
Lp_prob += x1 <=1 
Lp_prob += x2 <=1
Lp_prob += x3 <=1 
Lp_prob += x4<=1 
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(p.value(x1), p.value(x2),p.value(x3),p.value(x4), p.value(Lp_prob.objective)) 
'''
Minimize :  Z = 3x + 5y
Subject to the constraints: 
2x + 3y >= 12
-x + y <= 3
x >= 4
y <= 3
x, y >= 0
'''