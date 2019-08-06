# Knapsack problem

[knapsack.py](https://github.com/RinniSwift/Advanced-Recursion-And-Graphs/blob/master/Challenges/Challenge4/knapsack.py)

*A  method to determine the maximum value of the items included in the knapsack without exceeding the capacity*

```python
def knapsack(C, items):
```

> `C`: the maximum weight capacity the knapsack can contain\
> `items`: an array of all items the knapsack can contain as `Item` objects


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
 ```

> Output:
> "The value of the optimal solution to the knapsack problem is: 230"\
> "The items included in the knapsack for this optimal solution are: ['first aid', 'tent', 'boat']"


# Edit Distance

[editDistance.py](https://github.com/RinniSwift/Advanced-Recursion-And-Graphs/blob/master/Challenges/Challenge4/edit_distance.py)

*A method to determine the minimum amount of edits between to convert str_1 to str_2*

```python
def edit_distanct(str_1, str_2, m, n)
```

> `str_1`: string 1\
> `str_2`: string 2\
> `m`: character length of string 1\
> `n`: character length of string 2

```python
str1 = "happy"
str2 = "happpy"
print(edit_distance(str1, str2, len(str1), len(str2)))

str_1 = "sunday"
str_2 = "saturday"
print(edit_distance(str_1, str_2, len(str_1), len(str_2)))
```

> Output:
> 1
> 3

