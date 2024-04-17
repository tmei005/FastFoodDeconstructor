import pandas as pd
import Node

class MinHeap:
    dataset_name = "ms_annual_data_2022.xlsx"
    def __init__(self, sorted_by=lambda x: x):
        self.heap = []
        self.sorted_by = sorted_by

        # this is for all items but we can edit & change parameters as needed
        def importItems(self):
            # Read the Excel file
            df = pd.read_excel(self.dataset_name)

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
                carbs = row['carbs']
                dietary_fiber = row['dietary_fiber']
                sugar = row['sugar']
                protein = row['protein']

                self.heap.insert(Node(name, category, restaurant, description, serving_size, calories, total_fat, saturated_fat,
                 trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein))

            # Function to return parent
            def parent(self, pos):
                return pos // 2

            # Function to return the position of
            # the left child for the node currently
            # at pos
            def leftChild(self, pos):
                return 2 * pos

                # Function to return the position of

            # the right child for the node currently
            # at pos
            def rightChild(self, pos):
                return (2 * pos) + 1

            # Function that returns true if the passed
            # node is a leaf node
            def isLeaf(self, pos):
                return pos * 2 > self.size

                # Function to swap two nodes of the heap

            def swap(self, fpos, spos):
                self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

                # Function to heapify the node at pos

            def minHeapify(self, pos):
                # If the node is a non-leaf node and greater than any of its child
                if not self.isLeaf(pos):
                    if (self.sorted_by(self.Heap[pos]) > self.sorted_by(
                            self.Heap[self.leftChild(pos)]) or
                            self.sorted_by(self.Heap[pos]) > self.sorted_by(
                                self.Heap[self.rightChild(pos)])):
                        # swap with left child and heapify left child
                        if self.sorted_by(self.Heap[self.leftChild(pos)]) < self.sorted_by(
                                self.Heap[self.rightChild(pos)]):
                            self.swap(pos, self.leftChild(pos))
                            self.minHeapify(self.leftChild(pos))
                            # swap w right child and heapify right child
                        else:
                            self.swap(pos, self.rightChild(pos))
                            self.minHeapify(self.rightChild(pos))
            # Function to insert a node into the heap

            def insert(self, element):
                if self.size >= self.maxsize:
                    return
                self.size += 1
                self.Heap[self.size] = element

                current = self.size

                while (current != self.FRONT and
                       self.sorted_by(self.Heap[current]) < self.sorted_by(self.Heap[self.parent(current)])):
                    self.swap(current, self.parent(current))
                    current = self.parent(current)
            # Function to print the contents of the heap

            def Print(self):
                for i in range(1, (self.size // 2) + 1):
                    print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                          str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                          str(self.Heap[2 * i + 1]))

            # Function to remove and return the minimum element from the heap
            def remove(self):
                popped = self.Heap[self.FRONT]
                self.Heap[self.FRONT] = self.Heap[self.size]
                self.size -= 1
                self.minHeapify(self.FRONT)
                return popped