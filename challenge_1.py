
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
        self.edges = {}

    def add_vertex(self, vertex):
        ''' If vertex not in vertices list, add with empty naighbors '''
        if vertex not in self.vertices:
            self.vertices[vertex.name] = []

    def add_edge(self, u, v, weight=1):
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

            # add_path
            self.add_path(u, v, weight)

    def add_path(self, from_vert, to_vert, weight=1):
        if from_vert not in self.edges:
            self.edges[from_vert] = [(to_vert, weight)]
        else:
            self.edges[from_vert].append((to_vert, weight))


    def __str__(self):
        return str(self.vertices)


    def form_graph_output(self):
        print("# Vertices: {}".format(len(self.vertices)))
        print("# Edges: {}".format(len(self.edges)))
        print("Edge List:")


# friendOne = Vertex("one")
# friendTwo = Vertex("two")
# friendThree = Vertex("three")
# friendFour = Vertex("four")


# graph = Graph()

# graph.add_path(friendOne, friendTwo, 5)
# graph.add_path(friendTwo, friendThree)
# graph.add_path(friendOne, friendFour)

# # graph.add_edge(friendOne, friendTwo)

# for item in graph.edges:
#     print(item.name)
#     edges_from_item = graph.edges[item]

#     for it in edges_from_item:
#         print("edge: ({}, {}) with weight of: {}".format(item.name, it[0].name, it[1]))
    


'''
line 1 indicate with 'G' or 'D'. 'G': graph (undirected graph). 'D': Diagram (directed graph)
line 2 indicating all the vertex numbers
line 3+ indicating the edges with a weight


graph_data.txt file format:

G
1,2,3,4
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)

'''
def main():
    with open('graph_data.txt', 'r') as file:

        graph_type = "G"
        graph = Graph()


        for num, line in enumerate(file):
            
            # number type
            if num == 0:
                graph_type = line[0]

            # vertex list
            elif num == 1:

                stripped = line.strip()

                for item in stripped:
                    if item != ",":     # todo: create algorithm for more a name more than one space
                        vert = Vertex(item)
                        graph.add_vertex(vert)

            elif num > 1:

                strip_brackets = line.replace('(', '').replace(')', '')
                stripped = strip_brackets.strip()
                arr = stripped.split(',')
                
                from_vertex = Vertex(arr[0])
                to_vertex = Vertex(arr[1])

                graph.add_edge(from_vertex, to_vertex, arr[2])


        for item in graph.edges:
            edges_from_item = graph.edges[item]

            for it in edges_from_item:
                print("edge: ({}, {}) with weight of: {}".format(item.name, it[0].name, it[1]))




if __name__ == "__main__":
    main()








