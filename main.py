# 31 vertices , 66 edges
original_adj = {0: [(1, 10), (2, 2), (3, 7)], 1: [], 2: [(3, 2), (4, 5)], 3: [(0, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 6)]}

adj = {0: [(1, 10), (2, 2), (3, 7)], 1: [], 2: [(3, 2), (4, 5)], 3: [(4, 1)], 4: [(0, 4), (1, 4)]}
item_container = [2, 0, 2, 3, 1, 2]
dist = []
bag = []
parent = []


# Printing the adjacency list
def show_adj():
    for node, neighbors in adj.items():
        print(f"adj[{node}]:", end=" ")
        for neighbor, weight in neighbors:
            print(f"({neighbor}, {weight})", end=" ")
        print()


def decrease_key(vertex_id, new_distance):
    pass


def item_finder_dijkstra():
    """this code is base on dijikstra algorithm. However, this dijikstra determine on a
    weight and numbers of items that are in the vertice"""

    for _ in range(len(adj)):
        dist.append(9999999)
        parent.append(-1)

    dist[0] = 0

    for j in range(len(adj)):
        bag.append((j, dist[j]))

    while bag:
        u = bag.pop(0)[0]
        for num_pair in adj[u]:
            v = num_pair[0]
            weight = num_pair[1]

            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                decrease_key(v, dist[v])


item_finder_dijkstra()
print(dist)

