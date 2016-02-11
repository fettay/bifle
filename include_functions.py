from order import Order
from warehouse import Warehouse
DEBUG = False

def read_input_file(file_name):
   """
   Returns simulation_area, num_drones_available, simulation_deadline,
   max_drone_load, warehouse_locations, warehouse_stock,
   order_locations, order_items
   simulation_area is (rows, cols)
   warehouse_locations and order_locations are [[row1, col1], [row2, col2], ..., [rowN, colN]]
   warehouse_stock and order_items are [[item1_1, ...], [item2_1, ...], ..., [itemN_1, ...]]

   :param file_name: input file name
   """
   with open(file_name, 'r') as file_handle:

      rows, cols, drones, turns, max_payload = map(int, file_handle.readline().strip().split(' '))
      num_prod_types = int(file_handle.readline())

      product_weights = map(int, file_handle.readline().strip().split(' '))
      assert num_prod_types == len(product_weights)

      num_warehouses = int(file_handle.readline())
      warehouse_locations = [None] * num_warehouses
      warehouse_stock = [None] * num_warehouses
      for w_id in xrange(num_warehouses):
         warehouse_locations[w_id] =  map(int, file_handle.readline().strip().split(' '))
         warehouse_stock[w_id] =  map(int, file_handle.readline().strip().split(' '))

      if DEBUG:
         print 'Warehouse locations', warehouse_locations[:2]
         print 'Warehouse stock', warehouse_stock[:2]

      num_orders = int(file_handle.readline())
      order_locations = [None] * num_orders
      order_items = [None] * num_orders
      for o_id in xrange(num_orders):
         order_locations[o_id] =  map(int, file_handle.readline().strip().split(' '))
         order_len = int(file_handle.readline())
         order_items[o_id] =  map(int, file_handle.readline().strip().split(' '))
         assert order_len == len(order_items[o_id])

      if DEBUG:
         print 'Order locations', order_locations[:2]
         print 'Order items', order_items[:2]

      file_handle.close()

      return (rows, cols), \
            drones, turns, max_payload, \
            warehouse_locations, warehouse_stock, \
            order_locations, order_items

def write_output_file(file_name, data):
   """
   Write output file

   :param file_name: output file name
   :param data:
   """
   with open(file_name, 'w') as file_handle:
      # TODO: implement this
      file_name.close()


def populate_orders(order_locations, order_items):
   """
      create the orders
      :param order_locations
      :param order_items
      return list of orders
   """
   id_ = 0
   items = []
   for l, i in zip(order_locations, order_items):
      id_ += 1
      items.append(Order(id, i , l))
   return items

def populate_warehouses(warehouse_locations, warehouse_stock):
   """
   create the warehouses
   :param warehouses_locations
   :param warehouses_stock
   return list of warehouses
   """
   id_ = 0
   items = []
   for l, s in zip(warehouse_locations, warehouse_stock):
      id_ += 1
      items.append(Warehouse(id, l , s))
   return items

