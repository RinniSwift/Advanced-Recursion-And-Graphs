
with open('graph_data.txt', 'r') as file:
    data = file.read()



class Vertex:

    def __init__(self, v):
        self.name = v
        self.neighbors = set()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.add(v)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        ''' If vertex not in vertices list, add with empty naighbors '''
        if vertex not in self.vertices:
            self.vertices[vertex.name] = []

    def add_edge(self, u, v):
        ''' In an undirected graph, add u to v's neighbors and v to u's neighbors.
            In a directed graph, add v to u's neighbor.

            and add v to u's neighbor in the Vertex class
        '''

        if u.name in self.vertices and v.name in self.vertices:

            # add v to u neighbors in self.vertices
            if v.name not in self.vertices[u.name]:
                self.vertices[u.name].append(v.name)
            # add u to v neighbors in self.vertices
            if u.name not in self.vertices[v.name]:
                self.vertices[v.name].append(u.name)

            # add v to u's neighbors and u to v's neighbors in Vertex class
            v.add_neighbor(u)
            u.add_neighbor(v)


    def __str__(self):
        return f'{self.vertices}'


friendOne = Vertex("one")
friendTwo = Vertex("two")
friendThree = Vertex("three")
friendFour = Vertex("four")


graph = Graph()

graph.add_vertex(friendOne)
graph.add_vertex(friendTwo)
graph.add_vertex(friendThree)
graph.add_vertex(friendFour)

graph.add_edge(friendOne, friendTwo)

print(graph)









