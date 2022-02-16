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




"""

db.child("product_db").child("cold_coffee").child().child("cold_brew").child("Starbucks Cold Brew Coffee").set({"cust_type": "cold_coffee", "flavor": "nutty", "id":
    3, "name": "Starbucks Cold Brew Coffee"})
db.child("product_db").child("hot_coffee").child().child("Americanos").child("Caffè Americano").set({"cust_type": "hot_coffee", "flavor": "nutty", "id":
    1, "name": "Caffè Americano"})



db.child("product_db").child("hot_coffee").child("Brewed Coffees").child("Veranda Blend").set({"cust_type": "brewed_coffee", "flavor": "nutty", "id":
    5, "name": "Veranda Blend"})
db.child("product_db").child("hot_coffee").child("Brewed Coffees").child("Caffè Misto").set({"cust_type": "brewed_coffee", "flavor": "nutty", "id":
    6, "name": "Caffè Misto"})
db.child("product_db").child("hot_coffee").child("Brewed Coffees").child("Featured Starbucks Dark Roast Coffee").set({"cust_type": "brewed_coffee", "flavor": "nutty", "id":
    7, "name": "Featured Starbucks Dark Roast Coffee"})
db.child("product_db").child("hot_coffee").child("Brewed Coffees").child("Pike Place Roast").set({"cust_type": "brewed_coffee", "flavor": "nutty", "id":
    8, "name": "Pike Place Roast"})
db.child("product_db").child("hot_coffee").child("Brewed Coffees").child("Decaf Pike Place Roast").set({"cust_type": "brewed_coffee", "flavor": "nutty", "id":
    9, "name": "Decaf Pike Place Roast"})

db.child("product_db").child("hot_coffee").child("Cappuccinos").child("Cappuccino").set({"cust_type": "cappuccino", "flavor": "nutty", "id":
    10, "name": "Cappuccino"})
db.child("product_db").child("hot_coffee").child("Espresso Shots").child("Espresso").set({"cust_type": "espresso", "flavor": "nutty", "id":
    11, "name": "Espresso"})
db.child("product_db").child("hot_coffee").child("Espresso Shots").child("Espresso Con Panna").set({"cust_type": "espresso", "flavor": "nutty", "id":
    12, "name": "Espresso Con Panna"})
db.child("product_db").child("hot_coffee").child("Flat Whites").child("Flat White").set({"cust_type": "flat_white", "flavor": "nutty", "id":
    13, "name": "Flat White"})
db.child("product_db").child("hot_coffee").child("Flat Whites").child("Honey Almondmilk Flat White").set({"cust_type": "flat_white", "flavor": "nutty", "id":
    14, "name": "Honey Almondmilk Flat White"})
    
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Pistachio Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    15, "name": "Pistachio Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Sugar Cookie Almondmilk Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    16, "name": "Sugar Cookie Almondmilk Latte"})
db.child("product_db").child("hot_coffee").child("Lattes").child("Chestnut Praline Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    17, "name": "Chestnut Praline Latte"})
db.child("product_db").child("hot_coffee").child("Lattes").child("Caramel Brulée Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    18, "name": "Caramel Brulée Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Caffè Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    19, "name": "Caffè Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Cinnamon Dolce Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    20, "name": "Cinnamon Dolce Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Starbucks Reserve Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    21, "name": "Starbucks Reserve Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Starbucks Reserve Hazelnut Bianco Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    22, "name": "Starbucks Reserve Hazelnut Bianco Latte"})
    
db.child("product_db").child("hot_coffee").child("Lattes").child("Starbucks Blonde Vanilla Latte").set({"cust_type": "latte", "flavor": "nutty", "id":
    23, "name": "Starbucks Blonde Vanilla Latte"})
    
db.child("product_db").child("hot_coffee").child("Macchiatos").child("Caramel Macchiato").set({"cust_type": "macchiatos", "flavor": "nutty", "id":
    24, "name": "Caramel Macchiato"})
db.child("product_db").child("hot_coffee").child("Macchiatos").child("Espresso Macchiato").set({"cust_type": "macchiatos", "flavor": "nutty", "id":
    25, "name": "Espresso Macchiato"})
    
    
db.child("product_db").child("hot_coffee").child("Mochas").child("Toasted White Chocolate Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    26, "name": "Toasted White Chocolate Mocha"})
    
db.child("product_db").child("hot_coffee").child("Mochas").child("Peppermint White Chocolate Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    27, "name": "Peppermint White Chocolate Mocha"})
    
db.child("product_db").child("hot_coffee").child("Mochas").child("Peppermint Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    28, "name": "Peppermint Mocha"})
    
db.child("product_db").child("hot_coffee").child("Mochas").child("Caffè Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    29, "name": "Caffè Mocha"})
    
db.child("product_db").child("hot_coffee").child("Mochas").child("Starbucks Reserve Dark Chocolate Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    30, "name": "Starbucks Reserve Dark Chocolate Mocha"})

db.child("product_db").child("hot_coffee").child("Mochas").child("White Chocolate Mocha").set({"cust_type": "mochas", "flavor": "nutty", "id":
    31, "name": "White Chocolate Mocha"})
"""

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
    hot_coffee = db.child("product_db").child("hot_coffee").child("Americanos").get()
    cust = cust = db.child("cust_db").child("hot_coffee").get()
    cust = cust.val()
    selected_drink = hot_coffee
    currdrink = "Caffè Americano"
    return render_template('submit.html', cust=cust, hot_coffee=hot_coffee, selected_drink = selected_drink, currdrink = currdrink)

@app.route('/submit', methods=['POST'])
def submit2():
    currdrink = request.form.get('drink')
    hot_coffee = db.child("product_db").child("hot_coffee").child("Americanos").child(currdrink)


    selected_drink = hot_coffee.get()

    hot_coffee = db.child("product_db").child("hot_coffee").child("Americanos").get()

    str = "hot_coffee"
    cust = db.child("cust_db").child(str).get()
    cust = cust.val()


    print(selected_drink.val()['name'] )
    return render_template('submit.html', cust=cust, hot_coffee=hot_coffee, selected_drink = selected_drink, currdrink = currdrink)

@app.route('/friends/')
def friends():
    return render_template('friends.html')




if __name__ == "__main__":
    app.run(debug=True)