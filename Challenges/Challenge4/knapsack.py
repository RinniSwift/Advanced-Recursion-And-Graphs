
class Item():
	'''
		Item object containing a name, weight, and value correlated to the item. This object represents items in the knapsack.
	'''

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
	
	# if items is empty or capacity is down to 0, can't add any other items so we return a tuple where at [0] is the value and at [1] is the list of items in the knapsack
	if len(items) == 0 or C == 0:
		return (0, [])

	# grab first item in the items list
	item = items[0]

	# if the item's weight is greater than the capacity, call the fucntion again without this item contained in
	if item.weight > C:
		return knapsack(C, items[1:])

	# by this point, the item can be added into the knapsack without exceeding the capacity
	# calculate the total value containing the item
	val_with_item, items_used_with = knapsack(C - item.weight, items[1:])
	val_with_item += item.value

	# calculate the total value without containing the item
	val_without_item, items_used_without = knapsack(C, items[1:])

	# if the value with the item is greater, than the item without, add to the total items in the knapsack list 
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