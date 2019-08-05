
class Item(self, name, w, v):

	def __init__(self, name, w, v):
		self.name = name
		self.weight = w
		self.value = v

def knapsack(C, items, n):
	''' A  method to determine the maximum value of the items included in the knapsack 
	without exceeding the capacity C

	    Parameters: 
	    C= 50
	    items = (("boot", 10, 60),
	         ("tent", 20, 100),
	         ("water", 30, 120),
	         ("first aid", 15, 70))
	    n = 0 (the index of the item you're looking at)
	    Returns: max value
	'''


