# from dis import Instruction
import sys
from unicodedata import category
import pyrebase
from flask import Flask, redirect, render_template, request, session,  url_for
from timeHelpers import getTimeCategory
from order import Item, Order, getCurOrder, getOrders


#Initialze flask constructor
app = Flask(__name__)       

#Add your own details
config = {
    'apiKey': "AIzaSyBztWUIwgKYvM8YLFHbpuazAgPBak3gSXE",
    'authDomain': "socialbarista-a9ddc.firebaseapp.com",
    'projectId': "socialbarista-a9ddc",
    'databaseURL': "https://socialbarista-a9ddc-default-rtdb.firebaseio.com/",
    'storageBucket': "socialbarista-a9ddc.appspot.com",
    'messagingSenderId': "947484314169",
    'appId': "1:947484314169:web:7fa9c1b550a1051d1f5be8"}

#initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": ""}

#Login
@app.route("/")
def login():
    return render_template("login.html")

#Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html")

# Checkout fav drinks
@app.route("/fav")
def fav():
    db = firebase.database()
    # Getting user db info
    user_id = "NzkGCghmk4MO4mCjwn3DQ8n3LxH2"
    fav_db = db.child("fav_db")
    user_rf = fav_db.child(user_id)
    inventory = user_rf.get().val()
    order_list = getOrders(inventory)
    toBeDisplay = getCurOrder(order_list)[0]
    
    return render_template("fav_order.html", orders = toBeDisplay, length = len(order_list))

# submit drinks
@app.route("/submit", methods = ["POST", "GET"])
def submit():
    db = firebase.database()

    user_id = person["uid"]
    fav_db = db.child("fav_db")
    
    if (request.method == "POST"):
        #//////////////// Data processing
        # gather Data
        result = request.form
        # Passing data   
        order_name = result["order_name"]
        category = getTimeCategory()
        drink_id = result["Drinks"]
        instruction = result["instruction"]
        form  = result["Form"]
        size = result["Size"]
        quantity = result["Quantities"]
        
        try: 
            user_rf = fav_db.child(user_id)
            user_rf.update({
                order_name: {
                    "category" : category,
                    "items": {
                        drink_id: {
                            'formCode': form,
                            'instructions': instruction,
                            'name': "Chestnut Praline Latte",
                            'quantity': quantity,  
                            'sizeCode': size,
                        }
                    } 
                }                
            })


            print(user_id," ", fav_db.child(user_id).get(), file=sys.stderr)
            #Redirect to welcome page
            return redirect(url_for('submit'))
        except:
            #If there is any error, redirect back to login
            return redirect(url_for('submit'))
    else:
        print(user_id," ", fav_db.child(user_id).get(), file=sys.stderr)

        return render_template('submit.html')


#Welcome page
@app.route("/welcome")
def welcome():
    if person["is_logged_in"] == True:
        return render_template("welcome.html", email = person["email"], name = person["name"])
    else:
        return redirect(url_for('login'))

#If someone clicks on login, they are redirected to /result
@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method == "POST":        #Only if data has been posted
        result = request.form           #Get the data
        email = result["email"]
        password = result["pass"]
        try:
            #Try signing in the user with the given information
            user = auth.sign_in_with_email_and_password(email, password)
            #Insert the user data in the global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            #Get the name of the user
            data = db.child("users").get()
            person["name"] = data.val()[person["uid"]]["name"]
            #Redirect to welcome page
            return redirect(url_for('welcome'))
        except:
            #If there is any error, redirect back to login
            return redirect(url_for('login'))
    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('login'))

#If someone clicks on register, they are redirected to /register
@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["pass"]
        name = result["name"]
        try:
            #Try creating the user account using the provided data
            auth.create_user_with_email_and_password(email, password)
            #Login the user
            user = auth.sign_in_with_email_and_password(email, password)
            #Add data to global person
            global person
            person["is_logged_in"] = True
            person["email"] = user["email"]
            person["uid"] = user["localId"]
            person["name"] = name
            #Append data to the firebase realtime database
            data = {"name": name, "email": email}
            db.child("users").child(person["uid"]).set(data)
            #Go to welcome page
            return redirect(url_for('welcome'))
        except:
            #If there is any error, redirect to register
            return redirect(url_for('register'))

    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(debug=True)