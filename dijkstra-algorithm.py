graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

start = "A"
target = "F"

unvisited = set(graph.keys())
distances = {node : float("inf") for node in graph}
distances[start] = 0

while unvisited:
    current_node = None
    current_distance = float("inf")

    for node in unvisited:
        if distances[node] < current_distance:
            current_distance = distances[node]
            current_node = node

    if current_node is None:
        break

    unvisited.remove(current_node)

    for neighbor, weight in graph[current_node].items():
        if neighbor in unvisited:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

print(f"Shortest distance from {start} to {target} is: {distances[target]}")
