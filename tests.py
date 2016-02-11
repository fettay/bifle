from include_functions import *
from drone import Drone
from item import Item


if __name__ == "__main__":
   read_input_file('data/ex.in')
   data = read_input_file('data/busy_day.in')
   read_input_file('data/mother_of_all_warehouses.in')
   read_input_file('data/redundancy.in')
   liste = populate_warehouses(data[4], data[5])

   test_item = Item(123, 100)
   test_item2 = Item(123, 1)
   test_drone = Drone(100)
   print test_drone.location
   test_drone.move_to([10, 10])
   print test_drone.location

   test_drone.add_item(test_item, None)
   print test_drone.current_weight
   test_drone.deliver_item(test_item, None)
   test_drone.add_item(test_item2, None)
   print test_drone.current_weight