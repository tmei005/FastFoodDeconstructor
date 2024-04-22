from flask import Flask, render_template, request, session, redirect, url_for
import time
import RestaurantMap
import HashMapClass
import HeapClass
import os

def generate_secret_key():
    """
    Generate a secret key for Flask application.
    """
    return os.urandom(24).hex()

app = Flask(__name__)
app.secret_key = generate_secret_key()
restMap = RestaurantMap.RestaurantMap()
# hashMap = None  # Define hashMap as a global variable


@app.route('/')
def page1():
    restaurants = list(restMap.restaurant_categories.keys())
    restaurants = restaurants[:-1]  # take out 'Nan'
    return render_template('page1.html', restaurants_list=restaurants)


# Function called when first page search button is clicked
# Stores selected_restaurant variable and directs user to second page
@app.route('/process_input', methods=['POST'])
def process_input():
    selected_restaurant = request.form.get('selectedRestaurant').replace("&amp;", "&")
    session['selected_restaurant'] = selected_restaurant
    return redirect('page2.html')


@app.route('/page2.html')
def page2():
    # Load in restaurant to get a list of categories to display to user
    selected_restaurant = session.get('selected_restaurant')
    restaurant_cat_map = restMap.restaurant_categories[selected_restaurant]
    restaurant_cat = [pair[0] for pair in restaurant_cat_map]
    return render_template('page2.html', restaurant_cat=restaurant_cat, selected_restaurant=selected_restaurant)

# Function to load menu items once category and data structure is selected
@app.route('/get_menu', methods=['POST'])
def get_menu():
    print("get menu")
    selected_category = request.form.get('selected_category')
    selected_datastructure = request.form.get('selected_datastructure')
    session['selected_category'] = selected_category
    session['selected_datastructure'] = selected_datastructure
    start_time = time.time()
    global hashMap  # Declare hashMap as global here
    if (selected_datastructure == "Heap"):
        heap = HeapClass.Heap(session.get('selected_restaurant'), selected_category)
        menu_items = heap.getHeap()
        menu_items_dict = [item.to_dict() for item in menu_items]
        session['menu_items'] = menu_items_dict
    else:
        hashMap = HashMapClass.HashMap(session.get('selected_restaurant'), selected_category)
        hashMap.insertData()
        menu_items = hashMap.getMap()
    menu = [menuItem.name for menuItem in menu_items]
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time = f"{elapsed_time:.2f}"
    # Redirect to page 2.5 to show items in that category
    return render_template('page2_5.html', selected_datastructure=session.get('selected_datastructure'),
                           selected_category=session.get('selected_category'),
                           selected_restaurant=session.get('selected_restaurant'), menu=menu, elapsed_time=elapsed_time)


@app.route('/item_select', methods=['POST'])
def item_select():
    selected_item = request.form.get('selected_item')
    session['selected_item'] = selected_item
    print(session.get('selected_datastructure'))
    if session.get('selected_datastructure' == "Heap"): # for heap
        menu_items= session.get('menu_items', [])
        for i in menu_items:
            if i.name == selected_item:
                item = i
    else:
        global hashMap  # access hashMap
        item = hashMap.search_by_name(selected_item) # for HashMap
    # Load all menu item info into HTML template
    return render_template('page3.html', selected_restaurant=session.get('selected_restaurant'), item_name=item.name,
                           item_desc=item.description,
                           item_protein=item.protein, item_cal=item.calories, item_carbs=item.carbs,
                           item_sfat=item.saturated_fat,
                           item_fiber=item.dietary_fiber, item_fat=item.total_fat, item_chol=item.cholesterol,
                           item_sodium=item.sodium, item_sugar=item.sugar)


#
# @app.route('/page3.html')
# def page3():
#     return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True)
