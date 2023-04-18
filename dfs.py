graph = {
            0: [1, 2, 3, 4],
            1: [0, 5],
            2: [0, 5],
            3: [0, 6],
            4: [0, 6],
            5: [1, 2, 7],
            6: [3, 4, 7],
            7: [5, 6],
}
def dfs(graph, start):  
    explored = [] 
    queue = [start] 
    print(queue)   
    while queue:
        print("queue : ", queue)
        node = queue.pop() 
        print("explored : ", explored)
        if node not in explored: 
         
            explored.append(node) 
            neighbours = graph[node]  
        
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)  
    return explored
print(dfs(graph, 4))
