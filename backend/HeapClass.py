import pandas as pd
from Node import MenuItem
class Heap:
    def __init__(self, restaurant, category):
        self.heapArr = []
        self.heapSize = 0
        self.restaurant = restaurant
        self.category = category

    def heapifyUp(self, child):
        if child == 0:
            return
        parent = (child - 1) // 2

        if parent >= 0 and self.heapArr[parent].name > self.heapArr[child].name:
            self.heapArr[parent], self.heapArr[child] = self.heapArr[child], self.heapArr[parent]

            self.heapifyUp(parent)

    def heapifyDown(self, index = 0):

        leftChild = 2 * index + 1
        rightChild = 2 * index + 2
        smallerChild = index
        if leftChild < self.heapSize and self.heapArr[leftChild].name < self.heapArr[smallerChild].name:
            smallerChild = leftChild
        if rightChild < self.heapSize and self.heapArr[rightChild].name < self.heapArr[smallerChild].name:
            smallerChild = rightChild

        if smallerChild != index:
            self.heapArr[index], self.heapArr[smallerChild] = self.heapArr[smallerChild], self.heapArr[index]
            self.heapifyDown(smallerChild)

    def insertData(self):
        dataset_name = "ms_annual_data_2022.xlsx"
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
                self.heapArr.append(
                    MenuItem(name, category, restaurant, description, serving_size, calories, total_fat, saturated_fat,
                             trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))
                self.heapSize += 1
                self.heapifyUp(self.heapSize-1)

    def extractMin(self):
        if self.heapSize == 0:
            return None
        minNum = self.heapArr[0]
        self.heapArr[0] = self.heapArr[self.heapSize - 1]
        self.heapSize -= 1
        self.heapArr.pop()
        if self.heapSize > 0:
            self.heapifyDown(0)

        return minNum

    def printHeap(self):
        self.insertData()
        for i in range(self.heapSize):
            print(self.extractMin().name)