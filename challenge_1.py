class Vertex:

    def __init__(self, v):
        self.name = v
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)


class Graph:
    self.vertices = {}

    def add_vertex(self, vertex):
        '''Given input should already be a vertex object'''
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, u, v):
        # makes sure it's in the dictionary before adding it
        if u in self.vertices and v in self.vertices:
            # go through the vertices to get to the vertex of u and v
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)

    def print_graph(self):
        for pair in self.vertices.keys():
            print(self.vertices.values())