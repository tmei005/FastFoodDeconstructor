from flask import Flask, render_template
import time
import RestaurantMap
from Node import MenuItem
import HashMapClass
import pandas as pd
import sys

app = Flask(__name__)

@app.route('/')
def page1():
    # Pass the restaurants_list variable to the template
    restList = RestaurantMap.RestaurantMap()
    restaurants_list = list(restList.restaurant_categories.keys())
    return render_template('page1.html', restaurants_list=restaurants_list)

@app.route('/page2.html')
def page2():
    return render_template('page2.html')


@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
