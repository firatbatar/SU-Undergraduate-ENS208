from gurobipy import GRB, Model

demand = [0, 52, 87, 23, 56]
p = 9
h = 1
f = 75

m = Model('4period-LotSizing')

# Variables for order/production size
x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2')
x3 = m.addVar(vtype=GRB.CONTINUOUS, name='x3')
x4 = m.addVar(vtype=GRB.CONTINUOUS, name='x4')

# Variables for fixed set-up
y1 = m.addVar(vtype=GRB.BINARY, name='y1')
y2 = m.addVar(vtype=GRB.BINARY, name='y2')
y3 = m.addVar(vtype=GRB.BINARY, name='y3')
y4 = m.addVar(vtype=GRB.BINARY, name='y4')

# Variables for fixed inventory level at the end of the period
i1 = m.addVar(vtype=GRB.CONTINUOUS, name='I1')
i2 = m.addVar(vtype=GRB.CONTINUOUS, name='I2')
i3 = m.addVar(vtype=GRB.CONTINUOUS, name='I3')
i4 = m.addVar(vtype=GRB.CONTINUOUS, name='I4')

# Constraints for stock control and demand satisfaction
m.addConstr(x1 == demand[1] + i1, name='invBalP1')
m.addConstr(i1 + x2 == demand[2] + i2, name='invBalP2')
m.addConstr(i2 + x3 == demand[3] + i3, name='invBalP3')
m.addConstr(i3 + x4 == demand[4] + i4, name='invBalP4')

# Constraints to determine how to handle the fixed cost
M = sum(demand)
m.addConstr(x1 <= M * y1, name='linkP1')
m.addConstr(x2 <= M * y2, name='linkP2')
m.addConstr(x3 <= M * y3, name='linkP3')
m.addConstr(x4 <= M * y4, name='linkP4')

# Define the objective function
m.setObjective(p * (x1 + x2 + x3 + x4) + f * (y1 + y2 + y3 + y4) + h * (i1 + i2 + i3 + i4), GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)