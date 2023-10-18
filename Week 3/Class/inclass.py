import pandas as pd

# Read the distances from the excel file named "real_distances_10customers.xlsx"
df = pd.read_excel('Week3-Exercise-NNH-Data.xlsx') # dataframe

# List of nodes
# nodes = list(range(11))
nodes = list(range(df.shape[0]))


# Build distance matrix
d = [[df[j][i] for j in nodes] for i in nodes]

origin = 10
tour = [origin]
tour_length = 0
current_node = origin

while len(tour) < len(nodes):
    nearest_node = None  # Not known yet
    dist_to_nearest_node = max(d[current_node]) + 1  # A large enough node
    # Find the (unvisited) nearest
    for i in nodes:
        if current_node == 12:
            break
        if i == 18:
            continue
        
        if i not in tour and d[current_node][i] < dist_to_nearest_node:
            nearest_node = i  # Update the nearest node
            dist_to_nearest_node = d[current_node][i]  # Update the distance to nearest

    if current_node == 12:
        nearest_node = 18
        dist_to_nearest_node = d[current_node][nearest_node]
    
    tour.append(nearest_node)  # Add nearest to the tour
    print(f"From {current_node} to {nearest_node}: {dist_to_nearest_node}. Total: {tour_length}")
    tour_length += dist_to_nearest_node  # Update the tour length
    current_node = nearest_node  # Udate the current node

tour_length += d[tour[-1]][origin]
tour.append(origin)

print(f"TSP tour found with neares neigbour heuristic starting from {origin} is {tour} with a total length of {tour_length}")


