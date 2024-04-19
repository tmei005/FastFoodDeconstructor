# import MinHeap
# import RestaurantMap
import time
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

if __name__ == "__main__":
    hashmap = HashMapClass.HashMap()
    start_time = time.time()  # Record the start time
    hashmap.insertAll()
    end_time = time.time()  # Record the end time

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print("insertAll() execution time:", elapsed_time, "seconds")
    hashmap.print_restaurant_categories("McDonald's")
    # hashmap.print_map()
    # mcdonaldsburgers = hashmap.search("Burgers", "McDonald's")
    # wendysdessert = hashmap.search("Desserts", "Wendy's")
    # for burgers in mcdonaldsburgers:
    #     print(burgers.name)
    # for burgers in wendysdessert:
    #     print(burgers.name)
