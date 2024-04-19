import string
from Node import MenuItem
import pandas as pd

class HashMap:
    def __init__(self):
        self.capacity = 1000
        self.size = 0
        self.load_factor = .75
        self.map = [None] * self.capacity

    def _hash(self, menu_item):
        category = str(menu_item.category)
        restaurant = str(menu_item.restaurant)
        ascii_sum = sum(ord(c) for c in category) + sum(ord(c) for c in restaurant)
        return ascii_sum % self.capacity

    def _rehash(self):
        print('\nRehashing \n')
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

        # Update hashmap properties
        self.map = new_map
        self.capacity = new_capacity
        self.size = new_size

    def insert(self, menu_item):
        # check load factor
        if self.size / self.capacity >= self.load_factor:
            self._rehash()

        index = self._hash(menu_item)
        print (index)
        if self.map[index] is None:
            self.map[index] = menu_item
            self.size += 1
        else:
            current = self.map[index]
            while current.next is not None:
                current = current.next
            current.next = menu_item

    # function to insert all items from excel sheet
    def insertAll(self):
        dataset_name = ".\ms_annual_data_2022.xlsx"
        # Read the Excel file
        df = pd.read_excel(dataset_name)
        # Accessing data
        for index, row in df.iterrows():
            name = row['item_name']
            category = row['food_category']
            restaurant = row['restaurant']
            description = row['item_description']
            serving_size = row['serving_size']
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

            self.insert(
                MenuItem(name, category, restaurant, description, serving_size, calories, total_fat, saturated_fat,
                     trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))

    # search / retrieval function to return a vector of menu items that satisfy the parameters
    def search(self, category, restaurant):
        index = (sum(ord(c) for c in category) + sum(ord(c) for c in restaurant)) % self.capacity
        current = self.map[index]
        found_items = []
        while current:
            if current.category == category and current.restaurant == restaurant:
                found_items.append(current)
            current = current.next
        return found_items
    # function to print map
    def print_map(self):
        for i, item in enumerate(self.map):
            print(f"Index {i}:")
            current = item
            while current:
                print(f"    {current.name} ({current.category}) - {current.restaurant}")
                current = current.next
            print()