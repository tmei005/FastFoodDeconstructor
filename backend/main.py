# import MinHeap
# import RestaurantMap
import Node
import HashMapClass
import pandas as pd
import sys

if __name__ == "__main__":
    # Create a sample hashmap
    hashmap = HashMapClass.HashMap(2)

    # Create some sample nodes
    node1 = Node.MenuItem("Burger", "Main Course", "Restaurant A")
    node2 = Node.MenuItem("Taco", "Dessert", "Restaurant B")

    # Insert nodes into the hashmap
    hashmap.insert(node1)
    hashmap.insert(node2)

    # Retrieve and print some attributes of the inserted nodes for testing
    print("Retrieved node 1:")
    print("Name:", node1.name)
    print("Category:", node1.category)
    print("Restaurant:", node1.restaurant)

    print("\nRetrieved node 2:")
    print("Name:", node2.name)
    print("Category:", node2.category)
    print("Restaurant:", node2.restaurant)
