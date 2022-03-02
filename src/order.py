from unicodedata import category
from timeHelpers import getTimeCategory
from dbInit import db
# from main import db, auth, person

class Item:
    def __init__(self, name, customizations, sizeCode, quantity, instructions):
        self.name = name
        self.customizations = customizations
        self.sizeCode = sizeCode
        self.quantity = quantity
        self.instructions = instructions
        
class Customization:
    def __init__(self, name, option):
        self.name = name
        self.option = option
        
class Order:
    def __init__(self, name, category, itemList):
        self.name = name
        self.category = category
        self.itemList = itemList
    
# to get all available order of the user
def getOrderList(inventory):
    order_list = []
    for order in inventory:
        # print(order)
        order_list.append(order)
    
    orders = []
    for order in order_list:
        category = inventory[order]['category'] 
        items_dic = inventory[order]['items']
        itemList = []
        # print(order)
        for i in items_dic:
            # print(i)
            customizations = []
            instructions = items_dic[i]['instructions']
            name = items_dic[i]['name']
            # print(name)
            quantity = items_dic[i]['quantity']
            sizeCode = items_dic[i]['sizeCode']
            custom_inventory = items_dic[i]['customizations']
            # get customizations
            for k in custom_inventory:
                if (k != None):
                    custom_name = db.child('cust_db').child(k).child('name').get().val()
                    opt_id = custom_inventory[k]
                    # print(opt_id)
                    custom_option = db.child('cust_db').child(k).child('opts').child(opt_id).get().val()
                    custom = Customization(custom_name, custom_option)
                    print(custom_name, custom_option)
                    customizations.append(custom)
            item = Item(name, customizations, sizeCode, quantity, instructions)
            itemList.append(item)
        cur = Order(order, category, itemList)
        orders.append(cur)
    
    return orders


# TO GET TIME-BASED ORDERS
def getUsualOrders(orders):
    
    curTime = getTimeCategory()
    usualOrders = []
    
    for order in orders:
        if curTime == order.category:
            # print(order.name)
            usualOrders.append(order)

    return usualOrders


# Init Usual Order
# Querying database and pass it to getOrderList and getUsualOrders
def userOrderInit(user_id, db):
    
    order_list = []
    usualOrders = []
    fav_db = db.child("fav_db")
    user_rf = fav_db.child(user_id)
    inventory = user_rf.get().val()
    order_list = getOrderList(inventory)
    usualOrders = getUsualOrders(order_list)
    
    return [order_list, usualOrders]
    
    
# Sort out usual orders that going to be display in the index page (index.html)
# Currently only displays maximum 2 orders and 2 items in each order
def getToBeDisplayIndex(usualOrders):
    
    curDisplayOrder = []

    for order in usualOrders:
        # print(order.name)
        itemList = order.itemList
        toBeDisplay = str(order.name) + ": "
        for i in range(len(itemList)):
            if i >= 2: 
                toBeDisplay += "..."
                break
            curItem = itemList[i]
            
            toBeDisplay += str(curItem.quantity) + " "
            toBeDisplay += curItem.sizeCode + " "
            toBeDisplay += curItem.name
            if i < 1 and len(itemList) > 1:
                toBeDisplay += ", "
        curDisplayOrder.append(toBeDisplay)
        # print(toBeDisplay)

    return curDisplayOrder




# from app import firebase
# db = firebase.database()
# user_id = "NzkGCghmk4MO4mCjwn3DQ8n3LxH2"
# [order_list, usualOrders] = userOrderInit(user_id, db)