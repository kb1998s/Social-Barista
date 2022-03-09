# from typing_extensions import Self
from ast import iter_child_nodes
from asyncio.windows_events import NULL
from itertools import count
from turtle import update
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
    def __init__(self, name, category, itemList, orderCount):
        self.name = name
        self.category = category
        self.itemList = itemList
        self.orderCount = orderCount
    
# GET ALL AVAILABLE ORDERS OF CURRENT USER
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
        orderCount = inventory[order]['order_count']
        itemList = []
        
        if items_dic == 'none':
            cur = Order(order, category, itemList, orderCount)
            orders.append(cur)
            continue
        
        for name in items_dic:
            customizations = {}
            instructions = items_dic[name]['instructions']
            quantity = items_dic[name]['quantity']
            sizeCode = items_dic[name]['sizeCode']
            custom_inventory = items_dic[name]['customizations']
            drink_id = items_dic[name]['drink_id']
            drink_category = items_dic[name]['category']

            # load custom for each item
            if custom_inventory != 'none':
                for cust in custom_inventory:
                    if (cust != None and cust != 'bug_holder'):
                        custom_name = db.child('cust_db').child(cust).child('name').get().val()
                        custom_option = custom_inventory[cust]
                        custom = {custom_name: custom_option}
                        # print(custom)
                        customizations.update(custom)
            else: customizations = 'none'
            
            item = Item(name, customizations, sizeCode, quantity, instructions, drink_category, drink_id)
            itemList.append(item)
            
        cur = Order(order, category, itemList, orderCount)
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

# TO GET COUNT-BASED ORDERS:
def getCountBasedOrder(orders):
    import heapq
    def sortkey(order):
        return order.orderCount
    heapOrders = heapq.nlargest(1, orders, key=sortkey)
    return heapOrders
    # print(heapOrders[0].name)


# INIT USUAL ORDER
# Querying database and pass it to getOrderList and getUsualOrders
def userOrderInit(user_id):
    
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
    print(usualOrders)
    if usualOrders == []:
        return ['No custom orders have been saved into the system yet.']
    for order in usualOrders:
        # print(order.name)
        itemList = order.itemList
        toBeDisplay = str(order.name).upper() + ": "
        for i in range(len(itemList)):
            if i >= 2: 
                toBeDisplay += "..."
                break
            curItem = itemList[i]
            if curItem.category == 'custom':
                toBeDisplay += str(curItem.quantity) + " "
                toBeDisplay += curItem.name
            else:
                toBeDisplay += str(curItem.quantity) + " "
                toBeDisplay += curItem.sizeCode + " "
                toBeDisplay += curItem.name
            if i < 1 and len(itemList) > 1:
                toBeDisplay += ", "
        curDisplayOrder.append(toBeDisplay)
        print("RS Display:", toBeDisplay)
        
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
            'items': 'none',
            'added-orders': 'none',
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
        return Order('cart', category, [], 0) 
        
    for item in items_dic:
        customizations = {}
        instructions = items_dic[item]['instructions']
        name = item
        quantity = items_dic[item]['quantity']
        sizeCode = items_dic[item]['sizeCode']
        custom_inventory = items_dic[item]['customizations']
        drink_category = items_dic[item]['category']
        # load custom for each item
        print(custom_inventory)
        if custom_inventory != 'none':
            for cust in custom_inventory:
                if (cust != None and cust != 'bug_holder'):
                    print(cust,' ',item)
                    custom_name = db.child('cust_db').child(cust).child('name').get().val()
                    custom_option = custom_inventory[cust]
                    custom = {custom_name: custom_option}
                    print(custom)
                    customizations.update(custom)
        else: customizations = 'none'
        drink_id =  items_dic[item]['drink_id']
        category = items_dic[item]['category']
        
        curItem = Item(name, customizations, sizeCode, quantity, instructions, drink_category, drink_id)
        itemList.append(curItem)
     
    cart = Order('cart', category, itemList, 0)
    return cart

# UPDATE Order FROM DB
def getOrder(userId, orderId):
    inventory = db.child('fav_db').child(userId).child(orderId).get().val()
    category = inventory['category'] 
    items_dic = inventory['items']
    orderCount = inventory['order_count']
    itemList = []
    if items_dic == 'none':
        return Order(orderId, category, [], orderCount) 
        
    for item in items_dic:
        customizations = {}
        instructions = items_dic[item]['instructions']
        name = item
        quantity = items_dic[item]['quantity']
        sizeCode = items_dic[item]['sizeCode']
        custom_inventory = items_dic[item]['customizations']
        # load custom for each item
        if custom_inventory != 'none':
            for cust in custom_inventory:
                if (cust != None and cust != 'bug_holder'):
                    custom_name = db.child('cust_db').child(cust).child('name').get().val()
                    custom_option = custom_inventory[cust]
                    custom = {custom_name: custom_option}
                    print(custom)
                    customizations.update(custom)
        else: customizations = 'none'
                  
        id =  items_dic[item]['drink_id']
        item_category = items_dic[item]['category']
        
        curItem = Item(name, customizations, sizeCode, quantity, instructions, item_category, id)
        itemList.append(curItem)
     
    order = Order(orderId, category, itemList, orderCount)
    return order

# UPDATE GIVEN QUANTITY AND SIZES INSIDE THE CART
def updateCart(userId, request):
    inventory = db.child('fav_db').child(userId).child('cart').get().val()
    timeCategory = getTimeCategory()
    items = inventory['items']
    if (items == 'none'): 
        print('There is no item in cart')
        return
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
        
        items_dic.update(item_dic)
    
    toBeUpdated = {
        'category': timeCategory,
        'items': items_dic
    }
    
    # update to db
    db.child('fav_db').child(userId).child('cart').update(toBeUpdated)

# UPDATE GIVEN QUANTITY AND SIZES FOR EACH DRINK AND CATEGORY INSIDE THE ORDER
def updateOrder(userId, orderId, request):
    inventory = db.child('fav_db').child(userId).child(orderId).get().val()
    timeCategory = request.form.get('time-category')
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
    db.child('fav_db').child(userId).child(orderId).update(toBeUpdated)

# SAVE ORDER FROM CART
def saveOrderFromCart(userId, request):

    inventory = db.child('fav_db').child(userId).child('cart').get().val()
    order_name = request.form.get('order')
    if order_name == '': 
        return
    order_instruction = request.form.get('instructions')
    if order_instruction == '': order_instruction = 'none'
    inventory.update({
        'instructions': order_instruction,
        'order_count': 1
        })
    toBeUpdated = {
        order_name: inventory
    }
    
    # db update new order
    db.child('fav_db').child(userId).update(toBeUpdated)
    
# REMOVE ALL ITEM FROM THE CART
def cartReInit(userId):
    cartReInit = {
        'category': getTimeCategory(),
        'items': 'none',
        'added-orders': 'none',
    }
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
        value = request.form.get(str(opts[i]))
        if value != "" and value != "None" and value != None:
            cusDict.update({
                str(cusList[i]) : value
            })
            

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
    else: cusDict.update({"bug_holder": "bug_holder"})
    if custDrinkInstructions == '': custDrinkInstructions = "none"
    if sizeCode == None: sizeCode= 'short'
    item = {
        custDrinkName : {
                'drink_id': drink_id, 
                'customizations': cusDict,
                'instructions': custDrinkInstructions,
                'quantity': 1,
                'sizeCode': sizeCode,
                'category': 'custom',
            }
    }
    
    # DB cart updating
    db.child('fav_db').child(userId).child('cart').update({'category': timeCategory})
    db.child('fav_db').child(userId).child('cart').child('items').update(item)
    
# ADD CUSTOM ITEM TO CART
def customizeItemFromOrder(request, userId, orderId):
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
        value = request.form.get(str(opts[i]))
        if value != "" and value != "None" and value != None:
            cusDict.update({
                str(cusList[i]) : value
            })
            

    custDrinkName = request.form.get('custDrinkName')
    custDrinkInstructions = request.form.get('custDrinkInstruction')
    
    
    # Processing cus drink name
    if custDrinkName == '':
        custDrinkName = 'Custom' + ' ' + drinkName + ' ' + '1'
        item_name_dic = db.child('fav_db').child(userId).child(orderId).child('items').shallow().get().val()
        counter = 1
        while custDrinkName in item_name_dic:
            custDrinkName = custDrinkName[:len(custDrinkName) - 1] + str(counter)
            counter += 1
    
    print(cusDict)
    # Updating item to cart
    if cusDict == {}: cusDict = "none"
    else: cusDict.update({"bug_holder": "bug_holder"})
    if custDrinkInstructions == '': custDrinkInstructions = "none"
    if sizeCode == None: sizeCode= 'short'
    item = {
        custDrinkName : {
                'drink_id': drink_id, 
                'customizations': cusDict,
                'instructions': custDrinkInstructions,
                'quantity': 1,
                'sizeCode': sizeCode,
                'category': 'custom',
            }
    }
    print('to be updated', item)
    
    # DB cart updating
    # db.child('fav_db').child(userId).child(orderId).update({'category': timeCategory})
    db.child('fav_db').child(userId).child(orderId).child('items').update(item)

# REMOVE AN ITEM FROM CART GIVEN ITS IT
def removeItemFromCart(userId, drinkId):
    timeCategory = getTimeCategory()
    # print(drinkId)
    db.child('fav_db').child(userId).child('cart').update({'category': timeCategory})
    keys = db.child('fav_db').child(userId).child('cart').child('items').shallow().get().val()
    if len(keys) == 1 and drinkId in keys:
        db.child('fav_db').child(userId).child('cart').update({'items': 'none'})
    else:
        db.child('fav_db').child(userId).child('cart').child('items').child(drinkId).remove()

# REMOVE AN ITEM FROM AN ORDER GIVEN ITS ID
def removeItemFromOrder(userId, drinkId, orderId):
    keys = db.child('fav_db').child(userId).child(orderId).child('items').shallow().get().val()
    
    print(drinkId, keys)
    if len(keys) == 1 and drinkId in keys:
        db.child('fav_db').child(userId).child(orderId).update({'items': 'none'})
    elif drinkId in keys:
        db.child('fav_db').child(userId).child(orderId).child('items').child(drinkId).remove()

# REMOVE AN ORDER FROM SAVED ORDERS PAGE
def removeSavedOrder(userId, orderID):
    db.child('fav_db').child(userId).child(orderID).remove()
    print("Removed", orderID)
    
# ADD ALL ITEMS OF A SAVED ORDERS TO CART
def addOrderToCart(userId, orderId):
    # order init
    inventory = db.child('fav_db').child(userId).child(orderId).get().val()
    itemList = inventory['items']
    order_count = inventory['order_count']
    cart_inventory = db.child('fav_db').child(userId).child('cart').get().val()
    cart_itemList = cart_inventory['items']
    addedOrders = cart_inventory['added-orders']
    
    if addedOrders == 'none': 
        addedOrders = { orderId: order_count}
    else: addedOrders.update({orderId: order_count})
    
    if cart_itemList == 'none': cart_itemList = itemList
    
    elif itemList != 'none':
        for item in itemList:
            cart_itemList.update({
                item: itemList[item]
            })
    
    toBeUpdated = {
        'items': cart_itemList,
        'added-orders': addedOrders
    }
    print(toBeUpdated)
    # DB update
    db.child('fav_db').child(userId).child('cart').update(toBeUpdated)
    
# UPDATE ORDER COUNT OF AN ORDER OF A USER
def updateOrderCount(userId):
    addedOrders = db.child('fav_db').child(userId).child('cart').child('added-orders').get().val()
    orderList = db.child('fav_db').child(userId).shallow().get().val()
    for order in addedOrders:
        if order not in orderList:
            continue
        order_count = int(addedOrders[order]) + 1
        toBeUpdated = {
            'order_count': order_count
        }
        db.child('fav_db').child(userId).child(order).update(toBeUpdated)
    
def updateDrinkCount(userId):
    drinkList = []
    items = db.child('fav_db').child(userId).child('cart').child('items').get().val()
    count_dic = db.child('user-item-db').child(userId).get().val()
    if items == 'none': 
        print('There is no drink inside the cart to submit')
        return
    if count_dic == None : count_dic = {}
    count_dic.update({'bug_holder': 'bug_holder'})
    
    for item in items:
        drinkList.append(items[item]['drink_id'])
    
    for item in drinkList:
        if item in count_dic:
            item_count = int(count_dic[item]) + 1
        else:
            item_count = 1
        item_dic = {item: item_count}
        count_dic.update(item_dic)
    
    if count_dic == {}: 
        return   
    
    # print(count_dic)
    keys = db.child('user-item-db').shallow().get().val()
    if userId not in keys:
        db.child('user-item-db').child(userId).set(count_dic)
    else:
        db.child('user-item-db').child(userId).update(count_dic)
    
    