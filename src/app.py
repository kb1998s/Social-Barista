from flask import Flask, render_template, url_for, request
import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyBztWUIwgKYvM8YLFHbpuazAgPBak3gSXE",
    'authDomain': "socialbarista-a9ddc.firebaseapp.com",
    'projectId': "socialbarista-a9ddc",
    'databaseURL': "https://socialbarista-a9ddc-default-rtdb.firebaseio.com/",
    'storageBucket': "socialbarista-a9ddc.appspot.com",
    'messagingSenderId': "947484314169",
    'appId': "1:947484314169:web:7fa9c1b550a1051d1f5be8"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

db.child("product_db").child("hot_coffee").child("test drink").set({"cust_type": "hot_coffee", "flavor": "nutty", "id":
    2, "name": "test drink"})

db.child("product_db").child("cold_coffee").child().child("cold_brew").child("Starbucks Cold Brew Coffee").set({"cust_type": "cold_coffee", "flavor": "nutty", "id":
    3, "name": "Starbucks Cold Brew Coffee"})

#HTML app routes
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/order/')
def order():
    return render_template('order.html')
@app.route('/account/')
def account():
    return render_template('account.html')
@app.route('/submit')
def submit():
    hot_coffee = db.child("product_db").child("hot_coffee").get()
    cust = cust = db.child("cust_db").child("hot_coffee").get()
    cust = cust.val()
    selected_drink = hot_coffee
    currdrink = "Caffè Americano"
    return render_template('submit.html', cust=cust, hot_coffee=hot_coffee, selected_drink = selected_drink, currdrink = currdrink)

@app.route('/submit', methods=['POST'])
def submit2():
    currdrink = request.form.get('drink')
    print(currdrink)
    hot_coffee = db.child("product_db").child("hot_coffee")


    selected_drink = hot_coffee.order_by_child("name").equal_to(currdrink).get()

    hot_coffee = db.child("product_db").child("hot_coffee").get()

    str = "hot_coffee"
    cust = db.child("cust_db").child(str).get()
    cust = cust.val()
    print(cust)

    print((selected_drink.val()[currdrink]['name']))
    return render_template('submit.html', cust=cust, hot_coffee=hot_coffee, selected_drink = selected_drink, currdrink = currdrink)

@app.route('/friends/')
def friends():
    return render_template('friends.html')




if __name__ == "__main__":
    app.run(debug=True)