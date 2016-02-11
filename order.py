class Order:
	""" class order awesome"""
	def	__init__(self, id, items, position):
		self.id = id
		self.completed = False
		self.items = items
		self.position = position
		self.sub_orders = [SubOrder(self.id, self.items, self.position)]

	def remove_item(self, item):
		self.items.remove(item)

	def weight(self):
		total_weight = 0
		for item in self.items:
			total_weight += item.weight
		return total_weight

	def split_order(self):
		self.sub_orders = []
		for i in self.items:
			self.sub_orders.append(SubOrder(self.id, [i], self.position))

class SubOrder():
	def	__init__(self, id, items, position):
		self.id = id
		self.completed = False
		self.items = items
		self.position = position

	def remove_item(self, item):
		self.items.remove(item)

	def weight(self):
		total_weight = 0
		for item in self.items:
			total_weight += item.weight
		return total_weight

