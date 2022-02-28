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

#FLAVOR PROFILE LOGIC (using dummt user)
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


#HTML app routes
@app.route("/")
def index():
    return render_template('index.html', topFlavors = topFlavors, topStats = topStats, totalDrinks = numDrinksOrdered)
@app.route('/order/')
def order():
    return render_template('order.html')
@app.route('/account/')
def account():
    return render_template('account.html', topFlavors = topFlavors, topStats = topStats, totalDrinks = numDrinksOrdered)
@app.route('/submit/')
def submit():
    return render_template('submit.html')
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

if __name__ == "__main__":
    app.run(debug=True)