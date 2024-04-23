import pandas as pd
from Node import MenuItem
import time
class Heap:
    def __init__(self, restaurant, category):
        self.heapArr = []
        self.heapSize = 0
        self.restaurant = restaurant
        self.category = category

    # Recursively compares and swaps the child to parent to see if it's smaller or not to rearrange heap
    def heapifyUp(self, child):
        if child == 0:
            return
        parent = (child - 1) // 2

        if parent >= 0 and self.heapArr[parent].name > self.heapArr[child].name:
            self.heapArr[parent], self.heapArr[child] = self.heapArr[child], self.heapArr[parent]
            self.heapifyUp(parent)

    # Recursively compares and swaps the parent to its children to see if it's smaller or not to rearrange heap
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

    # Inserts MenuItems from Excel Sheet into heap based on specified restaurant and category
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

            # Checks the dataset see if it's positioned at the selected restaurant and category and inserts it into the heap
            if row['restaurant'] == self.restaurant and row['food_category'] == self.category:
                self.heapArr.append(
                    MenuItem(name, category, restaurant, description, calories, total_fat, saturated_fat,
                             trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))
                self.heapSize += 1
                self.heapifyUp(self.heapSize-1)

    # Returns the top element in the heap and sorts the heap after extraction
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

    # Returns a list of the minheap of all the menuItems
    def getHeap(self):
        self.insertData()
        arr = []
        for i in range(self.heapSize):
            arr.append(self.extractMin())
        return arr