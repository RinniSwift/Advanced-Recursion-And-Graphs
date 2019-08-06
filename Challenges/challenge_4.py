
class Item():

	def __init__(self, name, w, v):
		self.name = name
		self.weight = w
		self.value = v

def knapsack(C, items):
	''' A  method to determine the maximum value of the items included in the knapsack 
	without exceeding the capacity C

	    Parameters: 
	    C= 50
	    items = (("boot", 10, 60),
	         ("tent", 20, 100),
	         ("water", 30, 120),
	         ("first aid", 15, 70))
	    val = the maximum value
	    n = 0 (the index of the item you're looking at)
	    Returns: max value
	'''
	

	if len(items) == 0 or C == 0:
		return (0, [])


	item = items[0]

	if item.weight > C:
		return knapsack(C, items[1:])

	val_with_item, items_used_with = knapsack(C - item.weight, items[1:])
	val_with_item += item.value

	val_without_item, items_used_without = knapsack(C, items[1:])

	if val_with_item >= val_without_item:
		items_used_with.append(item.name)
		return (val_with_item, items_used_with)

	return (val_without_item, items_used_without)


items = [Item("boot", 10, 60),
		 Item("tent", 20, 100),
		 Item("water", 30, 120),
		 Item("first aid", 15, 70)]



def main():
	values = knapsack(50, items)

	print(f"The value of the optimal solution to the knapsack problem is: {values[0]}")
	print(f"The items included in the knapsack for this optimal solution are {values[1]}")

if __name__ == "__main__":
    main()