from flask import Flask, render_template, url_for, request
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
"""
db.child("product_db").child(1).set({"name": "Caffè Americano", "category": "Hot Coffee", "sub-category": "Americanos",
                                          "cust_opts": {0: 1, 1: 4, 2: 8, 3: 11, 4: 23}, "flavor": "sweet", "id": 1})

db.child("product_db").child(2).set({"name": "Veranda Blend", "category": "Hot Coffee", "sub-category": "Brewed Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 2})
db.child("product_db").child(3).set({"name": "Caffè Misto", "category": "Hot Coffee", "sub-category": "Brewed Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 3})
db.child("product_db").child(4).set({"name": "Featured Starbucks Dark Roast Coffee", "category": "Hot Coffee", "sub-category": "Brewed Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 4})
db.child("product_db").child(5).set({"name": "Pike Place Roast", "category": "Hot Coffee", "sub-category": "Brewed Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 5})
db.child("product_db").child(6).set({"name": "Decaf Pike Place Roast", "category": "Hot Coffee", "sub-category": "Brewed Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 6})

db.child("product_db").child(7).set({"name": "Cappuccino", "category": "Hot Coffee", "sub-category": "Cappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 7})

db.child("product_db").child(8).set({"name": "Espresso", "category": "Hot Coffee", "sub-category": "Espresso Shots",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 8})
db.child("product_db").child(9).set({"name": "Espresso Con Panna", "category": "Hot Coffee", "sub-category": "Espresso Shots",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 9})

db.child("product_db").child(10).set({"name": "Flat White", "category": "Hot Coffee", "sub-category": "Flat Whites",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 10})
db.child("product_db").child(11).set({"name": "Honey Almondmilk Flat White", "category": "Hot Coffee", "sub-category": "Flat Whites",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 11})

db.child("product_db").child(12).set({"name": "Pistachio Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 12})
db.child("product_db").child(13).set({"name": "Sugar Cookie Almondmilk Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 13})
db.child("product_db").child(14).set({"name": "Chestnut Praline Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 14})
db.child("product_db").child(15).set({"name": "Caramel Brulée Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 15})
db.child("product_db").child(16).set({"name": "Caffè Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 16})
db.child("product_db").child(17).set({"name": "Cinnamon Dolce Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 17})
db.child("product_db").child(18).set({"name": "Starbucks Reserve Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 18})
db.child("product_db").child(19).set({"name": "Starbucks Reserve Hazelnut Bianco Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 19})
db.child("product_db").child(20).set({"name": "Starbucks Blonde Vanilla Latte", "category": "Hot Coffee", "sub-category": "Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 20})

db.child("product_db").child(21).set({"name": "Caramel Macchiato", "category": "Hot Coffee", "sub-category": "Macchiatos",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 21})
db.child("product_db").child(22).set({"name": "Espresso Macchiato", "category": "Hot Coffee", "sub-category": "Macchiatos",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 22})

db.child("product_db").child(23).set({"name": "Toasted White Chocolate Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 23})
db.child("product_db").child(24).set({"name": "Peppermint White Chocolate Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 24})
db.child("product_db").child(25).set({"name": "Peppermint Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 25})
db.child("product_db").child(26).set({"name": "Caffè Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 26})
db.child("product_db").child(27).set({"name": "Starbucks Reserve Dark Chocolate Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 27})
db.child("product_db").child(28).set({"name": "White Chocolate Mocha", "category": "Hot Coffee", "sub-category": "Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 28})


db.child("product_db").child(29).set({"name": "Irish Cream Cold Brew", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 29})
db.child("product_db").child(30).set({"name": "Salted Caramel Cream Cold Brew", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 30})
db.child("product_db").child(31).set({"name": "Starbucks Reserve Cold Brew", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 31})
db.child("product_db").child(32).set({"name": "Starbucks Cold Brew Coffee", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 32})
db.child("product_db").child(33).set({"name": "Vanilla Sweet Cream Cold Brew", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 33})
db.child("product_db").child(34).set({"name": "Starbucks Cold Brew Coffee with Milk", "category": "Cold Coffee", "sub-category": "Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 34})

db.child("product_db").child(35).set({"name": "Starbucks Reserve Nitro Cold Brew", "category": "Cold Coffee", "sub-category": "Nitro Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 35})
db.child("product_db").child(36).set({"name": "Nitro Cold Brew", "category": "Cold Coffee", "sub-category": "Nitro Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 36})
db.child("product_db").child(37).set({"name": "Vanilla Sweet Cream Nitro Cold Brew", "category": "Cold Coffee", "sub-category": "Nitro Cold Brews",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 37})

db.child("product_db").child(38).set({"name": "Iced Caffè Americano", "category": "Cold Coffee", "sub-category": "Iced Americano",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 38})

db.child("product_db").child(39).set({"name": "Iced Coffee", "category": "Cold Coffee", "sub-category": "Iced Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 39})
db.child("product_db").child(40).set({"name": "Iced Coffee with Milk", "category": "Cold Coffee", "sub-category": "Iced Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 40})
db.child("product_db").child(41).set({"name": "Iced Espresso", "category": "Cold Coffee", "sub-category": "Iced Coffees",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 41})

db.child("product_db").child(42).set({"name": "Iced Brown Sugar Oatmilk Shaken Espresso", "category": "Cold Coffee", "sub-category": "Iced Shaken Espresso",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 42})
db.child("product_db").child(43).set({"name": "Iced Chocolate Almondmilk Shaken Espresso", "category": "Cold Coffee", "sub-category": "Iced Shaken Espresso",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 43})
db.child("product_db").child(44).set({"name": "Iced Shaken Espresso", "category": "Cold Coffee", "sub-category": "Iced Shaken Espresso",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 44})

db.child("product_db").child(45).set({"name": "Iced Flat White", "category": "Cold Coffee", "sub-category": "Iced Flat Whites",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 45})
db.child("product_db").child(46).set({"name": "Iced Honey Almondmilk Flat White", "category": "Cold Coffee", "sub-category": "Iced Flat Whites",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 46})

db.child("product_db").child(47).set({"name": "Iced Pistachio Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 47})
db.child("product_db").child(48).set({"name": "Iced Sugar Cookie Almondmilk Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 48})
db.child("product_db").child(49).set({"name": "Iced Chestnut Praline Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 49})
db.child("product_db").child(50).set({"name": "Iced Caramel Brulée Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 50})
db.child("product_db").child(51).set({"name": "Starbucks Reserve Iced Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 51})
db.child("product_db").child(52).set({"name": "Starbucks Reserve Iced Hazelnut Bianco Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 52})
db.child("product_db").child(53).set({"name": "Iced Caffè Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 53})
db.child("product_db").child(54).set({"name": "Iced Cinnamon Dolce Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 54})
db.child("product_db").child(55).set({"name": "Iced Starbucks Blonde Vanilla Latte", "category": "Cold Coffee", "sub-category": "Iced Lattes",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 55})

db.child("product_db").child(56).set({"name": "Iced Caramel Macchiato", "category": "Cold Coffee", "sub-category": "Iced Macchiatos",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 56})

db.child("product_db").child(57).set({"name": "Iced White Chocolate Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 57})
db.child("product_db").child(58).set({"name": "Iced Peppermint White Chocolate Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 58})
db.child("product_db").child(59).set({"name": "Iced Toasted White Chocolate Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 59})
db.child("product_db").child(60).set({"name": "Iced Peppermint Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 60})
db.child("product_db").child(61).set({"name": "Iced Caffè Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 61})
db.child("product_db").child(62).set({"name": "Starbucks Reserve Iced Dark Chocolate Mocha", "category": "Cold Coffee", "sub-category": "Iced Mochas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 62})


db.child("product_db").child(63).set({"name": "Toasted White Hot Chocolate", "category": "Hot Drinks", "sub-category": "Hot Chocolates",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 63})
db.child("product_db").child(64).set({"name": "Peppermint White Hot Chocolate", "category": "Hot Drinks", "sub-category": "Hot Chocolates",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 64})
db.child("product_db").child(65).set({"name": "Peppermint Hot Chocolate", "category": "Hot Drinks", "sub-category": "Hot Chocolates",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 65})
db.child("product_db").child(66).set({"name": "Hot Chocolate", "category": "Hot Drinks", "sub-category": "Hot Chocolates",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 66})
db.child("product_db").child(67).set({"name": "White Hot Chocolate", "category": "Hot Drinks", "sub-category": "Hot Chocolates",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 67})

db.child("product_db").child(68).set({"name": "Caramel Apple Spice", "category": "Hot Drinks", "sub-category": "Juice",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 68})
db.child("product_db").child(69).set({"name": "Steamed Apple Juice", "category": "Hot Drinks", "sub-category": "Juice",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 69})

db.child("product_db").child(70).set({"name": "Pistachio Crème", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 70})
db.child("product_db").child(71).set({"name": "Chestnut Praline Crème", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 71})
db.child("product_db").child(72).set({"name": "Caramel Brulée Crème", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 72})
db.child("product_db").child(73).set({"name": "Cinnamon Dolce Crème", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 73})
db.child("product_db").child(74).set({"name": "Steamed Milk", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 74})
db.child("product_db").child(75).set({"name": "Vanilla Crème", "category": "Hot Drinks", "sub-category": "Steamers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 75})


db.child("product_db").child(76).set({"name": "Star Drink", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 76})
db.child("product_db").child(77).set({"name": "Kiwi Starfruit Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 77})
db.child("product_db").child(78).set({"name": "Kiwi Starfruit Lemonade Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 78})
db.child("product_db").child(79).set({"name": "Dragon Drink", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 79})
db.child("product_db").child(80).set({"name": "Mango Dragonfruit Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 80})
db.child("product_db").child(81).set({"name": "Mango Dragonfruit Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 81})
db.child("product_db").child(82).set({"name": "Mango Dragonfruit Lemonade Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 82})
db.child("product_db").child(83).set({"name": "Strawberry Açaí Lemonade Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 83})
db.child("product_db").child(84).set({"name": "Pink Drink", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 84})
db.child("product_db").child(85).set({"name": "Strawberry Açaí Starbucks Refreshers Beverage", "category": "Cold Drinks", "sub-category": "Starbucks Refreshers",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 85})

db.child("product_db").child(86).set({"name": "Lemonade", "category": "Cold Drinks", "sub-category": "Juice",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 86})
db.child("product_db").child(87).set({"name": "Blended Strawberry Lemonade", "category": "Cold Drinks", "sub-category": "Juice",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 87})

db.child("product_db").child(88).set({"name": "Milk", "category": "Cold Drinks", "sub-category": "Milk",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 88})

db.child("product_db").child(89).set({"name": "Water", "category": "Cold Drinks", "sub-category": "Water",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 89})

db.child("product_db").child(90).set({"name": "Chai Tea Latte", "category": "Hot Teas", "sub-category": "Chai Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 90})
db.child("product_db").child(91).set({"name": "Chai Tea", "category": "Hot Teas", "sub-category": "Chai Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 91})

db.child("product_db").child(92).set({"name": "Black Teas", "category": "Hot Teas", "sub-category": "Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 92})
db.child("product_db").child(93).set({"name": "London Fog Tea Latte", "category": "Hot Teas", "sub-category": "Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 93})
db.child("product_db").child(94).set({"name": "Royal English Breakfast Tea", "category": "Hot Teas", "sub-category": "Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": {0: "smooth"}, "id": 94})
db.child("product_db").child(95).set({"name": "Royal English Breakfast Tea Latte", "category": "Hot Teas", "sub-category": "Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 95})

db.child("product_db").child(96).set({"name": "Emperor’s Clouds & Mist", "category": "Hot Teas", "sub-category": "Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 96})
db.child("product_db").child(97).set({"name": "Matcha Tea Latte", "category": "Hot Teas", "sub-category": "Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 97})
db.child("product_db").child(98).set({"name": "Honey Citrus Mint Tea", "category": "Hot Teas", "sub-category": "Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 98})
db.child("product_db").child(99).set({"name": "Jade Citrus Mint Brewed Tea", "category": "Hot Teas", "sub-category": "Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 99})

db.child("product_db").child(100).set({"name": "Mint Majesty", "category": "Hot Teas", "sub-category": "Herbal Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 100})
db.child("product_db").child(101).set({"name": "Peach Tranquility", "category": "Hot Teas", "sub-category": "Herbal Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 101})


db.child("product_db").child(102).set({"name": "Iced Black Tea", "category": "Iced Teas", "sub-category": "Iced Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 102})
db.child("product_db").child(103).set({"name": "Iced Black Tea Lemonade", "category": "Iced Teas", "sub-category": "Iced Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 103})
db.child("product_db").child(104).set({"name": "Iced Royal English Breakfast Tea Latte", "category": "Iced Teas", "sub-category": "Iced Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 104})
db.child("product_db").child(105).set({"name": "Iced London Fog Tea Latte", "category": "Iced Teas", "sub-category": "Iced Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 105})

db.child("product_db").child(106).set({"name": "Iced Chai Tea Latte", "category": "Iced Teas", "sub-category": "Iced Chai Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 106})

db.child("product_db").child(107).set({"name": "Iced Peach Green Tea", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 107})
db.child("product_db").child(108).set({"name": "Iced Peach Green Tea Lemonade", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 108})
db.child("product_db").child(109).set({"name": "Iced Matcha Tea Latte", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 109})
db.child("product_db").child(110).set({"name": "Iced Green Tea", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 110})
db.child("product_db").child(111).set({"name": "Iced Green Tea Lemonade", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 111})
db.child("product_db").child(112).set({"name": "Iced Matcha Lemonade", "category": "Iced Teas", "sub-category": "Iced Green Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 112})

db.child("product_db").child(113).set({"name": "Iced Passion Tango Tea", "category": "Iced Teas", "sub-category": "Iced Herbal Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 113})
db.child("product_db").child(114).set({"name": "Iced Passion Tango Tea Lemonade", "category": "Iced Teas", "sub-category": "Iced Herbal Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 114})

db.child("product_db").child(115).set({"name": "Pistachio Coffee Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 115})
db.child("product_db").child(116).set({"name": "Sugar Cookie Almondmilk Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 116})
db.child("product_db").child(117).set({"name": "Sugar Cookie Almondmilk Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 117})
db.child("product_db").child(118).set({"name": "Toasted White Chocolate Mocha Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 118})
db.child("product_db").child(119).set({"name": "Peppermint White Chocolate Mocha Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 119})
db.child("product_db").child(120).set({"name": "Caramel Brulée Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 120})
db.child("product_db").child(121).set({"name": "Peppermint Mocha Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 121})
db.child("product_db").child(122).set({"name": "Mocha Cookie Crumble Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 122})
db.child("product_db").child(123).set({"name": "Chestnut Praline Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 123})
db.child("product_db").child(124).set({"name": "Caramel Ribbon Crunch Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 124})
db.child("product_db").child(125).set({"name": "Espresso Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 125})
db.child("product_db").child(126).set({"name": "Caffè Vanilla Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 126})
db.child("product_db").child(127).set({"name": "Caramel Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 127})
db.child("product_db").child(128).set({"name": "Coffee Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 128})
db.child("product_db").child(129).set({"name": "Mocha Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 129})
db.child("product_db").child(130).set({"name": "Java Chip Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 130})
db.child("product_db").child(131).set({"name": "White Chocolate Mocha Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Coffee Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 131})

db.child("product_db").child(132).set({"name": "Pistachio Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 132})
db.child("product_db").child(132).set({"name": "Sugar Cookie Almondmilk Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 132})
db.child("product_db").child(133).set({"name": "Peppermint White Chocolate Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 133})
db.child("product_db").child(134).set({"name": "Peppermint Mocha Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 134})
db.child("product_db").child(135).set({"name": "Caramel Brulée Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 135})
db.child("product_db").child(136).set({"name": "Chestnut Praline Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 136})
db.child("product_db").child(137).set({"name": "Toasted White Chocolate Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 137})
db.child("product_db").child(138).set({"name": "Chocolate Cookie Crumble Crème Frappuccino", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 138})
db.child("product_db").child(139).set({"name": "Caramel Ribbon Crunch Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 139})
db.child("product_db").child(140).set({"name": "Strawberry Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 140})
db.child("product_db").child(141).set({"name": "Chai Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 141})
db.child("product_db").child(142).set({"name": "Double Chocolaty Chip Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 142})
db.child("product_db").child(143).set({"name": "Matcha Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 143})
db.child("product_db").child(144).set({"name": "Vanilla Bean Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 144})
db.child("product_db").child(145).set({"name": "White Chocolate Crème Frappuccino Blended Beverage", "category": "Frappuccino Blended Beverages", "sub-category": "Creme Frappuccino",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": "placeholder", "id": 145})

db.child("cust_db").child(1).set({"name": "Oatmilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Oatmilk", 1: "Light Splash of Oatmilk",
                                                   2: "No Splash of Oatmilk", 3: "Splash of Oatmilk", 4: "Substitute Splash of Oatmilk"}, "id": 1})
db.child("cust_db").child(4).set({"name": "2% Milk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of 2% Milk", 1: "Light Splash of 2% Milk",
                                                   2: "No Splash of Oatmilk", 3: "Splash of 2% Milk"}, "id": 4})
db.child("cust_db").child(8).set({"name": "Almondmilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Almondmilk", 1: "Light Splash of Almondmilk",
                                                   2: "Splash of Almondmilk"}, "id": 8})

db.child("cust_db").child(11).set({"name": "Brown Sugar Syrup", "category": "Flavors", "sub-category": "Syrups",
                                          "opts": {0: "pump(s) Brown Sugar Syrup"}, "id": 11})

db.child("cust_db").child(23).set({"name": "Caramel Brulée Sauce", "category": "Flavors", "sub-category": "Sauces",
                                          "opts": {0: "pump(s) Caramel Brulée Sauce"}, "id": 23})
                                          
"""
"""
db.child("cust_db").child(1).set({"name": "Oatmilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Oatmilk", 1: "Light Splash of Oatmilk",
                                                   2: "No Splash of Oatmilk", 3: "Splash of Oatmilk", 4: "Substitute Splash of Oatmilk"}, "id": 1})
db.child("cust_db").child(2).set({"name": "Sweet Cream", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Sweet Cream", 1: "Light Splash of Sweet Cream",
                                                   2: "No Splash of Sweet Cream", 3: "Splash of Sweet Cream"}, "id": 2})
db.child("cust_db").child(3).set({"name": "Nonfat Milk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Nonfat Milk", 1: "Light Splash of Nonfat Milk",
                                                   2: "Splash of Nonfat Milk"}, "id": 3})
db.child("cust_db").child(4).set({"name": "2% Milk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of 2% Milk", 1: "Light Splash of 2% Milk",
                                                   2: "No Splash of Oatmilk", 3: "Splash of 2% Milk"}, "id": 4})
db.child("cust_db").child(5).set({"name": "Whole Milk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Whole Milk", 1: "Light Splash of Whole Milk",
                                                   2: "Splash of Whole Milk"}, "id": 5})
db.child("cust_db").child(6).set({"name": "Cream (Half & Half)", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Cream (Half & Half)", 1: "Light Splash of Cream (Half & Half)",
                                                   2: "Splash of Cream (Half & Half)"}, "id": 6})
db.child("cust_db").child(7).set({"name": "Heavy Cream", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Heavy Cream", 1: "Light Splash of Heavy Cream",
                                                   2: "Splash of Heavy Cream"}, "id": 7})
db.child("cust_db").child(8).set({"name": "Almondmilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Almondmilk", 1: "Light Splash of Almondmilk",
                                                   2: "Splash of Almondmilk"}, "id": 8})
db.child("cust_db").child(9).set({"name": "Coconutmilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Coconutmilk", 1: "Light Splash of Coconutmilk", 2: "No Splash of Coconutmilk",
                                                   3: "Splash of Coconutmilk"}, "id": 9})
db.child("cust_db").child(10).set({"name": "Soymilk", "category": "Add-ins", "sub-category": "Creamer",
                                          "opts": {0: "Extra Splash of Soymilk", 1: "Light Splash of Soymilk",
                                                   2: "Splash of Soymilk"}, "id": 10})
                                                   
                                                   
"""

db.child("product_db").child(94).set({"name": "Royal English Breakfast Tea", "category": "Hot Teas", "sub-category": "Black Teas",
                                          "cust_opts": {0: "cust_id goes here"}, "flavor": {0: "smooth"}, "id": 94})

cust = db.child("product_db").child(1).child("cust_opts").get()


test = db.child("product_db").child(1)

print(test.get().val()["name"])

print(db.child("cust_db").child(cust.val()[0]).get().val()["name"])



user = db.child("user-item-db").child("1XHftVUhoFhBeCoac0p2DhKfoos2").get()

#11
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
"""
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
    print(custDict)
    print(custCat)
    return render_template('submit.html', custRefs=custRefs, drink = drink, db = db, custDict = custDict, custCat = custCat)

@app.route('/submit', methods=['POST'])
def submit2():
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
    print(custDict)
    print(custCat)
    return render_template('submit.html', custRefs=custRefs, drink=drink, db = db, custCat = custCat, custDict = custDict)

@app.route('/friends/')
def friends():
    return render_template('friends.html')




if __name__ == "__main__":
    app.run(debug=True)

"""



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


db.child("product_db").child("cold_coffee").child("Cold Brews").child("Irish Cream Cold Brew").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    32, "name": "Irish Cream Cold Brew"})

db.child("product_db").child("cold_coffee").child("Cold Brews").child("Salted Caramel Cream Cold Brew").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    33, "name": "Salted Caramel Cream Cold Brew"})

db.child("product_db").child("cold_coffee").child("Cold Brews").child("Starbucks Reserve Cold Brew").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    34, "name": "Starbucks Reserve Cold Brew"})

db.child("product_db").child("cold_coffee").child("Cold Brews").child("Starbucks Cold Brew Coffee").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    35, "name": "Starbucks Cold Brew Coffee"})

db.child("product_db").child("cold_coffee").child("Cold Brews").child("Vanilla Sweet Cream Cold Brew").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    36, "name": "Vanilla Sweet Cream Cold Brew"})

db.child("product_db").child("cold_coffee").child("Cold Brews").child("Starbucks Cold Brew Coffee with Milk").set({"cust_type": "cold_brew", "flavor": "nutty", "id":
    37, "name": "Starbucks Cold Brew Coffee with Milk"})

db.child("product_db").child("cold_coffee").child("Nitro Cold Brews").child("Starbucks Reserve Nitro Cold Brew").set({"cust_type": "nitro", "flavor": "nutty", "id":
    38, "name": "Starbucks Reserve Nitro Cold Brew"})

db.child("product_db").child("cold_coffee").child("Nitro Cold Brews").child("Nitro Cold Brew").set({"cust_type": "nitro", "flavor": "nutty", "id":
    39, "name": "Nitro Cold Brew"})

db.child("product_db").child("cold_coffee").child("Nitro Cold Brews").child("Vanilla Sweet Cream Nitro Cold Brew").set({"cust_type": "nitro", "flavor": "nutty", "id":
    40, "name": "Vanilla Sweet Cream Nitro Cold Brew"})

db.child("product_db").child("cold_coffee").child("Iced Americano").child("Iced Caffè Americano").set({"cust_type": "iced_americano", "flavor": "nutty", "id":
    41, "name": "Iced Caffè Americano"})

db.child("product_db").child("cold_coffee").child("Iced Coffees").child("Iced Coffee").set({"cust_type": "iced_coffee", "flavor": "nutty", "id":
    42, "name": "Iced Coffee"})

db.child("product_db").child("cold_coffee").child("Iced Coffees").child("Iced Coffee with Milk").set({"cust_type": "iced_coffee", "flavor": "nutty", "id":
    43, "name": "Iced Coffee with Milk"})

db.child("product_db").child("cold_coffee").child("Iced Coffees").child("Iced Espresso").set({"cust_type": "iced_coffee", "flavor": "nutty", "id":
    44, "name": "Iced Espresso"})


db.child("product_db").child("cold_coffee").child("Iced Coffees").child("Iced Espresso").set({"cust_type": "iced_coffee", "flavor": "nutty", "id":
    45, "name": "Iced Espresso"})

db.child("product_db").child("cold_coffee").child("Iced Shaken Espresso").child("Iced Brown Sugar Oatmilk Shaken Espresso").set({"cust_type": "iced_shaken_espresso", "flavor": "nutty", "id":
    46, "name": "Iced Brown Sugar Oatmilk Shaken Espresso"})

db.child("product_db").child("cold_coffee").child("Iced Shaken Espresso").child("Iced Chocolate Almondmilk Shaken Espresso").set({"cust_type": "iced_shaken_espresso", "flavor": "nutty", "id":
    47, "name": "Iced Chocolate Almondmilk Shaken Espresso"})

db.child("product_db").child("cold_coffee").child("Iced Shaken Espresso").child("Iced Shaken Espresso").set({"cust_type": "iced_shaken_espresso", "flavor": "nutty", "id":
    48, "name": "Iced Shaken Espresso"})

db.child("product_db").child("cold_coffee").child("Iced Flat Whites").child("Iced Flat White").set({"cust_type": "iced_white", "flavor": "nutty", "id":
    49, "name": "Iced Flat White"})

db.child("product_db").child("cold_coffee").child("Iced Flat Whites").child("Iced Honey Almondmilk Flat White").set({"cust_type": "iced_white", "flavor": "nutty", "id":
    50, "name": "Iced Honey Almondmilk Flat White"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Pistachio Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    51, "name": "Iced Pistachio Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Sugar Cookie Almondmilk Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    52, "name": "Iced Sugar Cookie Almondmilk Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Chestnut Praline Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    53, "name": "Iced Chestnut Praline Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Caramel Brulée Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    54, "name": "Iced Caramel Brulée Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Starbucks Reserve Iced Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    55, "name": "Starbucks Reserve Iced Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Starbucks Reserve Iced Hazelnut Bianco Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    56, "name": "Starbucks Reserve Iced Hazelnut Bianco Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Caffè Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    57, "name": "Iced Caffè Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Cinnamon Dolce Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    58, "name": "Iced Cinnamon Dolce Latte"})

db.child("product_db").child("cold_coffee").child("Iced Lattes").child("Iced Starbucks Blonde Vanilla Latte").set({"cust_type": "iced_latte", "flavor": "nutty", "id":
    59, "name": "Iced Starbucks Blonde Vanilla Latte"})

db.child("product_db").child("cold_coffee").child("Iced Macchiatos").child("Iced Caramel Macchiato").set({"cust_type": "iced_macchiato", "flavor": "nutty", "id":
    60, "name": "Iced Caramel Macchiato"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Iced White Chocolate Mocha").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    61, "name": "Iced White Chocolate Mocha"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Iced Peppermint White Chocolate Mochao").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    62, "name": "Iced Peppermint White Chocolate Mocha"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Iced Toasted White Chocolate Mocha").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    63, "name": "Iced Toasted White Chocolate Mocha"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Iced Peppermint Mocha").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    64, "name": "Iced Peppermint Mocha"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Iced Caffè Mocha").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    65, "name": "Iced Caffè Mocha"})

db.child("product_db").child("cold_coffee").child("Iced Mochas").child("Starbucks Reserve Iced Dark Chocolate Mocha").set({"cust_type": "iced_mocha", "flavor": "nutty", "id":
    66, "name": "Starbucks Reserve Iced Dark Chocolate Mocha"})


"""