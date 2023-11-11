# Maximaze a * xc + b * xt
# subject to
#   xc + 2 * xt <= 50
#   2 * xc + xt <= 40

from gurobipy import GRB, Model

m = Model('Carpenter - 1')  # Create a production model

# Add two continues decision varialbes (>= 0) into the model
xc = m.addVar(vtype=GRB.CONTINUOUS, name="num_of_chairs")  
xt = m.addVar(vtype=GRB.CONTINUOUS, name="num_of_tables")

# Add constraints
m.addConstr(xc + 2 * xt <= 50, "raw_material")
m.addConstr(2 * xc + xt <= 40, "work_time")

# Set the objective
a = 10
b = 10
m.setObjective(a * xc + b * xt, GRB.MAXIMIZE)

m.optimize()

# Print the results
for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")