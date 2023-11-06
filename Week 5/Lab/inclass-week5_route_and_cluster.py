import pandas as pd

# Read the distance matrix from the excel file "real_distances_40customers.xlsx"
df = pd.read_excel('..\\real_distances_40customers.xlsx')

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]
demand = [1] * len(nodes)

origin = 0 # origin for the vehicle routes

# Below is the tour given
tour = [0, 27, 36, 23, 26, 11, 39, 34, 33, 13, 16, 22, 30, 6, 25, 7, 12, 21, 
        8, 18, 3, 31, 10, 20, 35, 40, 38, 2, 15, 37, 29, 28, 1, 24, 14, 4, 19, 
        5, 17, 32, 9, 0]


vrp_solution = []
vrp_solution_length = 0
veh_cap = 15

current_tour = [origin]
total_demand = 0

for idx in range(1, len(tour)):
    if tour[idx] != origin:
        if total_demand + demand[tour[idx]] <= veh_cap:
            current_tour.append(tour[idx])
            total_demand += demand[tour[idx]]
        else:
            current_tour.append(origin)
            vrp_solution.append(current_tour)
        
            current_tour = [origin]
            total_demand = 0
    else:
        current_tour.append(origin)
        vrp_solution.append(current_tour)
        break

for r in vrp_solution:
    for i in range(len(r) - 1):
        vrp_solution_length += d[r[i]][r[i + 1]] 


print(f"VRP Solution: {vrp_solution} with length {vrp_solution_length:.2f}")