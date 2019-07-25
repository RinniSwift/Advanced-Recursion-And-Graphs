
import queue


'''
Properties

Vertex: vertex object containing an id and it's neighbors

    id: string representation of vertex
    neighbors: set of vertices adjacent to self

Graph: a graph class containing multiple vertexes and paths
    
    vertices: [Vertex] list of all vertices in the graph
    order: total number of vertices in the graph
    edges: [Vertex: [(Vertex, weight)]] a dict of keys being the vertex and value being vertex it connects to with a weight in a tuple format.

'''


class Vertex(object):

    def __init__(self, vertex):
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=1):
        """Add a neighbor along with a weighted edge """

        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'vertex "{self.id}" adjacent to {[ x.id for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        return self.neighbors[vertex]



class Graph:

    def __init__(self):
        self.vertices = set()
        self.order = 0

    def add_vertex(self, v):
        """Add a new vertex object to the graph with the given key and return the vertex """

        self.vertices.add(v)
        self.order += 1
        return v

    def get_vertex(self, v):
        """Return the vertex if it exists """

        # given a vertex object, return the vertex if it is in the graph
        if v in self.vertices:
            return v

    def add_edge(self, from_vert, to_vert, cost=0):
        """add an edge from the given vertex to the other given vertex with a cost """

        if from_vert in self.vertices:
            # adding edge between existing vertices
            if to_vert in self.vertices:
                from_vert.add_neighbor(to_vert, cost)
            # adding edges between an existing node to a new node
            else:
                self.vertices.add(to_vert)
                from_vert.add_neighbor(to_vert, cost)

    def get_vertices(self):
        """return all the vertices in the graph """
        return self.vertices

    def breadth_first_search(self, vertex, n):
        """ run breadth first search starting from the input vertex and going `n` levels deep. Return all nodes found at the `n`th level """

        # initialize an array with the input vertex
        # initialize a set with the input vertex in 
        # if `n` is 1, return all the input array's neighbors
        # if not 1:
            # loop through n amount of times
                # if the amount of times is equivilent to `n`, return all items in the arr

                # loop through the items in the vertex
                    # loop through the neighbors in the vertex
                        # if the neighbor is not in the seen set, add it to there, and append to the arr variable.
                # by now, all previous items in the arr from the last iteration should be removed and updated with the new vertices from the nieghbors of the previous's
                
        arr = [vertex]
        seen_set = set()
        seen_set.add(vertex)

        if n == 1:
            arr = []
            for nei in vertex.neighbors:
                arr.append(nei)
        else: 
            for iteration in range(n + 1):
                if iteration == (n):
                    return [x.id for x in arr]

                values = []
                for item in arr:
                    curr_vert = item
                    for nei in curr_vert.neighbors:
                        if nei not in seen_set:
                            seen_set.add(nei)
                            values.append(nei)

                arr = values

        return [x.id for x in arr]
        

if __name__ == "__main__":

    # Challenge 1: Create the graph


    # create friend vertex objects

    friendOne = Vertex("one")
    friendTwo = Vertex("two")
    friendThree = Vertex("three")
    friendFour = Vertex("four")
    friendFive = Vertex("five")


    # create empty graph

    g = Graph()


    # add friends

    g.add_vertex(friendOne)
    g.add_vertex(friendTwo)
    g.add_vertex(friendThree)
    g.add_vertex(friendFour)
    g.add_vertex(friendFive)

    # Add connections (non weighted edges for now)

    g.add_edge(friendOne, friendTwo)
    g.add_edge(friendTwo, friendThree)
    g.add_edge(friendOne, friendFour)
    g.add_edge(friendTwo, friendFive)


    print(f"vertex '{friendOne.id}', connected to {g.breadth_first_search(friendOne, 2)} with 2 levels down")


    # Challenge 1: Output the vertices & edges
    # Print vertices

    print(f"The vertices are: {[x.id for x in g.vertices] }")
    print(friendOne)







