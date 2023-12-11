
from gurobipy import GRB, Model

demand = [[0, 0, 0, 0, 0, 0, 0],              #item0 (not exist)
          [0, 80, 70, 15, 45, 30, 150],       #item1  (demand at period 0 = 0)      
          [0, 28, 80, 40, 60, 90, 120],       #item2
          [0, 25, 45, 40, 80, 10, 180],       #item3
          [0, 30, 80, 15, 65, 90, 200]]       #item4     
p = 5
h = 0.5
f = 50

M = sum([sum(demand[i]) for i in range(len(demand))])

m = Model('multi-item-LSP')

# Variables 
x = m.addVars(range(1, 5), range(1, 7), vtype=GRB.CONTINUOUS, name='x')
y = m.addVars(range(1, 5), range(1, 7), vtype=GRB.BINARY, name='y')
I = m.addVars(range(0, 5), range(0, 7), vtype=GRB.CONTINUOUS, name='I')

# Constraints 
m.addConstrs((I[i, t-1] + x[i, t] == demand[i][t] + I[i, t]) for i in range(1, 5) for t in range(1, 7))
m.addConstrs(I[i, 0] == 0 for i in range(1, 5))
m.addConstrs((x[i, t] <= M * y[i, t] for i in range(1, 5) for t in range(1, 7)))


m.setObjective(p * x.sum() + f * y.sum() + h * I.sum(), GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)