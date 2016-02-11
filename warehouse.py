class Warehouse:
	""" warehouse cool
		position
		stock [{item_id:qty}]
	"""
	def __init__(self, id, position, stock):
		self.position = position
		self.stock = {}
		self.id  = id
		for i, j in zip(range(1, len(stock)), stock):
			self.stock[i] = j

	def take_item(item_id):
		if(self.stock[item_id] == 0):
			return -1
		else:
			self.stock[item_id] -= 1
			return 0

	def add_item(item_id):
		self.stock[item_id] += 1