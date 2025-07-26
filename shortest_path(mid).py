graph = {
    "A": {"B": 2, "C": 4},
    "B": {"C": 3, "E": 1},
    "C": {"D": 2},
    "D": {"E": 1},
    "E": {}
}

def main(graph,start,end):

    current = start
    path = [start]
    total_distance = 0

    while current != end:
        neighbor = graph[current]
        if not neighbor:
            return None,float("inf")

        next_node = min(neighbor, key=lambda n : neighbor[n])
        distance = graph[neighbor][next_node]
        total_distance += distance
        path.append(next_node)
        current = next_node

    return path,total_distance

path,dist = main(graph, "A", "E")

print(path)
print(dist)
