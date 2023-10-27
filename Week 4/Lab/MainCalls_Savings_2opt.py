"""
ENS 208 - Introduction to IE

Constructs a TSP solution using the savings algorithm and improves it
using the 2-opt algorithm.
"""

import pandas as pd
from TSP_Algos import savings, two_opt

# Read the distance matrix from the excel file TSP_Data
df = pd.read_excel('TSP_Data.xlsx')
#print(df.shape)

# List of nodes
nodes = list(range(df.shape[0]))

# Build distance matrix
d = [[round(float(df[j][i]), 2) for j in nodes] for i in nodes]

origin = 0 # origin for the TSP tour

# Call the savings function to construct a TSP tour via the savings algorithm 
tour, tour_length = savings(nodes, origin, d)
print('TSP tour found with savings heuristic starting from', origin, 'is', tour,
      'with total length', tour_length)

# Start with  the tour found by savings heuristic and improve it via 2-opt 
#until no further improvement is achieved
# Call the 2-opt function
tour, tour_length = two_opt(tour, tour_length, d)
# Print the best solution found as a result of the improvement phase
print('Improved TSP tour is', tour, 'with total length', tour_length)  