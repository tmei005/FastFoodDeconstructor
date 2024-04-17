import MinHeap
import pandas as pd
import sys

if __name__ == "__main__":
    dataset_name = "ms_annual_data_2022.xlsx"
    # create a map with all restaurant names as the key and
    # a minHeap of its menu items as the value
    restaurants = {}
    restaurant_index = {}
    df = pd.read_excel(dataset_name)
    rest_name = ""
    #iterate through excel sheet to add restaurants
    for index, row in df.iterrows():
        # if restaurant already added, add that item to its heap
        if row['Restaurant'] in restaurants:
            # INSERT ITEM TO EXISTING MINHEAP AT THIS INDEX

        # if not already in set, add the restaurant and set value to none
        else:
            rest_name = row['Restaurant']
            # INSERT ITEM TO MINHEAP AT INDEX rest_name
