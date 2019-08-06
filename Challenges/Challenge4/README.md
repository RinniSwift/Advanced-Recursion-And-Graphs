# Knapsack problem

[knapsack.py](https://github.com/RinniSwift/Advanced-Recursion-And-Graphs/blob/master/Challenges/Challenge4/knapsack.py)

*A  method to determine the maximum value of the items included in the knapsack without exceeding the capacity*

```python
def knapsack(C, items):
```

`C`: the maximum weight capacity the knapsack can contain

`items`: an array of all items the knapsack can contain as `Item` objects


```python
class Item():

   def __init__(self, name, w, v):
      self.name = name
      self.weight = w
      self.value = v
```



Output of the maximum value of items without exceeding the maximum weight capacity with the item names.

```python
items = [Item("boot", 10, 60),
	 Item("tent", 20, 100),
	 Item("water", 30, 120),
	 Item("first aid", 15, 70)]
knapsack(50, items)

"The value of the optimal solution to the knapsack problem is: 230"
"The items included in the knapsack for this optimal solution are: ['first aid', 'tent', 'boat']"
 ```
