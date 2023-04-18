import queue as q

def Astar(graph, heuristic, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return 0
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return 0

    heu = heuristic[start]

    queue = q.PriorityQueue()
    queue.put((heu, 0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[2][len(node[2]) - 1]

        if end in node[2]:
            print("\nPath found: " + str(node[2]) + "\n--> Cost = " + str(node[1]))
            break

        cost = node[1]
        for neighbor in graph[current]:
            temp = node[2][:]
            temp.append(neighbor)
            cur_cost = cost + graph[current][neighbor]
            heu = heuristic[neighbor] + cur_cost
            print("visiting node is = " + str(neighbor) + "\n--> h(n) + g(n) = " + str(heu) + " --> Cost = " + str(cur_cost))
            queue.put((heu, cur_cost, temp))


def read_Graph():
    mapfile = open("map.txt", "r+")
    graph = {}
    heuristic = {}
    for line in mapfile:
        separater = line.split(",")
        cities = separater[0]
        heuristic_value = separater[1]
        tokens = cities.split()
        node = tokens[0]
        heuristic[str(tokens[0])] = int(heuristic_value)
        graph[node] = {}

        for i in range(1, len(tokens) - 1, 2):
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph, heuristic

def main():
    graph, heu = read_Graph()
    print("Graph :"+ str(graph))
    print("\nHeuristic Value = " + str(heu) + "\n\n")
    Astar(graph, heu, 'Arad', 'Bucharest')

if __name__ == "__main__":
    main()

