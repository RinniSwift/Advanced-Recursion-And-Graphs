import sys
import queue

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
        else:
            raise KeyError("Tried adding an existing neighbor")


class Graph:

    def __init__(self):
        ''' vertices: dict containing keys of the vertex names and values of the vertex object { Vertex.name : Vertex }
        '''

        self.vertices = {} 


    def add_edge(self, from_vert, to_vert):
        ''' adds vertex to each others neighbors 
            args:
                from_vert, vertex object at beginning of the path
                to_vert, vertex object at end of the path
        '''
    
        if from_vert.name in self.vertices and to_vert.name in self.vertices:
            from_vert.add_neighbor(to_vert)

    def add_vertex(self, v):
        ''' adds vertex to the vertices list values only if the vertex is unique to others
            args:  v, vertex object '''

        if v.name not in self.vertices:
            self.vertices[v.name] = v
        else:
            raise KeyError(f"Tried adding an existing vertex: {v.name}")


    def __str__(self):
        ''' returns a string format of the vertices dictionary'''

        for item in self.vertices:
            print(f"{item} connects to {[x.name for x in self.vertices[item].neighbors]}")

        return ""


    def dfs_recursive(self, from_vert, to_vert, seen_set=None):
        ''' searches for path that connects both vertices input recursively using the call stack.
            args: from_vert, starting vertex object
                  to_vert, ending vertex object
                  seen_set, set containing all seen vertices
        '''
        if seen_set == None:
            seen_set = set()

        if from_vert == to_vert:
            seen_set.add(from_vert)
            return [x.name for x in seen_set]

        if from_vert not in seen_set:
            seen_set.add(from_vert)
            for neighb in from_vert.neighbors:
                return self.dfs_recursive(neighb, to_vert, seen_set)

        return [x.name for x in seen_set]


    def dfs_iteritive(self, from_vert, to_vert):
        ''' searches for path that connects both vertices input iteratively with a stack.
            args: from_vert, starting vertex object
                  to_vert, ending vertex object
        '''

        seen_set = set()
        stack = [from_vert]

        vertices_in_path = []
        
        while stack:
            vert = stack.pop()

            if vert == to_vert:
                vertices_in_path.append(vert)
                return vertices_in_path

            if vert.neighbors != None:
                vertices_in_path.append(vert)

            for neighb in vert.neighbors:
                if neighb == to_vert:
                    vertices_in_path.append(neighb)
                    return vertices_in_path
                if neighb not in seen_set:
                    stack.append(neighb)
                    seen_set.add(neighb) 

        return []



def main():

    file = sys.argv[1]

    graph = create_graph_from_file(file)
    print(graph)

    from_vert = graph.vertices[sys.argv[2]]
    to_vert = graph.vertices[sys.argv[3]]
    print(graph.dfs_recursive(from_vert, to_vert))

    # print(path)

    # print(f"Vertices in shortest path: {[x.name for x in path]}\nNumber of edges in shortest path: {len(path) - 1}")


def create_graph_from_file(file):
    ''' returns a graph object created from the given file '''
    graph = Graph()


    with open(file, 'r') as f:

        for num, line in enumerate(f):

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
                
                from_vertex = graph.vertices[arr[0]]
                to_vertex = graph.vertices[arr[1]]

                graph.add_edge(from_vertex, to_vertex)

        return graph


if __name__ == "__main__":
    main()