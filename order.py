class Order:
	""" class order awesome"""
	def	__init__(self, id, items, position):
		self.id = id
		self.completed = False
		self.items = items
		self.position = position

	def remove_item(id):
		self.items.remove(id)
