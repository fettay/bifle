class Drone(object):
   def __init__(self, max_weight, initial_location = [0, 0]):
      self.location = initial_location  # [x, y]
      self.current_weight = 0
      self.max_weight = max_weight
      self.payload = []

   def __str__(self):
      payload_str = 'None' if 0 == len(self.payload) else ', '.join([str(x) for x in self.payload])
      return "Drone\t[Location %d, %d] [Weight %d of %d]\n\t[Payload %s]" % \
            (     self.location[0], self.location[1],
                  self.current_weight, self.max_weight, payload_str)

   def add_item(self, item, from_warehouse):
      if self.current_weight + item.weight > self.max_weight:
         raise ValueError('drone payload weight exceeded')
      else:
         self.current_weight += item.weight
         self.payload.append(item)
         if from_warehouse:
            from_warehouse.take_item(item.id)

   def deliver_item(self, item, to_order):
      try:
         self.payload.remove(item)
         self.current_weight -= item.weight
         if to_order:
            to_order.remove_item(item.id)
      except ValueError:
         print 'drone failed to remove item (item not found)'
         raise

   def move_to(self, new_location):
      assert isinstance(new_location, list)
      assert 2 == len(new_location)
      self.location = new_location
