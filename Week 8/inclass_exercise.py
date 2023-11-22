# Team Members: Fırat Batar, Kerem Boncuk, İremsu Özdemir, Onur Orman

from gurobipy import GRB, Model

# Create a new model
m = Model("Gym Diet Example")

# Create variables
d1 = m.addVar(vtype=GRB.CONTINUOUS, name="d1")
d2 = m.addVar(vtype=GRB.CONTINUOUS, name="d2")
d3 = m.addVar(vtype=GRB.CONTINUOUS, name="d3")

# Add constraints
m.addConstr(d1 <= 3, "Max d1")
m.addConstr(d2 <= 3, "Max d2")
m.addConstr(d3 <= 3, "Max d3")

m.addConstr(d1 + 2*d2 + 1.5*d3 >= 8, "Protein")
m.addConstr(3*d1 + 2*d2 + d3 >= 12, "Carbohydrates")
m.addConstr(d1 + d2 + d3 >= 7, "Calcium")

# Set objective
m.setObjective(2*d1 + 3.5*d2 + d3, GRB.MINIMIZE)

# Solve
m.optimize()

# Print the optimal solution
for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)