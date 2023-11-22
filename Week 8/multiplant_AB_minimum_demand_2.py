# Formulate and solve the small instance on multi-plant production model
from gurobipy import GRB, Model

# Create a new model
m = Model("factoryAB")

# Create variables
xas = m.addVar(vtype=GRB.CONTINUOUS, name="xas")
xad = m.addVar(vtype=GRB.CONTINUOUS, name="xad")
xbs = m.addVar(vtype=GRB.CONTINUOUS, name="xbs")
xbd = m.addVar(vtype=GRB.CONTINUOUS, name="xbd")

# Add constraints
m.addConstr(4*xas + 2*xad <= 80, "Factory A - Grinding Hours")
m.addConstr(2*xas + 5*xad <= 60, "Factory A - Polishing Hours")

m.addConstr(5*xbs + 3*xbd <= 60, "Factory B - Grinding Hours")
m.addConstr(5*xbs + 6*xbd <= 75, "Factory B - Polishing Hours")

# Combine Raw Material constraints to find optimal allocation of raw materials
m.addConstr(4*xas + 4*xad + 4*xbs + 4*xbd <= 120, "Raw Materials")

# Add constrianst for minimal demands
m.addConstr(xas + xbs >= 25, "Minimal Demand for Standard")
m.addConstr(xad + xbd >= 8, "Minimal Demand for Deluxe")


# Set objective
m.setObjective(10*xas + 10*xbs + 15*xad + 15*xbd, GRB.MAXIMIZE)

# Solve
m.optimize()

# Check if the model is feasible
# if m.status == GRB.Status.INFEASIBLE:
#     pass

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)
