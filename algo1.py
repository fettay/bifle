from include_functions import *
from drone import Drone
from item import Item

for drone in drone_list:
    if drone.is_available:
        drone.is_available = False
        
        # Moves the drone to the nearest warehouse
        dist_warehouses = [dist(drone.position, wh.position) for wh in warehouses]
        wh_min = warehouses[np.argmin(dist_warehouses)]
        drone.move(wh_min.position)
        
        # Creates a list with all the possible orders that we can fill in the drone
        possible_orders = []
        for order in orders:
            weight = order.weight()
            if warehouse.has(order.items) and drone.weight + weight <= max_payload:
                possible_orders.append(order)
          
        # Sort the possible orders by their distance to the drone
        possible_orders.sort(key=dist(self.position, drone.position), reverse=True)
        
        # Fill the drone with the orders one by one, while it is possible
        i = 0
        orders_to_deliver = []
        while drone.weight <= max_payload and i < len(possible_orders):
            if drone.weight + possible_orders[i].weight() <= max_payload:
                drone.load(possible_orders[i])
                orders_to_deliver.append(possible_orders[i])
            i += 1
        
        # Delivers the orders one by one
        for order in orders_to_deliver:
            drone.deliver(order)
        
        drone.is_available = True