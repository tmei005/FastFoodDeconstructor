from flask import Flask, render_template, request, session, redirect, url_for
import json
import time
import RestaurantMap
from Node import MenuItem
import HashMapClass
import HeapClass
import pandas as pd
import sys

app = Flask(__name__)
app.secret_key = 'secret'
restMap = RestaurantMap.RestaurantMap()

@app.route('/')
def page1():
    restaurants = list(restMap.restaurant_categories.keys())
    restaurants = restaurants[:-1] # take out 'Nan'
    print(restaurants)
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/process_input', methods=['POST'])
def process_input():
    selected_restaurant = request.form.get('restaurant')
    session['selected_restaurant'] = selected_restaurant
    # You can do further processing here if needed
    return redirect('page2.html')

@app.route('/page2.html')
def page2():
    selected_restaurant = session.get('selected_restaurant')
    restaurant_cat_map = restMap.restaurant_categories[selected_restaurant]
    restaurant_cat = [pair[0] for pair in restaurant_cat_map]
    return render_template('page2.html', restaurant_cat=restaurant_cat, selected_restaurant=selected_restaurant)

# @app.route('/process_input2', methods=['POST'])
# def process_input2():
#     selected_category = request.form.get('selected_category')
#     selected_sorting = request.form.get('selected_sorting')
#     # Further processing based on the selected category and sorting method
#     # For example:
#     print("Selected category:", selected_category)
#     print("Selected sorting method:", selected_sorting)
#     # Redirect to the homepage or another appropriate page
#     return redirect('page1.html')
@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
