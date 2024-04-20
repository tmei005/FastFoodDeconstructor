from flask import Flask, render_template

app = Flask(__name__)

# Define the list of restaurants
restaurants_list = ["Restaurant 1", "mcdonalds 2", "Restaurant 3"]

@app.route('/')
def index():
    # Pass the restaurants_list variable to the template
    return render_template('page1.html', restaurants_list=restaurants_list)

if __name__ == '__main__':
    app.run(debug=True)
