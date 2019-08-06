## Depth First Search
*Finding if graph contains a path from start vertex to end vertex using dfs by returning all vertices in the path*

### Vertex

*representation of nodes on the graph*


```python
class Vertex:

   def __init__(self, v):
      self.name = v
      self.neighbors = set()
```
> `name`: representation string of vertex object\
> `neighbors`: a set of `Vertex` *objects* self connects to


```python
def add_neighbor(self, v):
```
> adds `Vertex` (v) to *self*'s neighbors set


### Graph

*graph object containing multiple vertices*

```python
class Graph:
   
   def __init__(self):
      self.vertices = {}
```
> `vertices`: dictionary with *key* of vertex's name and *value* of the `Vertex` 


```python
def dfs_iterative(self, from_vert, to_vert):
```
> `from_vert`: vertex object indicating the starting vertex\
> `to_vert`: vertex object indicating the ending vertex\
> returns an array containing all vertex objects in the path from start vertex to end vertex.

```python
def dfs_recursive(self, from_vert, to_vert, seen_set=None):
```
> `from_vert`: vertex object indicating the starting vertex\
> `to_vert`: vertex object indicating the end vertex\
> `seen_set`: a set containing all seen vertices in the path

---

### About

How to call the function:\
`python3 challenge_3.py graph_data_directed.txt 1 5` 
Pass in the text file after the file along with the vertex name of start to end.

Text file format:
```
D
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(3,5)
(5,2)
```