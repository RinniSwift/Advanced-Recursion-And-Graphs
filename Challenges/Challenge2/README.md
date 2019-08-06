### Vertex

*representation of nodes on the graph*


```python
class Vertex:

   def __init__(self, v):
      self.name = v
      self.neighbors = set()
      self.parent = None
```
> `name`: representation string of vertex object\
> `neighbors`: a set of `Vertex` *objects* self connects to\
> `parent`: a helper bfs method that stored the `Vertex` parent of self.


```python
def add_neighbor(self, v):
def add_parent(self, v):
```
> adds `Vertex` (v) to *self*'s neighbors set\
> sets *self*'s parent to the `Vertex` (v)


### Graph

*graph object containing multiple vertices*

```python
class Graph:
   
   def __init__(self):
      self.vertices = {}
```
> `vertices`: dictionary with *key* of vertex's name and *value* of the `Vertex` 


```python
def bfs(self, from_vert, to_vert):
```
> `from_vert`: vertex object indicating the starting vertex\
> `to_vert`: vertex object indicating the ending vertex\
> returns a string format of all vertices in the shortest path from starting and ending vertex.

---

### About

How to call the function:\
`python3 challenge_2.py graph_data_directed.txt 1 5` 
Pass in the text file after the file along with the vertex name of start to end.

Text file format:
```
G
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(2,5)
(3,5)
```

Return output:
```
Vertices in the shortest path: ['1', '4', '2', '5']
Number of edges in shortest path: 3 
```