
'''
Properties

Vertex: vertex object containing an id and it's neighbors

    id: String
    neighbors: [Vertex: weight] a list of dictionaries with the key being the neighbor vertex and value being the weight


Graph: a graph class containing multiple vertexes and paths
    
    vertices: [Vertex] a list of all vertexes in the graph
    order: total number of vertices in the graph
    edges: [Vertex: [(Vertex, weight)]] a dict of keys being the vertex and value being vertex it connects to with a weight in a tuple format.

'''


class Vertex(object):

    def __init__(self, vertex):
        self.id = vertex
        self.neighbors = [] 

    def add_neighbor(self, vertex, weight=1):
        """Add a neighbor along with a weighted edge.
        . add neighbor if not in neighbor list
        . update weight if already exists in neighbor list """

        if vertex not in self.neighbors:
            self.neighbors.append({vertex: weight})
        else:
            self.neighbors[vertex] = weight 


    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[ x for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        for neighb in self.neighbors:
            if neighb[0] == vertex:
                return neighb[1]



class Graph:

    def __init__(self):
        self.vertices = set()
        self.order = 0

    def add_vertex(self, v):
        """Add a new vertex object to the graph with the given key and return the vertex.
        args: v, vertex object """

        self.vertices.add(v)
        self.order += 1
        return v

    def get_vertex(self, v):
        """Return the vertex if it exists
        args: v, vertex object"""

        # given a vertex object, return the vertex if it is in the graph
        if v in self.vertices:
            return v

    def add_edge(self, from_vert, to_vert, cost=0):
        """add an edge from the given vertex to the other given vertex with a cost.
        args:   from_vert, vertex object
                to_vert, vertex object 
        . from_vert must be initially in the graph
        . if to_vert isn't a vertex in the graph, create one and add to each neighbor
        . if to_vert is initially in the graph, add to each neighbor
        """

        if from_vert in self.vertices:
            if to_vert in self.vertices:
                from_vert.add_neighbor(to_vert, cost)
            else:
                self.vertices.add(to_vert)
                from_vert.add_neighbor(to_vert, cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertices



if __name__ == "__main__":

    # Challenge 1: Create the graph


    # create friend vertex objects

    friendOne = Vertex("one")
    friendTwo = Vertex("two")
    friendThree = Vertex("three")
    friendFour = Vertex("four")


    # create empty graph

    g = Graph()


    # add friends

    g.add_vertex(friendOne)
    g.add_vertex(friendTwo)
    g.add_vertex(friendThree)
    g.add_vertex(friendFour)

    # Add connections (non weighted edges for now)

    g.add_edge(friendOne, friendTwo)
    g.add_edge(friendTwo, friendThree)
    g.add_edge(friendOne, friendFour)


    # Challenge 1: Output the vertices & edges
    # Print vertices

    print(f"The vertices are: {[x.id for x in g.vertices] }")
    print(friendOne)


    # Print edges

    print("The edges are: ")
    # for v in g:
    #     print(v)
    #     if len(v) > 0:
    #         for w in v.get_neighbors():
    #             print("( %s , %s )" % (v.getId(), w.getId()))







