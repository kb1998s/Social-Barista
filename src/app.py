from audioop import add
from flask import Flask, render_template, url_for, request, redirect
import pyrebase
from dbInit import config, firebase, auth, db
from collections import OrderedDict

app = Flask(__name__)

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
[order_list, usualOrders] = userOrderInit(user_id)
sizeList = [('short', 'Short'), ('tall', 'Tall'), ('grande', 'Grande'), ('venti', 'Venti'), ('trenta', 'Trenta')]


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

@app.route('/savedOrders/', methods=['POST', 'GET'])
def savedOrders():
    
    if request.method == 'POST':
        orderId = request.form.get('orderId')
        if request.form['cus-form'] == 'addToCart': addOrderToCart(user_id, orderId)
        if request.form['cus-form'] == 'removeOrder': removeSavedOrder(user_id, orderId)
        if request.form['cus-form'] == 'cusOrder':
            orderId = request.form['orderId']
            return redirect('cusOrder/' + orderId)
            
    
    order_list = userOrderInit(user_id)[0]
    return render_template('savedOrders.html', orderList = order_list)

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

@app.route('/cart/', methods=['POST', 'GET'])
def cart():
    if request.method == 'POST':
        updateCart(user_id, request)
        print("Updated quantities and Sizes")
        
        if request.form.get('cart-form') == 'save':
            saveOrderFromCart(user_id, request)
            print("saved cart to order", request.form.get('order'))
        if request.form.get('remove') != None:
            drink_id = request.form.get('remove')
            removeItemFromCart(user_id, drink_id)

    cart = getCart(user_id)
    # sizeList = [('short', 'Short'), ('tall', 'Tall'), ('grande', 'Grande'), ('venti', 'Venti'), ('trenta', 'Trenta')]
    return render_template('cart.html', itemList = cart.itemList, sizeList = sizeList, isinstance = isinstance, Item = Item)


# CART ROUTING FROM THE ORDER MENU
@app.route('/addItem', methods = ['POST'])
def addItem():
    drink_id = request.form.get('drink-id')
    addItemToCart(user_id, drink_id)
    return redirect("cart")

# REMOVE ITEM FROM CART
@app.route('/removeItem', methods = ['POST','GET'])
def removeItem():
    
    if request.method == 'POST':
        drink_id = request.form.get('drink-id')
        removeItemFromCart(user_id, drink_id)
        
    return redirect('cart')

# REMOVE AN ORDER
@app.route('/removeOrder', methods = ['POST'])
def removeOrder():
    orderId = request.form.get('orderId')
    removeSavedOrder(user_id, orderId)
    return redirect('savedOrders')

# ADD AN ORDER TO CART
@app.route('/addOrder', methods = ['POST'])
def addOrder():
    orderId = request.form.get('orderId')
    addOrderToCart(user_id, orderId)
    return redirect('cart')

@app.route('/savedOrders/cusOrder/<orderId>', methods=['POST','GET'])
def cusOrder(orderId):
    if request.method == 'POST':
        if request.form.get('remove') != None:
            orderId = request.form['orderId']
            drinkId = request.form['remove']
            removeItemFromOrder(user_id, drinkId, orderId)
            print('Remove Item',drinkId,'from order',orderId)
        if request.form.get('custom') != None:
            print('Customize Item',drinkId,'from order',orderId)
        if request.form.get('order-form') == "save":
            orderId = request.form['orderId']
            updateOrder(user_id, orderId, request)
            print('Saving order',orderId)
            
    order = getOrder(user_id, orderId)
    print(order.category)
    timeList = [('WEEKDAY_MORNING', 'WEEKDAY MORNING'), ('WEEKDAY_NOON', 'WEEKDAY NOON'), ('WEEKDAY_NIGHT', 'WEEKDAY NIGHT'), ('WEEKEND_MORNING', 'WEEKEND MORNING'), ('WEEKEND_NOON', 'WEEKEND NOON'), ('WEEKEND_NIGHT', 'WEEKEND NIGHT')]
    return render_template('order-cus.html', timeList = timeList, order = order, orderId = orderId, itemList = order.itemList, sizeList = sizeList)
 
 
if __name__ == "__main__":
    app.run(debug=True)
    
