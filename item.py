class Item(object):
   def __init__(self, id, weight):
      self.id = id
      self.weight = weight

   def __str__(self):
      return "Item [ID %d] [Weight %d]" % (self.id, self.weight)
