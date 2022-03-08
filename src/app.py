from flask import Flask, render_template, url_for, request, redirect
import pyrebase
from collections import OrderedDict

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

db.child("product_db").child(102).update({"img": ""})

#HTML app routess
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
    drink = db.child("product_db").child(34).get()
    cust = db.child("product_db").child(34).child("cust_opts").get()
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
    if request.form['DrinkButton'] == "Add to Order":

        id = request.form.get('drinkid')
        drinkRef = db.child("product_db").child(int(id)).get()
        drinkName = drinkRef.val()["name"]

        custDict = {}

        listofcusts = []


        opts = drinkRef.val()["cust_opts"]

        for i in opts:
            listofcusts.append(db.child("cust_db").child(int(i)).get().val()["id"])


        for i in range(len(listofcusts)):
            if request.form.get(str(opts[i])) != "" and request.form.get(str(opts[i])) != "None":
                custDict[str(listofcusts[i])] = request.form.get(str(opts[i]))

        print(custDict)
        custDrinkName = request.form.get('custDrinkName')
        custDrinkInstructions = request.form.get('custDrinkInstruction')
        db.child("order_test").child("user1").child(custDrinkName).set({"base_product": drinkName,"custom_name": custDrinkName, "special_instructions": custDrinkInstructions
                                                                        ,"cust": custDict, "size": request.form.get("size")})
        return redirect(url_for('submit'))


@app.route('/friends/')
def friends():
    return render_template('friends.html')




if __name__ == "__main__":
    app.run(debug=True)

