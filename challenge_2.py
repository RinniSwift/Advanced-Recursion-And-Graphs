
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





            