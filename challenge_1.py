import sys 


class Vertex:

    def __init__(self, v):
        ''' name: representation of the vertex
            neighbors: a list of vertex objects that self connects to '''

        self.name = v
        self.neighbors = set()

    def add_neighbor(self, v):
        ''' adds vertex object to self's neighbor list
            args: v, vertex object '''

        if v not in self.neighbors:
            self.neighbors.add(v)


class Graph:

    def __init__(self):
        ''' vertices: dict containing keys of the vertex names and values of the vertices neighbors name
            edges: dict containing keys of the vertex object and values as the vertex it connects to with a weight in a tuple format (vertexObj, weight)
        '''

        self.vertices = {} 
        self.edges = {}

    def add_vertex(self, v):
        ''' adds vertex to the vertices list values only if the vertex is unique to others
            args:  v, vertex object '''

        if v.name not in self.vertices:
            self.vertices[v.name] = v
        else:
            raise KeyError(f"Tried adding an existing vertex: {v.name}")
        

    def add_edge(self, u, v, weight=1):
        ''' adds v's name into vertices list at u's name
            adds u's name into verices list at v's name
            adds both u and v into each of the neighbor vertex object property
            adds v to u's edge list with weight

            Only if both vertices are already in the vertices list
        '''

        if u.name in self.vertices and v.name in self.vertices:

            # add v to u's neighbors and u to v's neighbors in Vertex class
            v.add_neighbor(u)
            u.add_neighbor(v)

            # add path
            self._add_path(u, v, weight)

    def _add_path(self, from_vert, to_vert, weight=1):
        ''' if from_vert not in the edges dict, add to the dict with an initial tuple of it's neighbor with the weight
            if from_vert is in the edges dict, append the neighbor's tuple to the existing list
            args:   from_vert, a vertex object 
                    to_vert, a vertex object 
                    weight, the edges weight, cost, or time '''

        if from_vert not in self.edges:
            self.edges[from_vert] = [(to_vert, weight)]
        else:
            self.edges[from_vert].append((to_vert, weight))


    def __str__(self):
        ''' returns a string format of the vertices dictionary'''

        return str(self.vertices)


    def form_graph_output(self):
        ''' helper function to print visual output
        e.g.
        G
        1,2,3,4
        (1,2,10)
        (1,4,5)
        (2,3,5)
        (2,4,7) '''

        print("# Vertices: {}".format(len(self.vertices)))
        print("# Edges: {}".format(len(self.edges)))
        print("Edge List:")

        for dict_item in self.edges:
            edges_from_item = self.edges[dict_item]

            for item in edges_from_item:
                print((dict_item.name, item[0].name, item[1]))

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
    with open(sys.argv[1], 'r') as file:

        graph_type = "G"
        graph = Graph()

        for num, line in enumerate(file):
            
            # graph type
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

        return graph.form_graph_output()




if __name__ == "__main__":
    main()