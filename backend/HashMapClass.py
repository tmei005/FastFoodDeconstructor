import string
from Node import MenuItem
import pandas as pd


class HashMap:
    def __init__(self, restaurant, category):
        self.capacity = 50
        self.size = 0
        self.load_factor = .75
        self.map = [None] * self.capacity
        self.restaurant = restaurant
        self.category = category
        # When HashMap is created, insert all items from that restaurant and category
        self.insertData()

        # Function to get hash value using ASCII sum of MenuItem name

    def _hash(self, menu_item):
        ascii_sum = sum(ord(c) for c in str(menu_item.name))
        return ascii_sum % self.capacity

    # If load factor > 0.75 then rehash
    def _rehash(self):
        # Double the capacity
        new_capacity = self.capacity * 2
        new_map = [None] * new_capacity
        new_size = 0

        # Re-insert existing items into the new map
        for item in self.map:
            if item is not None:
                current = item
                new_index = self._hash(current)
                if new_map[new_index] is None:
                    new_map[new_index] = current
                    new_size += 1
                else:
                    temp = new_map[new_index]
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = current
                current = current.next

        # Update hashmap values
        self.map = new_map
        self.capacity = new_capacity
        self.size = new_size

    # Function to insert a menu item into the hash map
    def insert(self, menu_item):
        # Check load factor
        if self.size / self.capacity >= self.load_factor:
            self._rehash()
        index = self._hash(menu_item)  # Get hash value for index
        # Add menu item to map
        if self.map[index] is None:
            self.map[index] = menu_item
            self.size += 1
        else:  # If there is already a menu item at that index, append it to the linked list
            current = self.map[index]
            while current.next is not None:
                current = current.next
            current.next = menu_item

    # Function to insert MenuItems from Excel sheet
    def insertData(self):
        dataset_name = "ms_annual_data_2022.xlsx"
        df = pd.read_excel(dataset_name)
        for index, row in df.iterrows():
            name = row['item_name']
            category = row['food_category']
            restaurant = row['restaurant']
            description = row['item_description']
            calories = row['calories']
            total_fat = row['total_fat']
            saturated_fat = row['saturated_fat']
            trans_fat = row['trans_fat']
            cholesterol = row['cholesterol']
            sodium = row['sodium']
            carbs = row['carbohydrates']
            dietary_fiber = row['dietary_fiber']
            sugar = row['sugar']
            protein = row['protein']
            if row['restaurant'] == self.restaurant and row['food_category'] == self.category:
                self.insert(
                    MenuItem(name, category, restaurant, description, calories, total_fat, saturated_fat,
                             trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))

    # Function to get all items in the map as an array
    def getMap(self):
        items = []
        for item in self.map:
            if item is not None:
                items.append(item)
        # return a list of menuItems sorted by name
        return sorted(items, key=lambda x: x.name)

    # Function to search for a MenuItem based on its name
    def search_by_name(self, name):
        ascii_sum = sum(ord(c) for c in str(name))
        index = ascii_sum % self.capacity
        current = self.map[index]
        while current is not None:
            if current.name == name:
                return current
            current = current.next
