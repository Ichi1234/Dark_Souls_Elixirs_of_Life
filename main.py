# 31 vertices , 66 edges

# this example come from elab
original_adj = {0: [(1, 10), (2, 2), (3, 7)], 1: [], 2: [(3, 2), (4, 5)],
                3: [(0, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 6)]}

# this example similar to my real data
adj = {0: [(1, 10), (2, 2), (3, 7), (4, 4)], 1: [(0, 10), (4, 4)], 2: [(0, 2), (3, 2), (4, 5)],
       3: [(0, 7), (2, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 5), (3, 1)]}

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

show_adj()
def decrease_key(vertex_id, new_distance):
    """Use for update new distance for bag"""
    for i, (vertex_in_bag, dist_v) in enumerate(bag):
        if vertex_in_bag == vertex_id:
            bag[i] = (vertex_id, new_distance)
            break
    bag.sort(key=lambda x: x[1])  # sort bag base on distance


def item_finder_dijkstra(first_vertex):
    """this code is base on dijikstra algorithm. However, this dijikstra determine on a
    weight and numbers of items that are in the vertice"""

    for _ in range(len(adj)):
        dist.append(9999999) # set initial value
        parent.append(-1)

    dist[first_vertex] = 0  # set first vertex

    for j in range(len(adj)):
        bag.append((j, dist[j]))

    bag.sort(key=lambda x: x[1])  # put first_vertex that user choose to front of the list

    while bag:
        u = bag.pop(0)[0]
        for num_pair in adj[u]:
            v = num_pair[0]
            weight = num_pair[1]

            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                decrease_key(v, dist[v])


item_finder_dijkstra(2)
print(dist)
print(parent)
