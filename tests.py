from include_functions import *


if __name__ == "__main__":
   read_input_file('data/ex.in')
   data = read_input_file('data/busy_day.in')
   read_input_file('data/mother_of_all_warehouses.in')
   read_input_file('data/redundancy.in')
   liste = populate_orders(data[6], data[7])