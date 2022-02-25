from flask import Flask, render_template, url_for
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

#flavor profile dict
user = db.child("user-item-db").child("1XHftVUhoFhBeCoac0p2DhKfoos2").get()

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

drinkslist = []
timesordered = []
for x,y in dict.items():
    drinkslist.append(int(x))
    timesordered.append(int(y))

print(drinkslist)
print(timesordered)

flavorlist = []

for i in range(len(drinkslist)):
    flavorlist.append(db.child("product_db").child(drinkslist[i]).child("flavor").get().val())


for i in flavorlist:
    for k in i:
        temp = k
        flavorDict[temp] += 1
print(flavorDict)

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
@app.route('/submit/')
def submit():
    return render_template('submit.html')
@app.route('/friends/')
def friends():
    return render_template('friends.html')
@app.route('/map/')
def map():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)