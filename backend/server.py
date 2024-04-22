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
    return render_template('page1.html', restaurants_list=restaurants)

@app.route('/process_input', methods=['POST'])
def process_input():
    selected_restaurant = request.form.get('selectedRestaurant')
    session['selected_restaurant'] = selected_restaurant
    # You can do further processing here if needed
    return redirect('page2.html')

@app.route('/page2.html')
def page2():
    selected_restaurant = session.get('selected_restaurant')
    restaurant_cat_map = restMap.restaurant_categories[selected_restaurant]
    restaurant_cat = [pair[0] for pair in restaurant_cat_map]
    return render_template('page2.html', restaurant_cat=restaurant_cat, selected_restaurant=selected_restaurant)

@app.route('/get_menu', methods=['POST'])
def get_menu():
    print("get menu")
    selected_category = request.form.get('selected_category')
    selected_sorting = request.form.get('selected_sorting')
    session['selected_category'] = selected_category
    session['selected_sorting'] = selected_sorting
    start_time = time.time()
    if (selected_sorting == "Heap"):
        heap = HeapClass.Heap(session.get('selected_restaurant'), selected_category)
        menu_items = heap.getHeap()
    else:
        print("poop")
        hashMap = HashMapClass.HashMap(session.get('selected_restaurant'), selected_category)
        hashMap.insertData()
        menu_items = hashMap.getMap()
    menu = [menuItem.name for menuItem in menu_items]
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = f"{elapsed_time:.2f}"  # Output: "12345.00"
    # Redirect to the homepage or another appropriate page
    return render_template('page2_5.html', selected_sorting=session.get('selected_sorting'), selected_category=session.get('selected_category'), selected_restaurant=session.get('selected_restaurant'), menu=menu, elapsed_time=elapsed_time)

@app.route('/page3.html')
def page3():

    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
