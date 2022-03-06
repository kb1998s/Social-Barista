# from typing_extensions import Self
from asyncio.windows_events import NULL
from itertools import count
from unicodedata import category
from timeHelpers import getTimeCategory
from dbInit import db
from DrinkLoader import drinkList
# from main import db, auth, person

class Item:
    def __init__(self, name, customizations, sizeCode, quantity, instructions, category, id):
        self.name = name
        self.customizations = customizations
        self.sizeCode = sizeCode
        self.quantity = quantity
        self.instructions = instructions
        self.category = category
        self.id = id

class Customization:
    def __init__(self, name, option):
        self.name = name
        self.option = option
    def getDict(self):
        return {self.name: self.option}
        
class Order:
    def __init__(self, name, category, itemList):
        self.name = name
        self.category = category
        self.itemList = itemList
    
# GET ALL AVAILABLE ORDERS OF CURRENT USER
# need to fix category tag for drink
def getOrderList(inventory):
    order_list = []
    for order in inventory:
        # print(order)
        order_list.append(order)
    
    orders = []
    for order in order_list:
        if order == 'cart': 
            continue
        
        category = inventory[order]['category'] 
        items_dic = inventory[order]['items']
        itemList = []
    
        for name in items_dic:
            customizations = []
            instructions = items_dic[name]['instructions']
            quantity = items_dic[name]['quantity']
            sizeCode = items_dic[name]['sizeCode']
            custom_inventory = items_dic[name]['customizations']
            drink_id = items_dic[name]['drink_id']
            drink_category = items_dic[name]['category']

            # load custom for each item
            if custom_inventory != 'none':
                for cust in custom_inventory:
                    if (cust != None):
                        custom_name = db.child('cust_db').child(cust).child('name').get().val()
                        custom_option = custom_inventory[cust]
                        custom = Customization(custom_name, custom_option)
                        customizations.append(custom)

            item = Item(name, customizations, sizeCode, quantity, instructions, drink_id, drink_category)
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


# INIT USUAL ORDER
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
        print(toBeDisplay)
        
    return curDisplayOrder



    
# SAVE CURRENT CART TO DB:
def saveOrder(order, userId):
    items_dic = {}
    for item in order.itemList:
        items_dic.update({
            item.id : {
                'name': item.name,
               'customizations': item.customizations,
               'instructions': item.instructions,
               'quantity': item.quantity,
               'sizeCode': item.sizeCode
            }
        })
        
    toBeSubmitted = {
        order.name : {
            'category': order.category,
            'items': items_dic
        }
    }
    keys_dic = db.child("fav_db").shallow().get().val()
    if userId in keys_dic:
        db.child('fav_db').child(userId).set(toBeSubmitted)
    else:
        db.child('fav_db').child(userId).update(toBeSubmitted)  
    
    print(toBeSubmitted)

# CART INIT
def cartInit(userId):
    timeCategory = getTimeCategory()
    cartInit = {
        'cart' : {
            'category': timeCategory,
            'items': 'none'
        }
    }
    # init card in db if user is not in favdb yet
    keys_dic = db.child("fav_db").shallow().get().val()
    if userId not in keys_dic:
        db.child('fav_db').child(userId).set(cartInit)
        print('init',userId,' and cart in favdb')
    orders_dic = db.child('fav_db').child(userId).shallow().get().val()
    
    if 'cart' not in orders_dic:
        db.child('fav_db').child(userId).update(cartInit)
        print('init cart in favdb')
    

# UPDATE CART FROM DB
def getCart(userId):
    inventory = db.child('fav_db').child(userId).child('cart').get().val()
    category = inventory['category'] 
    items_dic = inventory['items']
    itemList = []
    if items_dic == 'none':
        return Order('cart', category, []) 
        
    for item in items_dic:
        instructions = items_dic[item]['instructions']
        name = item
        quantity = items_dic[item]['quantity']
        sizeCode = items_dic[item]['sizeCode']
        customizations = items_dic[item]['customizations']
        id =  items_dic[item]['drink_id']
        category = items_dic[item]['category']
        
        curItem = Item(name, customizations, sizeCode, quantity, instructions, category, id)
        itemList.append(curItem)
     
    cart = Order('cart', category, itemList)
    return cart

# UPDATE GIVEN QUANTITY AND SIZES INSIDE THE CART
def updateCart(userId, request):
    inventory = db.child('fav_db').child(userId).child('cart').get().val()
    timeCategory = getTimeCategory()
    items = inventory['items']
    
    items_dic = {}
    for name in items:
        instructions = items[name]['instructions']
        customizations = items[name]['customizations']
        id =  items[name]['drink_id']
        category = items[name]['category']
        quantity = name + '-' + 'quantity'
        sizeCode = name + '-' + 'sizeCode'
        new_quantity = request.form.get(quantity)
        new_sizeCode = request.form.get(sizeCode)
        
        if new_quantity == '': new_quantity = 1
        if new_sizeCode == None: new_sizeCode = 'short'
        item_dic = {
            name: {
                'drink_id': id, 
                'customizations': customizations,
                'instructions': instructions,
                'quantity': new_quantity,
                'sizeCode': new_sizeCode,
                'category': category
            }
        }
        # print(item_dic)
        items_dic.update(item_dic)
    
    toBeUpdated = {
        'category': timeCategory,
        'items': items_dic
    }
    
    # update to db
    db.child('fav_db').child(userId).child('cart').update(toBeUpdated)

# SAVE ORDER FROM CART
def saveOrderFromCart(userId, request):

    inventory = db.child('fav_db').child(userId).child('cart').get().val()
    order_name = request.form.get('order')
    order_instruction = request.form.get('instructions')
    if order_instruction == '': order_instruction = 'none'
    inventory.update({'instructions': order_instruction })
    toBeUpdated = {
        order_name: inventory
    }
    cartReInit = {
        'category': inventory['category'],
        'items': 'none'
    }
    # db update new order, and remove all item from vard
    db.child('fav_db').child(userId).update(toBeUpdated)
    db.child('fav_db').child(userId).child('cart').update(cartReInit)
    
    
# ADD ITEM TO CART    
def addItemToCart(userId, drinkId):
    drinkName = drinkList[int(drinkId) - 1].name
    timeCategory = getTimeCategory()
    
    item = {
        drinkName : {
                'drink_id': drinkId, 
                'customizations': 'none',
                'instructions': 'none',
                'quantity': 1,
                'sizeCode': 'short',
                'category': 'default'
            }
    }
    
    # DB cart updating
    db.child('fav_db').child(userId).child('cart').update({'category': timeCategory})
    db.child('fav_db').child(userId).child('cart').child('items').update(item)
    return 
    
# ADD CUSTOM ITEM TO CART
def addCustomItemToCart(request, userId):
    drink_id = request.form.get('drinkid')
    sizeCode = request.form.get('sizeCode')
    drinkRef = db.child("product_db").child(int(drink_id)).get()
    drinkName = drinkList[int(drink_id) - 1].name
    cusDict = {}
    cusList = []
    opts = drinkRef.val()["cust_opts"]

    for i in opts:
        cusList.append(db.child("cust_db").child(int(i)).get().val()["id"])

    for i in range(len(cusList)):
        if request.form.get(str(opts[i])) != "":
            cusDict[str(cusList[i])] = request.form.get(str(opts[i]))

    custDrinkName = request.form.get('custDrinkName')
    custDrinkInstructions = request.form.get('custDrinkInstruction')
    
    # Get time category
    timeCategory = getTimeCategory()
    
    # Processing cus drink name
    if custDrinkName == '':
        custDrinkName = 'Custom' + ' ' + drinkName + ' ' + '1'
        item_name_dic = db.child('fav_db').child(userId).child('cart').child('items').shallow().get().val()
        counter = 1
        while custDrinkName in item_name_dic:
            custDrinkName = custDrinkName[:len(custDrinkName) - 1] + str(counter)
            counter += 1
    
    # Updating item to cart
    if cusDict == {}: cusDict = "none"
    if custDrinkInstructions == '': custDrinkInstructions = "none"
    item = {
        custDrinkName : {
                'drink_id': drink_id, 
                'customizations': cusDict,
                'instructions': custDrinkInstructions,
                'quantity': 1,
                'sizeCode': sizeCode,
                'category': 'custom'
            }
    }
    
    # DB cart updating
    db.child('fav_db').child(userId).child('cart').update({'category': timeCategory})
    db.child('fav_db').child(userId).child('cart').child('items').update(item)

# REMOVE AN ITEM FROM CART GIVEN ITS IT
def removeItemFromCart(userId, drinkId):
    timeCategory = getTimeCategory()
    print(drinkId)
    db.child('fav_db').child(userId).child('cart').update({'category': timeCategory})
    keys = db.child('fav_db').child(userId).child('cart').child('items').child(drinkId).shallow().get().val()
    if len(keys) == 1 and drinkId in keys:
        db.child('fav_db').child(userId).update({'cart': 'none'})
    else:
        db.child('fav_db').child(userId).child('cart').child('items').child(drinkId).remove()
