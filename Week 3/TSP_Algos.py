'''
ENS 208 - Introduction to IE

Function definitions for nearest neighbor, savings, and 2-opt algorithms.
'''

from pqdict import pqdict

def nearest_neighbor(nodes, origin, d):
    '''
    Constructs a TSP solution using the nearest neighbor algorithm, NNH, 
    for a given set of nodes, the associated pairwise distance matrix-d, 
    and the origin.
    '''
    # Tour should start at the origin
    tour = [origin]
    
    # Initialize the tour length
    tour_length = 0
    
    # If the origin is not in nodes, add it to nodes
    if origin not in nodes:
        nodes.append(origin)
        
    # Initialize the current node to be the origin
    current_node = origin
    
    # Nearest neighbor search until all nodes are visited
    while len(tour) < len(nodes):
        nearest_node = None # not known yet
        dist_to_nearest_node = max(d[current_node])+1 # a large enough number
        # Find the (unvisited) node that is nearest with respect to the current node
        for i in nodes:
            if i not in tour and d[current_node][i] < dist_to_nearest_node:
                #print("Node", i, "is closer to", current_node, "with distance", d[current_node][i])
                nearest_node = i # update nearest node
                dist_to_nearest_node = d[current_node][i] # update the distance to the nearest node
        #print("The nearest unvisited node is found to be", nearest_node)
        tour_length += dist_to_nearest_node # update the tour length
        tour.append(nearest_node) # add the nearest node to the end of the tour
        print('Added', nearest_node, 'to the tour!')
        current_node = nearest_node # update the current node
    
    # Tour should end at the origin
    tour_length += d[tour[-1]][origin]
    tour.append(origin)
    
    # Round the result to 2 decimals to avoid floating point representation errors
    tour_length = round(tour_length, 2)

    # Return the resulting tour and its length as a tuple
    return tour, tour_length

def savings(nodes, origin, d):
    '''
    Constructs a TSP solution using the savings method for a given set/list of 
    nodes, their pairwise distances-d, and the origin.
    '''
    # Set of customer nodes (i.e. nodes other than the origin)
    customers = {i for i in nodes if i != origin}
    
    # Initialize out-and-back tours from the origin to every other node
    tours = {(i, i): [origin, i, origin] for i in customers}
    
    # Compute savings
    savings = {(i, j): round(d[i][origin] + d[origin][j] - d[i][j], 2) 
               for i in customers for j in customers if j != i}
        
    # Define a priority queue dictionary to get a pair of nodes (i,j) which yields
    # the maximum savings
    pq = pqdict(savings, reverse = True)
    
    # Merge subtours until obtaining a TSP tour
    while len(tours) > 1:
        i, j = pq.pop()
        # print("\nSelected customer pair:", (i, j))
        # Outer loop
        break_outer = False
        for t1 in tours:
            for t2 in tours.keys() - {t1}:
                if t1[1] == i and t2[0] == j:
                    # print('Merging', tours[t1], 'and', tours[t2])
                    tours[(t1[0], t2[1])] = tours[t1][:-1] + tours[t2][1:]
                    del tours[t1], tours[t2]
                    # print(tours)
                    break_outer = True
                    break
            if break_outer:
                break
        # else:
            # print('No merging opportunities can be found for', (i,j)) 
    
    # Final tours dictionary (involves a single tour, which is the TSP tour)
    # print("\nFinal tour:", tours)
    
    # Compute tour length
    tour_length = 0
    for tour in tours.values():
        for i in range(len(tour)-1):
            tour_length += d[tour[i]][tour[i+1]]
            
    # Round the result to 2 decimals to avoid floating point representation errors
    tour_length = round(tour_length, 2)

    # Return the resulting tour and its length as a tuple
    return tour, tour_length