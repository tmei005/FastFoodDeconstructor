import pandas as pd
from Node import MenuItem

class Heap:
    def __init__(self, restaurant, category):
        self.arr = []
        self.size = len(self.arr)
        self.restaurant = restaurant
        self.category = category

    # inserts (searched) restaurant with (clicked-on) category
    def _insert(self):
        dataset_name = ".\ms_annual_data_2022.xlsx"
        df = pd.read_excel(dataset_name)
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

            if row['restaurant'] == self.restaurant and row['food_category'] == self.category:
                self.arr.append(MenuItem(name, category, restaurant, description, serving_size, calories, total_fat, saturated_fat,
                     trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))
                child = self.size()-1
                parent = (child-1)/2
                while(parent >= 0 and self.arr[parent].name > self.arr[child].name):
                    temp = parent
                    arr[parent] = lis[pos2]
                    lis[pos2] = temp
                    child = parent
                    parent = (child-1)/2

    def _findLeftChild(self, parentIndex):
        return 2*parentIndex+1

    def _findRightChild(self, parentIndex):
        return 2*parentIndex +2

    def _extractMin(self):
        self.arr[0] = self.arr[--self.size]
        self._heapifyDown(0)

    def _heapifyDown(self, index):
        lcIndex = self._findLeftChild(index)
        rcIndex = self._findRightChild(index)
        if (lcIndex < self.size and (self.arr[lcIndex] > self.arr[index] and self.arr[rcIndex] > self.arr[index])):
            if (self.arr[lcIndex] < self.arr[rcIndex]):
                largerChildIndex = rcIndex;
            else:
                largerChildIndex = lcIndex;

        temp = index
        self.arr[index] = self.arr[largerChildIndex]
        self.largerChildIndex = self.arr[temp]
        self._heapifyDown(largerChildIndex);

    def _print(self):
        for MenuItem in self.arr:
            print(MenuItem.name, MenuItem.calories)
