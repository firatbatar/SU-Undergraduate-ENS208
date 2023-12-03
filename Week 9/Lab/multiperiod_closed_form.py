from gurobipy import GRB, Model

# Create a new multiperiod production model
m = Model("multiPeriodCarpenter")

# Define period demends for chairs and tables
chair_demand = [0, 16, 20, 15, 13]  # 0 is a dummy value for the period before the first period
table_demand = [0, 12, 8, 18, 15]  # 0 is a dummy value for the period before the first period

# Define the number of chairs and tables in closed form
Xc = m.addVars(range(1, 5), vtype=GRB.INTEGER, name="num_chairs")
Xt = m.addVars(range(1, 5), vtype=GRB.INTEGER, name="num_tables")

# Define the leftover inventory of chairs and tables in closed form
Ic = m.addVars(range(0, 5), vtype=GRB.INTEGER, name="inv_chairs")
It = m.addVars(range(0, 5), vtype=GRB.INTEGER, name="inv_tables")

# Add constraints
# Raw material and work hour constraints
m.addConstrs((Xc[i] + 2.5 * Xt[i] <= 50 for i in range(1, 5)), name="raw_material")
m.addConstrs((2 * Xc[i] + Xt[i] <= 40 for i in range(1, 5)), name="work_hours")

# Demand/Inventory/Balance constraints
m.addConstrs((Ic[i - 1] + Xc[i] == chair_demand[i] + Ic[i] for i in range(1, 5)), name="chair_demand")
m.addConstrs((It[i - 1] + Xt[i] == table_demand[i] + It[i] for i in range(1, 5)), name="table_demand")

# Initial inventory constraints
m.addConstr(Ic[0] == 8, name="initial_chair_inventory")
m.addConstr(It[0] == 5, name="initial_table_inventory")

# Set objective
m.setObjective(10 * Xc.sum() + 15 * Xt.sum(), GRB.MAXIMIZE)

# Solve model
m.optimize()

# Print solution
for v in m.getVars():
    print(v.varName, v.x)
print("Optimal objective value:", m.objVal)
