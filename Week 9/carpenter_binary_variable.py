from gurobipy import GRB, Model

m = Model('production')  # Create a production model

# Add two integer varialbes (>= 0) into the model
xc = m.addVar(vtype=GRB.INTEGER, name="numOfChairs")  
xt = m.addVar(vtype=GRB.INTEGER, name="numOfTables")

# Add binary variables
yc = m.addVar(vtype=GRB.BINARY, name="ProductionOfChairs")
yt = m.addVar(vtype=GRB.BINARY, name="ProductionOfTables")
# yc = m.addVar(vtype=GRB.INTEGER, lb=0, ub=1, name="ProductionOfChairs")

# Add constraints
m.addConstr(xc + 2.5 * xt <= 50, "rawMaterial")
m.addConstr(2* xc + xt <= 40, "workTime")

# Define a big M
M = 20

# Can only produce chairs or tables
m.addConstr(xc <= M * yc, "LinkToBinaryVariableChair")
m.addConstr(xt <= M * yt, "LinkToBinaryVariableTable")
m.addConstr(yc + yt <= 1, "EitherChairsOrTables")

# Set the objective
m.setObjective(10 * xc + 15 * xt, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")