class Warehouse:
	""" warehouse cool
		position
		stock [{item_id:qty}]
	"""
	def __init__(self, id, position, stock):
		self.position = position
		self.stock = {}
		self.id  = id
		self.drones = []
		for i, j in zip(range(0, len(stock)), stock):
			self.stock[i] = j

	def has(self, items_list):
		item_id_to_qty = [0] * len(self.stock)
		for item in items_list:
			item_id_to_qty[item.id] += 1

		for item_id, item_qty in enumerate(item_id_to_qty):
			if self.stock[item_id] < item_qty:
				return False
		return True

	def take_item(self, item_id):
		if(self.stock[item_id] == 0):
			return -1
		else:
			self.stock[item_id] -= 1
			return 0

	def add_item(self, item_id):
		self.stock[item_id] += 1

