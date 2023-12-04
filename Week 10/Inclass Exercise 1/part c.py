from gurobipy import GRB, Model

# Create a new model
m = Model("Part A")

# Create variables
xas = m.addVar(vtype=GRB.INTEGER, name="xas")
xad = m.addVar(vtype=GRB.INTEGER, name="xad")
xbs = m.addVar(vtype=GRB.INTEGER, name="xbs")
xbd = m.addVar(vtype=GRB.INTEGER, name="xbd")

yas = m.addVar(vtype=GRB.BINARY, name="yas")
yad = m.addVar(vtype=GRB.BINARY, name="yad")
ybs = m.addVar(vtype=GRB.BINARY, name="ybs")
ybd = m.addVar(vtype=GRB.BINARY, name="ybd")

# Add constraints
m.addConstr(4*xas + 2*xad <= 100, "Factory A - Grinding Hours")
m.addConstr(2*xas + 5*xad <= 60, "Factory A - Polishing Hours")

m.addConstr(5*xbs + 3*xbd <= 60, "Factory B - Grinding Hours")
m.addConstr(5*xbs + 6*xbd <= 75, "Factory B - Polishing Hours")

# Add constraints for binary variables
M = 1000
m.addConstr(xas <= M*yas, "yas")
m.addConstr(xad <= M*yad, "yad")
m.addConstr(yas + yad <= 1, "Factory A - Only one product")

m.addConstr(xbs <= M*ybs, "ybs")
m.addConstr(xbd <= M*ybd, "ybd")
m.addConstr(ybs + ybd <= 1, "Factory B - Only one product")

# Each product type is made at either one of the factories
m.addConstr(yas + ybs == 1, "Product A - Factory")
m.addConstr(yad + ybd == 1, "Product B - Factory")

# Combine Raw Material constraints to find optimal allocation of raw materials
m.addConstr(4*xas + 4*xad + 4*xbd <= 120, "Raw Materials")


# Set objective
m.setObjective(10*xas + 20*xad + 20*xbd, GRB.MAXIMIZE)

# Solve
m.optimize()


for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)
