from flask import Flask, render_template, request, session
import json
import time
import RestaurantMap
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

app = Flask(__name__)
app.secret_key = 'user1'

restMap = RestaurantMap.RestaurantMap()

@app.route('/')
def page1():
    restaurants = list(restMap.restaurant_categories.keys())
    restaurants = restaurants[:-1] # take out 'Nan'
    # print(selected_restaurant)
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/page2.html')
def page2():
    json_map = json.dumps(restMap.restaurant_categories)
    return render_template('page2.html', restaurant_map=json_map)

@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
