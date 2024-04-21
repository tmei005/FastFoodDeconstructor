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
selected_restaurant = ''
# @app.route('/process_input', methods=['POST'])
# def process_input():
#     user_input = request.form['restaurant']
#     # Now you can use the user_input in your Python code
#     session['user1'] = user_input
#     # Process the input further as needed
#     return user_input
@app.route('/')
def page1():
    restaurants = list(restMap.restaurant_categories.keys())
    restaurants = restaurants[:-1] # take out 'Nan'
    # print(selected_restaurant)
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/page2.html')
def page2():
    # categories = restMap.restaurant_categories["Restaurant Name"].values()
    #print(categories)
    return render_template('page2.html', )

@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
