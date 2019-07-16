#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""


class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        # TODO check if vertex is already a neighbor
        # TODO if not, add vertex to neighbors and assign weight.

        if vertex not in neighbors:
            neighbors.add((vertex, weight))

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # TODO return the neighbors
        return self.neighbors

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # TODO return the weight of the edge from this
        # vertex to the given vertex.
        for neighb in self.neighbors:
            if neighb[0] == vertex:
                return neighb[1]



""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # TODO increment the number of vertices
        # TODO create a new vertex
        # TODO add the new vertex to the vertex list
        # TODO return the new vertex

        vert = Vertex(key)

        self.vertList[vert] = []
        self.numVertices += 1

        return vert

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # TODO return the vertex if it is in the graph

        return self.vertList[key]

    def add_edge(self, key1, key2, cost=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a cost."""
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

        vert1 = Vertex(key1)
        vert2 = Vertex(key2)

        if self.vertList[vert1] != None:
            self.vertList[vert1].append(vert2)
            vert1.add_neighbor(vert2, cost)
            vert2.add_neighbor(vert1, cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")


    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        print(v)
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))







