# 31 vertices , 66 edges

adj = {0: [(1, 10), (2, 2), (3, 7)], 2: [(3, 2), (4, 5)], 3: [(0, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 6)]}
container = [4, 2, 3, 1, 2]

# Function to add an edge to the adjacency list
# Printing the adjacency list
for node, neighbors in adj.items():
    print(f"adj[{node}]:", end=" ")
    for neighbor, weight in neighbors:
        print(f"({neighbor}, {weight})", end=" ")
    print()