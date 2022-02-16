from unicodedata import category
from timeHelpers import getTimeCategory
# from main import db, auth, person

class Item:
    def __init__(self, name, formCode, sizeCode, quantity, instructions):
        self.name = name
        self.formCode = formCode
        self.sizeCode = sizeCode
        self.quantity = quantity
        self.instructions = instructions

class Order:
    def __init__(self, name, category, itemList):
        self.name = name
        self.category = category
        self.itemList = itemList
    
# to get list of orders
def getOrders(inventory):
    order_list = []
    for order in inventory:
        # print(order)
        order_list.append(order)
    
    orders = []
    for order in order_list:
        category = inventory[order]['category'] 
        items_dic = inventory[order]['items']
        itemList = []
        for i in items_dic:
            formCode = items_dic[i]['formCode']
            instructions = items_dic[i]['instructions']
            name = items_dic[i]['name']
            quantity = items_dic[i]['quantity']
            sizeCode = items_dic[i]['sizeCode']
            item = Item(name, formCode, sizeCode, quantity, instructions)
            itemList.append(item)
        cur = Order(order, category, itemList)
        orders.append(cur)
    
    return orders


# TO GET TIME-BASED ORDERS
def getCurOrder(orders):
    curTime = getTimeCategory()
    print(len(orders))
    toBeDisplay = []
    
    for order in orders:
        if curTime == order.category:
            print(order.name)
            toBeDisplay.append(order)
    
    # print(len(toBeDisplay))
    # get itemLists
    itemLists = []
    for order in toBeDisplay:
        # print(order.name)
        itemLists.append(order.itemList)
    
    return [toBeDisplay, itemLists]
