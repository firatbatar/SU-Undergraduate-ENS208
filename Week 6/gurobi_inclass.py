from gurobipy import GRB, Model

m = Model('production')  # Create a production model

# Add two continues varialbes (>= 0) into the model
xc = m.addVar(vtype=GRB.CONTINUOUS, name="numOfChairs")  
xt = m.addVar(vtype=GRB.CONTINUOUS, name="numOfTables")

# Add constraints
m.addConstr(xc + 2 * xt <= 50, "rawMaterial")
m.addConstr(2* xc + xt <= 40, "workTime")
m.addConstr(xc + xt <= 28, "glue")

# Set the objective
m.setObjective(10 * xc + 15 * xt, GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")