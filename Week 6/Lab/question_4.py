# Minimize 2 * x1 + 3.5 * x2
# subject to
#   protein: x1 + 2 * x2 >= 9
#   carbs: 3 * x1 + 2 * x2 >= 15

from gurobipy import GRB, Model

m = Model('Diet')  # Create a production model

# Add two continues decision varialbes (>= 0) into the model
x1 = m.addVar(vtype=GRB.CONTINUOUS, name="first_drink")  
x2 = m.addVar(vtype=GRB.CONTINUOUS, name="second_drink")

# Add constraints
m.addConstr(x1 + 2 * x2 >= 9, "protein")
m.addConstr(3 * x1 + 2 * x2 >= 15, "carbs")

# Set the objective
m.setObjective(2 * x1 + 3.5 * x2, GRB.MINIMIZE)

m.optimize()

# Print the results
for v in m.getVars():
    print(v.varName, round(v.x))

print(f"The optimal objective function value is {m.objVal}")