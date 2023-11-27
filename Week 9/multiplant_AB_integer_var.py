# Formulate and solve the small instance on multi-plant production model
from gurobipy import GRB, Model

# Create a new model
m = Model("factoryAB")

# Create variables
xas = m.addVar(vtype=GRB.INTEGER, name="xas")
xad = m.addVar(vtype=GRB.INTEGER, name="xad")
xbs = m.addVar(vtype=GRB.INTEGER, name="xbs")
xbd = m.addVar(vtype=GRB.INTEGER, name="xbd")

# Add constraints
m.addConstr(4*xas + 2*xad <= 80, "Factory A - Grinding Hours")
m.addConstr(2*xas + 5*xad <= 60, "Factory A - Polishing Hours")

m.addConstr(5*xbs + 3*xbd <= 60, "Factory B - Grinding Hours")
m.addConstr(5*xbs + 6*xbd <= 75, "Factory B - Polishing Hours")

# Combine Raw Material constraints to find optimal allocation of raw materials
m.addConstr(4*xas + 4*xad + 4*xbs + 4*xbd <= 120, "Raw Materials")


# Set objective
m.setObjective(10*xas + 10*xbs + 15*xad + 15*xbd, GRB.MAXIMIZE)

# Solve
m.optimize()


for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)
