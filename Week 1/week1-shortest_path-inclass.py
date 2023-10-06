"""
HIGHLIGHTS:
1. Creates a Python representation for a weighted directed graph.
2. Plots the graph.
3. Finds all simple paths from a given source to a given destination.
4. Finds the shortest path from a given source to a given destination 
and its length.
"""

import matplotlib.pyplot as plt
import networkx as nx

# Build the set of weighted edges - stored as tuples (i, j, w) where i, j, and 
# w correspond to the tail (start) node, head (end) node, and the weight (in 
# our case, the length) of the edge, respectively
our_edges = {('H', 'A', 3), ('H', 'B', 2), ('H', 'C', 5),
             ('A', 'F', 3),
             ('B', 'D', 2),
             ('C', 'E', 3), ('C', 'D', 2),
             ('D', 'G', 4),
             ('E', 'F', 1), ('E', 'G', 2), ('E', 'C', 3),
             ('F', 'G', 3), ('F', 'U', 5), ('F', 'E', 1),
             ('G', 'U', 2)}

# Create an empty directed graph
G = nx.DiGraph()

# Add weighted edges to G
G.add_weighted_edges_from(our_edges)

# Print the nodes of G
print(sorted(G.nodes))

# Print the edges of G
print(sorted(G.edges))

# Adjacency view of G
print(G.adj)

# Draw G (do not show weights on edges)
pos = nx.spring_layout(G, scale=100.)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.axis('off')
plt.show()

# Specify beginning (source) & final (sink) nodes named Home (H) and University (U), respectively
b = 'H'
f = 'U'

# Enumerate all simple paths from H to S
paths = nx.all_simple_paths(G, b, f)

# print(paths) # This is not going to work
print(list(paths))  # This is going to work but not going to look nice

# This for-loop will print each path to a separate line


# Find the shortest path from 'H' to 'U' using Dijkstra's algorithm
path = nx.dijkstra_path(G, b, f)
path_length = nx.dijkstra_path_length(G, b, f)

# Print the shortest path and its length
print("The shortest path from", b, "to", f, "is: ", path, "with length", path_length)
