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
def add_neighbor(self, v)
```
> adds `Vertex` (v) to *self*'s neighbors set


### Graph

*graph object containing multiple vertices*

```python
class Graph:
   
   def __init__(self):
      self.vertices = {}
      self.edges = {}
```
> `vertices`: dictionary with *key* of vertex's name and *value* of the `Vertex` \
> `edges`: dictionary with *key* of `Vertex` and *value* of an array of tuples where the tuple at 0 is the `Vertex` it connects to with the tuple at 1 is the weight the both vertices connect with

---

### About

How to call the function:\
`python3 challenge_1.py graph_data.txt` 
Pass in the text file after the file.

Text file format:
```
G
1,2,3,4
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)
```

Return output:
```
# Vertices: 4
# Edges: 4
Edge List:
('1', '2', '10')
('1', '4', '5')
('2', '3', '5')
('2', '4', '7')
```