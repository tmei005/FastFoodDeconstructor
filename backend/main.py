# import MinHeap
from RestaurantMap import RestaurantMap
import time
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

if __name__ == "__main__":
    # Create an instance of the RestaurantMap class
    restaurant_map = RestaurantMap()

    restaurant = "McDonald's"
    category = 'Burger'
    print(restaurant_map.findIndex(restaurant, category))
