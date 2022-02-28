from re import sub
import pyrebase


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

class Drink:
    def __init__(self, name, cat, subcat, flavor, opts, id):  
        self.id = id
        self.name = name
        self.cat = cat
        self.subcat = subcat  
        self.flavor = flavor
        self.opts = opts
    

def getDrinkList():
    product_db_ref = db.child("product_db")
    inventory = product_db_ref.get().val()
    drink_list = []
    for i in range(1, 146):
        try:
            cur_subcat = inventory[i]['sub-category']
            cur_name = inventory[i]['name']
            cur_cat = inventory[i]['category']
            cur_flavor = inventory[i]['flavor']
            cur_opts = inventory[i]['cust_opts']
            cur_drink = Drink(cur_name, cur_cat, cur_subcat, cur_flavor, cur_opts, i)
            drink_list.append(cur_drink)
        except:
            print("error getting drink at",i)
    return drink_list

# initial drink list
drinkList = getDrinkList()

def getDrinkCatDic():
    drinkCat_dic = {}
    subcat_dic = {}
    subcat_cat_dic = {}
    for item in drinkList:
        subcat = item.subcat
        cat = item.cat
        try:        
            # name = item.name
            if subcat in subcat_dic.keys():
                subcat_dic[subcat].append(item)
                # print("in")
            else:
                subcat_dic.update({subcat: []})
                subcat_dic[subcat].append(item)
            
            subcat_cat_dic.update({subcat: cat})
        except:
            print("error at cat:",cat)
    
    
    for key in subcat_dic:
        
        itemList = subcat_dic[key]
        curDic = {key: itemList}
        # print(curDic)
        try:
            
        
            cat = subcat_cat_dic[key]
            
            if cat in drinkCat_dic:
                drinkCat_dic[cat].update(curDic)
            else:          
                drinkCat_dic.update({cat: curDic})
            # print(drinkCat_dic)
        except:
            print("error at cat:", cat)
        
    
    return drinkCat_dic

drinkCat_dic = getDrinkCatDic()
# print(drinkCat_dic)

# for cat in drinkCat_dic:
#     # print(cat)
#     for subcat in drinkCat_dic[cat]:
#         for item in drinkCat_dic[cat][subcat]:
#             print(item.name)
        