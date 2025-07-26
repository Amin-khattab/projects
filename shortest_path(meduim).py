# this is done manually to compare the diffrence between checking the neighbors manually and automatically
# just take a look at the shortest_path(mid) to see the diffrence

graph = {
    "A": {"B": 2, "C": 3},
    "B": {"D": 1, "C": 3},
    "C": {"D": 4},
    "D": {}
}

def main(gragh,start,end):

    path = [start]
    current = start
    total_distance = 0

    while current != end:
        neighbor = list(gragh[current].keys())

        if len(neighbor) > 1 :

            first_neighbor = neighbor[0]
            second_neighbor = neighbor[1]

            first_dist = gragh[current][first_neighbor]
            second_dist = gragh[current][second_neighbor]

            if first_dist > second_dist:
                distance = second_dist
                next_node = second_neighbor
            else:
                distance = first_dist
                next_node = first_neighbor

            total_distance = total_distance + distance
            path.append(next_node)
            current = next_node
        else:
            next_node = list(gragh[current].keys())[0]
            distance = gragh[current][next_node]
            total_distance = total_distance + distance
            path.append(next_node)
            current = next_node

    return path,total_distance
path,dist = main(graph,"A","D")

print(path)
print(dist)
