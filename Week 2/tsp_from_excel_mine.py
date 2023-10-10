"""
ENS 208 

HIGHLIGHTS:
1. Reads a given Excel file using the Python package pandas.
2. Builds the distance matrix based on the data read from the Excel file.
3. Constructs a TSP solution using nearest neighbor algorithm for a given origin. 
"""

import pandas as pd


def distance_matrix_replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][j] = float('inf')


def nearest_neighbour(distance_matrix, source, nodes):
    path = []
    path_length = 0
    unvisited = nodes.copy()
    
    current = source
    while len(unvisited) != 0:
        do = False
        nearest_node = min(unvisited, key=lambda x: distance_matrix[current][x])

        unvisited.remove(nearest_node)  # Remove from unvisited list
        path.append(nearest_node)
        path_length += distance_matrix[current][nearest_node]
        current = nearest_node
    
    return path, path_length


# Read the distances from the excel file named "real_distances_10customers.xlsx"
df = pd.read_excel('real_distances_10customers.xlsx') # dataframe

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[df[j][i] for j in nodes] for i in nodes]

source = 0

distance_matrix_replace(d)
path, path_length = nearest_neighbour(d, source, nodes)

print(path, path_length)