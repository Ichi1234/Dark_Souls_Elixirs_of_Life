# 31 vertices , 66 edges

adj = {0: [(1, 10), (2, 2), (3, 7)], 2: [(3, 2), (4, 5)], 3: [(4, 1)], 4: [(0, 4), (1, 4)]}
container = [0, 2, 3, 1, 2]


# Printing the adjacency list
def show_adj():
    for node, neighbors in adj.items():
        print(f"adj[{node}]:", end=" ")
        for neighbor, weight in neighbors:
            print(f"({neighbor}, {weight})", end=" ")
        print()


show_adj()
