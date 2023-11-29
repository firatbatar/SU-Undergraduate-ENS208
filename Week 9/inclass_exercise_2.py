# Team Members: Fırat Batar, Kerem Boncuk

from gurobipy import GRB, Model

m = Model('production')  # Create a production model

# Add two integer varialbes (>= 0) into the model
x1 = m.addVar(vtype=GRB.INTEGER, name="numOfProduct1")  
x2 = m.addVar(vtype=GRB.INTEGER, name="numOfProduct2")

# Add constraints
m.addConstr(x1 + 3 * x2 <= 200, "frameParts")
m.addConstr(2 * x1 + 2 * x2 <= 300, "electronicComponents")
m.addConstr(x2 <= 60, "notProfitable")

# Set the objective
m.setObjective(x1 + 2 * x2, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")