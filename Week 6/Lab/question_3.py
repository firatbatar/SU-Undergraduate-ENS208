# Maximaze a * xc + b * xt + c * xs
# subject to
#   xc + 2 * xt + 0.5 * xs <= 50
#   2 * xc + xt + 0.5 * xs <= 40

from gurobipy import GRB, Model

m = Model('Carpenter - 3')  # Create a production model

# Add two continues decision varialbes (>= 0) into the model
xc = m.addVar(vtype=GRB.CONTINUOUS, name="num_of_chairs")  
xt = m.addVar(vtype=GRB.CONTINUOUS, name="num_of_tables")
xs = m.addVar(vtype=GRB.CONTINUOUS, name="num_of_stools")

# Add constraints
m.addConstr(xc + 2 * xt + 0.5 * xs <= 50, "raw_material")
m.addConstr(2 * xc + xt + 0.5 * xs <= 40, "work_time")

# Set the objective
a = 10
b = 15
c = 5
m.setObjective(a * xc + b * xt + c * xs, GRB.MAXIMIZE)

m.optimize()

# Print the results
for v in m.getVars():
    print(v.varName, v.x)

print(f"The optimal objective function value is {m.objVal}")