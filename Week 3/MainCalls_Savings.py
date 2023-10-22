"""
ENS 208 - Introduction to IE

Constructs a TSP solution using the savings algorithm.
"""

import pandas as pd
from TSP_Algos import savings

# Read distance matrix from the excel file tsp_data
df = pd.read_excel('TSP_Data.xlsx')
#print(df.shape)

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

origin = 0 # origin for the TSP tour

# Call the savings function to construct a TSP tour via the savings algorithm 
tour, tour_length = savings(nodes, origin, d)

# Print the tour
print('\nA feasible TSP tour found with savings heuristic starting from', origin, 'is', 
      tour, 'with total length', tour_length)