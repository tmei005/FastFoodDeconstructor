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
# menu_items = []

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
    global hashMap
    global menu_items
    if (selected_sorting == "Heap"):
        heap = HeapClass.Heap(session.get('selected_restaurant'), selected_category)
        menu_items = heap.getHeap()
    else:
        hashMap = HashMapClass.HashMap(session.get('selected_restaurant'), selected_category)
        hashMap.insertData()
        menu_items = hashMap.getMap()
    # Store menu items in session
    # menu_items_dict = [item.to_dict() for item in menu_items]
    # session['menu_items'] = menu_items_dict
    # Get list of menu items
    menu = [menuItem.name for menuItem in menu_items]
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = f"{elapsed_time:.2f}"
    # Redirect to the homepage or another appropriate page
    return render_template('page2_5.html', selected_sorting=session.get('selected_sorting'), selected_category=session.get('selected_category'), selected_restaurant=session.get('selected_restaurant'), menu=menu, elapsed_time=elapsed_time)
@app.route('/item_select', methods=['POST'])
def item_select():
    selected_item = request.form.get('selected_item')
    # retrieve menu items from session
    # menu_items_dict = session.get('menu_items', [])
    # menu_items = [MenuItem(**item_dict) for item_dict in menu_items_dict]
    session['selected_item'] = selected_item
    # if(session.get('selected_sorting') == "Heap"):
    for i in menu_items:
        if i.name == selected_item:
            item = i
    else:
        print(session.get('selected_sorting'))
        item = hashMap.search_by_name(selected_item)
    return render_template('page3.html', selected_restaurant=session.get('selected_restaurant'), item_name=item.name, item_desc=item.description,
                           item_protein=item.protein, item_cal=item.calories, item_carbs=item.carbs, item_sfat=item.saturated_fat,
                           item_fiber=item.dietary_fiber, item_fat=item.total_fat, item_chol=item.cholesterol, item_sodium=item.sodium, item_sugar=item.sugar)

@app.route('/page3.html')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
