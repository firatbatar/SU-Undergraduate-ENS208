"""
ENS 208 

HIGHLIGHTS:
1. Reads a given Excel file using the Python package pandas.
2. Builds the distance matrix based on the data read from the Excel file.
3. Constructs a TSP solution using nearest neighbor algorithm for a given origin. 
"""

import pandas as pd

# Read the distances from the excel file named "real_distances_10customers.xlsx"
df = pd.read_excel('real_distances_10customers.xlsx') # dataframe
print(df)

# Get info about the dataframe
# df.describe() # some descriptive stats
# df.info() # summary info
print(df.shape) # number of rows & columns
# df.columns # list of column names

# List of nodes
# nodes = list(range(11))
nodes = list(range(df.shape[0]))
print(nodes)

print("df[2][5]", df[2][5])

# Build distance matrix
d = [[df[j][i] for j in nodes] for i in nodes]

print("d[5][2]", d[5][2])

origin = 0
tour = [origin]
tour_length = 0
current_node = origin

while len(tour) < len(nodes):
    nearest_node = None  # Not known yet
    dist_to_nearest_node = max(d[current_node]) + 1  # A large enough node
    # Find the (unvisited) nearest
    for i in nodes:
        if i not in tour and d[current_node][i] < dist_to_nearest_node:
            nearest_node = i  # Update the nearest node
            dist_to_nearest_node = d[current_node][i]  # Update the distance to nearest
    
    tour.append(nearest_node)  # Add nearest to the tour
    tour_length += dist_to_nearest_node  # Update the tour length
    current_node = nearest_node  # Udate the current node

tour_length += d[tour[-1]][origin]
tour.append(origin)

print(tour, tour_length)


