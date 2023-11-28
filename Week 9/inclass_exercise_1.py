# Team Members: Fırat Batar, Zeynep Dağcı, Simay Karaca

from gurobipy import GRB, Model

m = Model('production')  # Create a production model

# Add two integer varialbes (>= 0) into the model
x1 = m.addVar(vtype=GRB.INTEGER, name="numOfWooden")
x2 = m.addVar(vtype=GRB.INTEGER, name="numOfAluminum")

# Add constraints
m.addConstr(x1 <= 6, "firstEmployeeWooden")
m.addConstr(x2 <= 4, "firstEmployeeAluminum")
m.addConstr(6 * x1 + 8 * x2 <= 48, "amountOfGlass")

# Set the objective
m.setObjective(300 * x1 + 150 * x2, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")