from gurobipy import GRB, Model

# Create a new model
m = Model("carpenter")

# Create variables for chairs and tables for 4 weeks
xc1 = m.addVar(vtype=GRB.INTEGER, name="numOfChairs1")
xc2 = m.addVar(vtype=GRB.INTEGER, name="numOfChairs2")
xc3 = m.addVar(vtype=GRB.INTEGER, name="numOfChairs3")
xc4 = m.addVar(vtype=GRB.INTEGER, name="numOfChairs4")

xt1 = m.addVar(vtype=GRB.INTEGER, name="numOfTables1")
xt2 = m.addVar(vtype=GRB.INTEGER, name="numOfTables2")
xt3 = m.addVar(vtype=GRB.INTEGER, name="numOfTables3")
xt4 = m.addVar(vtype=GRB.INTEGER, name="numOfTables4")

Ic1 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfChairs1")
Ic2 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfChairs2")
Ic3 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfChairs3")
Ic4 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfChairs4")
It1 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfTables1")
It2 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfTables2")
It3 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfTables3")
It4 = m.addVar(vtype=GRB.INTEGER, name="inventoryOfTables4")


# Add constraints
m.addConstr(xc1 + 2.5*xt1 <= 50, "rawMat1")
m.addConstr(xc2 + 2.5*xt2 <= 50, "rawMat2")
m.addConstr(xc3 + 2.5*xt3 <= 50, "rawMat3")
m.addConstr(xc4 + 2.5*xt4 <= 50, "rawMat4")

m.addConstr(2 * xc1 + xt1 <= 40, "workHour1")
m.addConstr(2 * xc2 + xt2 <= 40, "workHour2")
m.addConstr(2 * xc3 + xt3 <= 40, "workHour3")
m.addConstr(2 * xc4 + xt4 <= 40, "workHour4")

m.addConstr(8 + xc1 == 16 + Ic1, "invBalDemanChP1")
m.addConstr(Ic1 + xc2 == 20 + Ic2, "invBalDemanChP2")
m.addConstr(Ic2 + xc3 == 15 + Ic3, "invBalDemanChP3")
m.addConstr(Ic3 + xc4 == 13 + Ic4, "invBalDemanChP4")

m.addConstr(5 + xt1 == 12 + It1, "invBalDemanTbP1")
m.addConstr(It1 + xt2 == 8 + It2, "invBalDemanTbP2")
m.addConstr(It2 + xt3 == 18 + It3, "invBalDemanTbP3")
m.addConstr(It3 + xt4 == 15 + It4, "invBalDemanTbP4")

# Set objective
m.setObjective(10 * (xc1 + xc2 + xc3 + xc4) + 15 * (xt1 + xt2 + xt3 + xt4), GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
    print(v.varName, v.x)

print('The optimal objective function value is', m.objVal)
