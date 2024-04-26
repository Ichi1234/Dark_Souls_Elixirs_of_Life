# 31 vertices , 66 edges

# this example come from elab (start vertex = 1)
original_adj = {0: [(1, 10), (2, 2), (3, 7)], 1: [], 2: [(3, 2), (4, 5)],
                3: [(0, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 6)]}

# this example similar to my real data
adj = {0: [(1, 10), (2, 2), (3, 7), (4, 4)], 1: [(0, 10), (4, 4)], 2: [(0, 2), (3, 2), (4, 5)],
       3: [(0, 7), (2, 2), (4, 1)], 4: [(0, 4), (1, 4), (2, 5), (3, 1)]}

items_container = [2, 0, 2, 3, 1]
current_amount_of_items = []
dist = []
bag = []
shortest_path = {0: [], 1: [], 2: [],
                 3: [], 4: []}


# Printing the adjacency list
def show_adj():
    """this function use to show relationship between each vertex"""
    for node, neighbors in adj.items():
        print(f"adj[{node}]:", end=" ")
        for neighbor, weight in neighbors:
            print(f"({neighbor}, {weight})", end=" ")
        print()


def decrease_key(vertex_id, new_distance):
    """Use for update new distance for bag"""
    for i, (vertex_in_bag, dist_v) in enumerate(bag):
        if vertex_in_bag == vertex_id:
            bag[i] = (vertex_id, new_distance)
            break
    bag.sort(key=lambda x: x[1])  # sort bag base on distance


def item_finder_dijkstra(first_vertex, find_num_items, best_path=None):
    """This code is base on dijikstra algorithm. However, this algorithm aims to find which paths
    is the shortest path and best path to find num_items that are in each vertex"""
    shortest_path.update({0: [], 1: [], 2: [],
                          3: [], 4: []})
    dist.clear()
    bag.clear()
    current_amount_of_items.clear()

    for _ in range(len(adj)):
        dist.append(9999999)  # set initial value
        current_amount_of_items.append([])

    dist[first_vertex] = 0  # set first vertex

    for j in range(len(adj)):
        bag.append((j, dist[j]))

    bag.sort(key=lambda x: x[1])  # put first_vertex that user choose to front of the list

    while bag:
        u = bag.pop(0)[0]
        for num_pair in adj[u]:
            v = num_pair[0]
            weight = num_pair[1]

            # choose path that higher item or path that shorter
            if items_container[u] / (dist[u] + weight) > items_container[v] / (dist[v] + 1e-9) or \
                    dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                decrease_key(v, dist[v])
                shortest_path[v].append(u)  # add connect vertex and amount of items
                current_amount_of_items[v].append(items_container[u])

    # add end vertex to shortest_path variable
    for index, value in shortest_path.items():
        if value:
            value.append(index)
            current_amount_of_items[index].append(items_container[index])
    print(shortest_path)
    # find which path is shortest
    result_path = [(i, items) for i, items in enumerate(current_amount_of_items) if
                   items and sum(items) >= find_num_items]
    print(result_path)
    print(f"this is items {current_amount_of_items}")
    # if the path >= num_items return it else back tracking to find more item
    if result_path:
        result = min(result_path, key=lambda x: len(x[1]))  # Return the path with the minimum length
        print(f"result from true {result}")
        print()
        print(best_path + shortest_path[result[0]])
        return best_path + shortest_path[result[0]]

    else:
        # back tracking
        recursive_path = max(enumerate(current_amount_of_items),
                             key=lambda x: sum(x[1]))  # The path with the maximum item sum
        target_path = shortest_path[recursive_path[0]]
        print(f"result from false {target_path}")
        print()
        for i in target_path:
            items_container[i] = 0

        return item_finder_dijkstra(recursive_path[0], find_num_items - sum(recursive_path[1]),
                                    shortest_path[recursive_path[0]])


def backtracking(result_from_dijkstra, current_sum):
    """This function use when the result of dijkstra not achieves user desired_number"""

    vertex, achieve = item_finder_dijkstra(result_from_dijkstra, current_sum)
    print()
    print(items_container)
    print(vertex, achieve)


vertex = item_finder_dijkstra(4, 8)

print(vertex)
