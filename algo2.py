import numpy as np
from include_functions import *
from drone import Drone
from item import Item
from warehouse import Warehouse
from order import Order

# Need:
#drone_list
#warehouse_list
#order_list

if __name__ == "__main__":

   order_list, warehouse_list, drone_list, items_list = populate_all('data/busy_day.in')

   max_duration = 1000000
   duration = 0
   while duration < max_duration:
       for drone in drone_list:
           if drone.is_available:
               drone.is_available = False
               # Moves the drone to the nearest warehouse
               wh_closests = warehouse_list.sort(key=lambda x: distance(x.position, drone.position), reverse=False)
               wh_closests = warehouse_list
               wh_closest = wh_closests[0]
               duration += drone.move_to(wh_closest.position)
               wh_closest.drones.append(drone.id)
               #To improve: Don't put all the drones in the same wh
               #if len(wh.closest.drones) >= 
               #To improve: split the orders into sub-orders.
               # Create a list with all the possible orders that we can fill in the drone
               possible_orders = []
               for order in order_list:
                   for sub_order in order.sub_orders:
                       weight = sub_order.weight()
                       if wh_closest.has(sub_order.items) and drone.current_weight + weight <= drone.max_weight:
                           possible_orders.append(sub_order)
                       else:
                           order.split_order()
               # Sort the possible orders by their distance to the drone
               possible_orders.sort(key=lambda x: distance(x.position, drone.position), reverse=False)
               # Fill the drone with the orders one by one, while it is possible
               i = 0
               orders_to_deliver = []
               while drone.current_weight <= drone.max_weight and i < len(possible_orders):
                   if drone.current_weight + possible_orders[i].weight() <= drone.max_weight:
                       duration += drone.load_order_from_warehouse(possible_orders[i], wh_closest)
                       orders_to_deliver.append(possible_orders[i])
                   i += 1
               # Delivers the orders one by one
               for order in orders_to_deliver:
                   duration += drone.move_to(order.position)
                   duration += drone.deliver_order(order)
               if len(possible_orders) == 0 or len(orders_to_deliver) == 0:
                   drone.move_to(wh_closests[1].position)
               drone.is_available = True
      #print(str(duration))

