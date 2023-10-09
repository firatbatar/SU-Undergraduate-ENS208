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
# print(sorted(G.nodes))

# Print the edges of G
# print(sorted(G.edges))

# Adjacency view of G
# print(G.adj)
adj = dict(G.adj)

# Draw G (do not show weights on edges)
pos = nx.spring_layout(G, scale=100.)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.axis('off')
plt.show()

# Specify beginning (source) & final (sink) nodes named Home (H) and University (U), respectively
source = 'H'
sink = 'U'

# Enumerate all simple paths from H to S
paths = nx.all_simple_paths(G, source, sink)

# print(paths) # This is not going to work
# print(list(paths))  # This is going to work but not going to look nice

# This for-loop will print each path to a separate line
# for path in list(paths):
#     print(path)

# Find the shortest path from 'H' to 'U' using Dijkstra's algorithm

# All nodes have two informations:
# [currently_found_shortest_distance, node_that_shortes_distance_came]
unvisited = {key: [float('inf'), None] for key in list(sorted(G.nodes))}  # Mark all nodes as unvisited
visited = dict()  # A dict for storing visited nodes
unvisited[source][0] = 0  # Source node has distance 0
current = None  # The current node that we check its neighbours

# Go over the unvisited nodes until sink becomes visited
while sink in unvisited:
    # Select the unvisited node with the minimum distance as the current node
    current = min(unvisited, key=lambda x: unvisited[x][0])
    # Go over its unvisited neighbours
    for neighbour in adj[current].keys():
        if neighbour in unvisited:
            # Distance from current node to its neighbour
            new_dist = unvisited[current][0] + adj[current][neighbour].get("weight")
            if new_dist < unvisited[neighbour][0]:
                # Replace new minium distance to that nighbour
                unvisited[neighbour] = [new_dist, current]

    # Mark current node as visited
    visited[current] = unvisited.pop(current)

all_nodes = unvisited | visited  # Combine visited and unvisited nodes
path_length = all_nodes[sink][0]  # Shortest path length is the distance to sink node

# Retrace the path from sink to source
path = list()
step = sink  # Last step of the path is the sink
while step is not None:  # Step reaches None when it reaches the source
    path.insert(0, step)   # Add to the beggining of the path to get the path from source to sink
    step = all_nodes[step][1]  # Change step to previous node from current step

# Print the shortest path and its length
print(f"The shortest path from { source } to { sink } is: { path } with length { path_length }")
