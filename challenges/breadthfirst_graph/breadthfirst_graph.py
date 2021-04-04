from breadthfirst_graph.graph import Node, Queue

class Vertex:
    """
    This is equivalent to a NOde...
    """
    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, end_vertex, weight=1):
        self.vertex = end_vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    
    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex


    def add_edge(self, start_vertex, end_vertex, weight=1):

        #check if start and end vertices are in the adjancy_list
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError('Start or End Vertex not in the graph')


        edge = Edge(end_vertex, weight)
        adjancencies = self.adjancecy_list[start_vertex]
        adjancencies.append(edge)


    def size(self):
        return len(self.adjacency_list)


    def get_vertices(self):
        """
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        output = []

        for vertex in self.adjacency_list:
            output.append(vertex.value)

        return output


        def get_neighbors(self, vertex):
            """
        Returns a collection of edges connected to the given node
        Takes in a given node
        Include the weight of the connection in the returned collection
        """
        output = []
        
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                output.append([neighbor.vertex.value, neighbor.weight])
                                
        return output

    def breadthfirst_graph(self, vertex):

        output = []

        vertices = self.get_neighnor(vertex)

        for item in vertices:
            output.append(item[0]) 



if __name__ == "__main":
    trip = Graph


