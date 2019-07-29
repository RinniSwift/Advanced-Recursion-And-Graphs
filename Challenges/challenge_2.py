import sys
import queue

class Vertex:

    def __init__(self, v):
        ''' name: representation of the vertex
            neighbors: a list of vertex objects that self connects to '''

        self.name = v
        self.neighbors = set()
        self.parent = None

    def add_neighbor(self, v):
        ''' adds vertex object to self's neighbor list 
            args:
                v, vertex object
        '''

        if v not in self.neighbors:
            self.neighbors.add(v)

    def add_parent(self, v):
        self.parent = v

class Graph:

    def __init__(self):
        ''' vertices: dict containing keys of the vertex names and values of the vertex object { Vertex.name : Vertex } '''

        self.vertices = {}

    def add_vertex(self, v):
        ''' adds vertex to the vertices list values only if the vertex is unique to others 
            args:
                v, vertex object 
        '''

        if v.name not in self.vertices:
            self.vertices[v.name] = v
        else:
            raise KeyError("Tried adding an existing vertex")

    def add_edge(self, from_vert, to_vert):
        ''' adds vertex to each others neighbors 
            args:
                from_vert, vertex object at beginning of the path
                to_vert, vertex object at end of the path
        '''
    
        if from_vert.name in self.vertices and to_vert.name in self.vertices:
            from_vert.add_neighbor(to_vert)
            to_vert.add_neighbor(from_vert)


    def __str__(self):
        ''' a string format of all the vertices in the graph with it's neighbors '''

        for vert in self.vertices:
            print(f"vertex '{vert}' contains neighbors: {[x.name for x in self.vertices[vert].neighbors]}")
        return ""


    def bfs(self, from_vert, to_vert):
        ''' returns a list of all vertices in the shortest path from starting and ending vertex indicated by the parameters '''

        path_of_vertices = []
        q = queue.Queue()
        seen_set = set()

        q.put(from_vert)

        while q:
            curr_vert = q.get()
            
            if curr_vert == to_vert:
                break

            for neighb in curr_vert.neighbors:
                if neighb not in seen_set:
                    neighb.add_parent(curr_vert)
                    # neighb.parent = curr_vert
                    q.put(neighb)
                    seen_set.add(curr_vert)
                
        while curr_vert is not None:
            path_of_vertices.append(curr_vert.name)
            curr_vert = curr_vert.parent

        return path_of_vertices[::-1]


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
        # for vert in graph.vertices:
        #     print(f"vertex {vert} contains:")
        #     neighborings = graph.vertices[vert].neighbors
        #     for neighb in neighborings:
        #         print(f"  {neighb.name}")

        print(graph)
        print(graph.bfs(graph.vertices[sys.argv[2]], graph.vertices[sys.argv[3]]))

        



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