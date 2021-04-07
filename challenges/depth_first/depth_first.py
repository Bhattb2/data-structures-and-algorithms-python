from challenges.graph import Graph


visited = []

def depth_first_graph(visited, graph, vertex):
    

    if vertex not in visited:
        visited.append(vertex)

        for neighbor in graph[vertex]:
            depth_first_graph(visited, graph, neighbor)
    
    return visited
