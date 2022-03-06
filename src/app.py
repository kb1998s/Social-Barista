from audioop import add
from flask import Flask, render_template, url_for, request, redirect
import pyrebase
from dbInit import config, firebase, auth, db
from collections import OrderedDict

app = Flask(__name__)

# config = {
#     'apiKey': "AIzaSyBztWUIwgKYvM8YLFHbpuazAgPBak3gSXE",
#     'authDomain': "socialbarista-a9ddc.firebaseapp.com",
#     'projectId': "socialbarista-a9ddc",
#     'databaseURL': "https://socialbarista-a9ddc-default-rtdb.firebaseio.com/",
#     'storageBucket': "socialbarista-a9ddc.appspot.com",
#     'messagingSenderId': "947484314169",
#     'appId': "1:947484314169:web:7fa9c1b550a1051d1f5be8"}


# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# db = firebase.database()

#FLAVOR PROFILE LOGIC (using dummt user)
#flavor profile dict

user = db.child("user-item-db").child("262ZKKD4IDWdNTa6BeSHtEljKJi1").get()
dict = user.val()

flavorDict = {
    "sweet": 0,
    "nutty": 0,
    "aromatic": 0,
    "bitter": 0,
    "robust": 0,
    "earthy": 0,
    "tropical": 0,
    "fruity": 0,
    "smooth": 0,
    "creamy": 0,
    "floral": 0,
    "refreshing": 0,
}

#list of ordered drinks ID's
drinkslist = []
#number of times drink was ordered
timesordered = []
for x,y in dict.items():
    drinkslist.append(int(x))
    timesordered.append(int(y))

flavorlist = []
for i in range(len(drinkslist)):
    flavorlist.append(db.child("product_db").child(drinkslist[i]).child("flavor").get().val())

#Count number of times flavor was ordered
for i, item in enumerate(flavorlist):
    for k in item:
        temp = k
        flavorDict[temp] += timesordered[i]

#Get total drinks ordered
numDrinksOrdered = 0
for i, item in enumerate(timesordered):
    numDrinksOrdered += timesordered[i]

#Get top 4 stats
import heapq
heapFlavors = heapq.nlargest(4, flavorDict, key=flavorDict.get)

topFlavors = []
topStats = []
for i in heapFlavors:
    topFlavors.append(i)

for i in topFlavors:
    topStats.append(flavorDict[i])
#END FLAVOR PROFILE

# DRINKS MENU LOADING -- for testing only
from DrinkLoader import drinkCat_dic

# ORDER, CART
from order import *
from timeHelpers import getGreeting
user_id = "NzkGCghmk4MO4mCjwn3DQ8n3LxH2"
cartInit(user_id)
[order_list, usualOrders] = userOrderInit(user_id, db)



# RECOMMENDATIONS
greeting = getGreeting()
toBeDisplayIndex = getToBeDisplayIndex(usualOrders)

# END DRINK LOADING TEST




#HTML app routes
@app.route("/")
def index():
    return render_template('index.html', topFlavors = topFlavors, topStats = topStats, totalDrinks = numDrinksOrdered,
                            orders = toBeDisplayIndex, greeting = greeting, length = len(usualOrders))

@app.route('/order/', methods = ['GET'])
def order():
        
        return render_template('order.html', drinkCat_dic = drinkCat_dic)

@app.route('/account/')
def account():
    return render_template('account.html', topFlavors = topFlavors, topStats = topStats, totalDrinks = numDrinksOrdered)

@app.route('/submit')
def submit():
    drink = db.child("product_db").child(1).get()
    cust = db.child("product_db").child(1).child("cust_opts").get()
    custVal = cust.val()

    custRefs = []
    custDict = {}


    for i in custVal:
        custRefs.append(db.child("cust_db").child(int(i)).get())
    for k in custRefs:
        custDict[k.val()["sub-category"]] = k.val()["category"]
    custCat = []
    for k in custRefs:
        custCat.append(k.val()["category"])
    custCat = list(OrderedDict.fromkeys(custCat))


    return render_template('submit.html', custRefs=custRefs, drink = drink, db = db, custDict = custDict, custCat = custCat)

@app.route('/submit', methods=['POST'])
def submit2():
    if request.form['DrinkButton'] == "ChangeDrinkName":
        sub = request.form.get('drink')
        drink = db.child("product_db").child(int(sub)).get()
        cust = db.child("product_db").child(int(sub)).child("cust_opts").get()
        custVal = cust.val()

        custRefs = []
        custDict = {}

        for i in custVal:
            custRefs.append(db.child("cust_db").child(int(i)).get())
        for k in custRefs:
            custDict[k.val()["sub-category"]] = k.val()["category"]
        custCat = []
        for k in custRefs:
            custCat.append(k.val()["category"])
        custCat = list(OrderedDict.fromkeys(custCat))


        return render_template('submit.html', custRefs=custRefs, drink=drink, db = db, custCat = custCat, custDict = custDict)
    elif request.form['DrinkButton'] == "SubmitDrink":
        addCustomItemToCart(request, user_id)
        return redirect(url_for('submit'))


@app.route('/friends/')
def friends():
    return render_template('friends.html')

@app.route('/map/')
def map():
    return render_template('map.html')

@app.route('/customization/')
def customization():
    return render_template('customization.html')

@app.route('/savedOrders/')
def savedOrders():
    return render_template('savedOrders.html')

@app.route('/cart/', methods=['POST', 'GET'])
def cart():
    cart = getCart(user_id)
    return render_template('cart.html', itemList = cart.itemList, isinstance = isinstance, Item = Item)


# CART ROUTING FROM THE ORDER MENU
@app.route('/addItem/', methods = ['POST'])
def addItem():
    drink_id = request.form.get('drink-id')
    addItemToCart(user_id, drink_id)
    cart = getCart(user_id)
    return render_template('cart.html', itemList = cart.itemList)

# REMOVE ITEM FROM CART
@app.route('/removeItem/', methods = ['POST'])
def removeItem():
    drink_id = request.form.get('drink-id')
    # addItemToCart(user_id, drink_id)
    # print(drink_id)
    cart = getCart(user_id)
    return render_template('cart.html', itemList = cart.itemList)


if __name__ == "__main__":
    app.run(debug=True)