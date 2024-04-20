import MinHeap
import pandas as pd
import sys

if __name__ == "__main__":
    dataset_name = "ms_annual_data_2022.xlsx"
    # create a map with all restaurant names as the key and
    # a minHeap of its menu items as the value
    restaurants = {}
    df = pd.read_excel(dataset_name)
    rest_name = ""
    #iterate through excel sheet to add restaurants
    for index, row in df.iterrows():
        # if restaurant not already added
        if(rest_name != restaurants[row['Restaurant']]):
            rest_name = row['Restaurant']
            minheap = MinHeap.MinHeap(restaurants) # create a new heap to add as the value
            restaurants[rest_name] = minheap
