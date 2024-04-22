# import MinHeap
from RestaurantMap import RestaurantMap
import time
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

if __name__ == "__main__":
    hashmap = HashMapClass.HashMap("Longhorn Steakhouse","Toppings & Ingredients")
    mcdonaldsburgers = hashmap.getMap()
    for burgers in mcdonaldsburgers:
        print(burgers.name)

