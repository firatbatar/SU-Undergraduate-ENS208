from gurobipy import GRB, Model

demand = [0, 52, 87, 23, 56]
p = 9
h = 1
f = 75

m = Model('4period-LotSizing')

# Variables for order/production size
x = m.addVars(range(1, len(demand)), vtype=GRB.CONTINUOUS, name='x')

# Variables for fixed set-up
y = m.addVars(range(1, len(demand)), vtype=GRB.BINARY, name='y')

# Variables for fixed inventory level at the end of the period
I = m.addVars(range(0, len(demand)), vtype=GRB.CONTINUOUS, name='I')
m.addConstr(I[0] == 0, name='I0')

# Constraints for stock control and demand satisfaction
m.addConstrs((I[t - 1] + x[t] == demand[t] + I[t] for t in range(1, len(demand))), name='invBal')

# Constraints to determine how to handle the fixed cost
M = sum(demand)
m.addConstrs((x[t] <= M * y[t] for t in range(1, len(demand))), name='link')

# Define the objective function
m.setObjective(p * x.sum() + f * y.sum() + h * I.sum(), GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)