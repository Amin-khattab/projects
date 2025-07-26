graph = {
    "A" : {"B":2},
    "B" : {"C":3},
    "C" : {"D":1},
    "D" : {}
}


def main(graph,start,end):

    current = start
    total_dist = 0
    path = [start]

    neighbor = graph[current]
    if not neighbor:
        return None,float("inf")
        
    while current != end:
        next_node = list(graph[current].keys())[0]
        distance = graph[current][next_node]
        total_dist += distance
        path.append(next_node)
        current = next_node

    return path,total_dist

path,dist = main(graph,"A","D")
print(path)
print(dist)
