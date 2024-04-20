from MinHeap import MinHeap
import pandas as pd

# This class creates a map where the key is restaurant name and value is
class RestaurantMap:

    def __init__(self):
        # restaurant name is the key, value is a vector of pairs of the category and row number of that category in the excel sheet
        self.restaurant_categories = {}
        dataset_name = ".\ms_annual_data_2022.xlsx"
        # Read the Excel file
        df = pd.read_excel(dataset_name)
        rowNum = 2; # items in this dataset start at row 2
        for index, row in df.iterrows():
            restaurant = row['restaurant']
            category = row['food_category']
            print (restaurant, category, rowNum)
            if restaurant in self.restaurant_categories: # add restaurant to map
                # add (category, rowNum) pair to the set for that restaurant
                # only if category doesn't exist because we want the first index of that category
                if category not in [pair[0] for pair in self.restaurant_categories[restaurant]]:
                    self.restaurant_categories[restaurant].append((category, rowNum))
            else:
                # add restaurant and create (category, rowNum) pair list
                self.restaurant_categories[restaurant] = [(category, rowNum)]
            rowNum += 1

    # this function returns the first row of the category for specified restaurant
    def findIndex(self, restaurant, category):
        if restaurant in self.restaurant_categories:
            for pair in self.restaurant_categories[restaurant]:
                if category == pair[0]:
                    return pair[1]
        return None
