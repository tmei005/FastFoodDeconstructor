import math

from flask import Flask, render_template
import json
import time
import RestaurantMap
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

app = Flask(__name__)
def escape_special_characters(string):
    if not isinstance(string, str):
        string = str(string)
    # Escape single quotes
    string = string.replace("'", "\\'")
    # Escape double quotes
    string = string.replace('"', '\\"')
    return string

@app.route('/')
def page1():
    # # Pass the restaurants_list variable to the template
    # restList = RestaurantMap.RestaurantMap()
    # restaurants_list = list(restList.restaurant_categories.keys())
    # restaurants = []
    # for restaurant in restaurants:
    #     restaurants.append(escape_special_characters(restaurant))
    # return render_template('page1.html', restaurants=restaurants)
    restList = RestaurantMap.RestaurantMap()
    # restaurants_list = list(restList.restaurant_categories.keys())
    restaurants = list(restList.restaurant_categories.keys())
    restaurants = restaurants[:-1]
    # restaurants_list = json.dumps(restaurants)
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/page2.html')
def page2():
    return render_template('page2.html')


@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
