import sys

class Vertex:

    def __init__(self, v):
        ''' name: representation of the vertex
            neighbors: a list of vertex objects that self connects to '''

        self.name = v
        self.neighbors = set()

    def add_neighbor(self, v):
        ''' adds vertex object to self's neighbor list '''
        # args: 
        #   v, vertex object

        if v not in self.neighbors:
            self.neighbors.add(v)


class Graph:

    def __init__(self):
        ''' vertices: dict containing keys of the vertex names and values of the vertex
            { Vertex.name : Vertex } '''

        self.vertices = {}

    def add_vertex(self, v):
        ''' adds vertex to the vertices list values only if the vertex is unique to others '''
        # args:  
        #   v, vertex object 

        if v.name not in self.vertices:
            self.vertices[v.name] = v
        else:
            raise KeyError(f"Tried adding an existing vertex: {v.name}")

    def add_edge(self, from_vert, to_vert):
        ''' adds vertex to each others neighbors '''
    
        if from_vert.name in self.vertices and to_vert.name in self.vertices:
            from_vert.add_neighbor(to_vert)
            to_vert.add_neighbor(from_vert)


    def __str__(self):
        ''' returns a string format of the vertices dictionary'''

        return str(self.vertices)


    def bfs(self, from_vert, to_vert):
        pass



def main():

    # file from terminal argv
    with open(sys.argv[1]) as file:

        # undirected, unweighted graph
        graph = Graph()

        # loop through the files lines
        for num, line in enumerate(file):

            if num == 1:
 
                for item in line.strip():
                    if item != ",":     # todo: create algorithm for a name more than one character
                        vert = Vertex(item)
                        graph.add_vertex(vert)

            elif num > 1:

                strip_brackets = line.replace('(', '').replace(')', '').strip()
                arr = strip_brackets.split(',')
                
                from_vertex = graph.vertices[arr[0]]
                to_vertex = graph.vertices[arr[1]]

                graph.add_edge(from_vertex, to_vertex)


        # sample testing
        for vert in graph.vertices:
            print(f"vertex {vert} contains:")
            neighborings = graph.vertices[vert].neighbors
            for neighb in neighborings:
                print(f"  {neighb.name}")

        



if __name__ == "__main__":
    main()


'''

terminal call: python3 challenge_2.py graph_data_unweighted_undirected.txt 1 6

argv[1] : textfile
argv[2] : from_vertex
argv[3] : to_vertex

Text file input format:

line 1 indicate with 'G' as a undirected and unweighted graph
line 2 indicating all the vertex names
line 3+ indicating the edges it connects

G
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(2,5)
(3,5)

'''