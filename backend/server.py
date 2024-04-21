from flask import Flask, render_template, request
import json
import time
import RestaurantMap
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

app = Flask(__name__)
restMap = RestaurantMap.RestaurantMap()
selected_restaurant = ''
@app.route('/process_input', methods=['POST'])
def get_input():
    user_in = request.form['userin']
    return user_in

@app.route('/')
def page1():
    restaurants = list(restMap.restaurant_categories.keys())
    restaurants = restaurants[:-1] # take out 'Nan'
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/page2.html')
def page2():
    return render_template('page2.html')

@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
