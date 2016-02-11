class Drone(object):
   def __init__(self, id, max_weight, initial_position = [0, 0]):
      self.position = initial_position  # [x, y]
      self.current_weight = 0
      self.max_weight = max_weight
      self.payload = []
      self.is_available = True
      self.id = id

   def __str__(self):
      payload_str = 'None' if 0 == len(self.payload) else ', '.join([str(x) for x in self.payload])
      return "Drone\itemPosition %d, %d] [Weight %d of %d]\n\t[Payload %s]" % \
            (     self.position[0], self.position[1],
                  self.current_weight, self.max_weight, payload_str)

   def add_item(self, item, from_warehouse):
      if self.current_weight + item.weight > self.max_weight:
         raise ValueError('drone payload weight exceeded')
      else:
         self.current_weight += item.weight
         self.payload.append(item)
         if from_warehouse:
            from_warehouse.take_item(item.id)

   def load_order_from_warehouse(self, order, from_warehouse):
      for item in order.items:
         print "Load %d %d at warehouse %s" % (self.id, item.id, from_warehouse.id)
         if self.current_weight + item.weight > self.max_weight:
            raise ValueError('drone payload weight exceeded')
         else:
            self.current_weight += item.weight
            self.payload.append(item)
            if from_warehouse:
               from_warehouse.take_item(item.id)

   def deliver_order(self, to_order):
      for item in to_order.items:
         self.deliver_item(item, to_order)

   def deliver_item(self, item, to_order):
      try:
         print "Unload %d %d at order %s" % (self.id, item.id, to_order.id)
         self.payload.remove(item)
         self.current_weight -= item.weight
         if to_order:
            to_order.remove_item(item)
      except ValueError:
         print 'drone failed to remove item (item not found)'
         raise

   def move_to(self, new_position):
      assert isinstance(new_position, list)
      assert 2 == len(new_position)
      self.position = new_position
