# Import datetime library
from datetime import datetime
datetime.now().strftime('%Y-%m-%d')

# Import OrderedDict to sort customer
from collections import OrderedDict

# Bool to keep track of which page user is on
isAdmin=False
loggedIn=False
isShopping=False 
isBuying=False
username=None

# Initialization for filtering and sorting, and total purchase
filProd=[]
listProduct=[]
filCust={}
total=0

customer = {
    'user1': {
        'password':'abc123', 
        'name':'Obiwan', 
        'date_joined':'2021-01-01',
        'transactions':[100000,20000]},
    'organa': {
        'password':'abc123', 
        'name':'Leia', 
        'date_joined':'2022-02-11',
        'transactions':[400000]},
    'skywalker': { 
        'password':'abc123', 
        'name':'Anakin', 
        'date_joined':'2023-12-18',
        'transactions':[]},
    'amidala': {
        'password':'abc123', 
        'name':'Padme',
        'date_joined':'2020-11-1',
        'transactions':[100000,1200000]},
    'ned': {
        'password':'abc123', 
        'name':'Ned Stark',
        'date_joined':'2022-09-21',
        'transactions':[]},
    'dany': {
        'password':'abc123', 
        'name':'Daenerys',
        'date_joined':'2020-09-1',
        'transactions':[100000,300000,299900,599900]},
    'runin': {
        'password':'abc123', 
        'name':'Rin',
        'date_joined':'2019-04-15',
        'transactions':[]},
    'venus': {
        'password':'abc123', 
        'name':'Aphrodite',
        'date_joined':'2022-04-21',
        'transactions':[1999900,2999900,5999900]},
    'mars': {
        'password':'abc123', 
        'name':'Ares',
        'date_joined':'2022-09-10',
        'transactions':[100000,100000,100000,100000,100000]},
    'neptune': {
        'password':'abc123', 
        'name':'Poseidon',
        'date_joined':'2021-03-10',
        'transactions':[50000000,1000000]} 
        
    }

product = [
    {'prod_id':0,
     'name':'Mini Dress with Zip',
     'category':'Dresses',
     'stock':225,
     'sold':142,
     'price':799900
     },
     {'prod_id':1,
     'name':'Denim Midi Dress',
     'category':'Dresses',
     'stock':234,
     'sold':901,
     'price':799900
     },
     {'prod_id':2,
     'name':'White Maxi Dress',
     'category':'Dresses',
     'stock':101,
     'sold':199,
     'price':1099000
     },
    {'prod_id':3,
     'name':'Pleated High Neck Top',
     'category':'Tops',
     'stock':1010,
     'sold':20,
     'price':399000
     },
     {'prod_id':4,
     'name':'Asymmetric Draped Top',
     'category':'Tops',
     'stock':100,
     'sold':99,
     'price':549000
     },
     {'prod_id':5,
     'name':'Ribbed Polo Neck T-Shirt',
     'category':'Tops',
     'stock':0,
     'sold':720,
     'price':4999000
     },
     {'prod_id':6,
     'name':'Black Silk Wrap Dress',
     'category':'Dresses',
     'stock':100,
     'sold':25,
     'price':999900
     },
     {'prod_id':7,
     'name':'Pink Sweater',
     'category':'Tops',
     'stock':199,
     'sold':19,
     'price':399000
     },
     {'prod_id':8,
     'name':'Polkadot Mini Dress',
     'category':'Dresses',
     'stock':19,
     'sold':295,
     'price':1999900
     },
     {'prod_id':9,
     'name':'Fitted Off Shoulder Knit TOp',
     'category':'Tops',
     'stock':299,
     'sold':55,
     'price':499900
     },

     {'prod_id':10,
     'name':'Belted Tube Top',
     'category':'Tops',
     'stock':199,
     'sold':0,
     'price':299900
     },
     {'prod_id':11,
     'name':'Abstract Satin Bias Cut Midi Dress',
     'category':'Dresses',
     'stock':199,
     'sold':101,
     'price':999900
     },
     {'prod_id':12,
     'name':'Tailored Blazer Dress',
     'category':'Dresses',
     'stock':190,
     'sold':10,
     'price':1999900
     },
     {'prod_id':13,
     'name':'Halter Bias Cut Midi Dress',
     'category':'Dresses',
     'stock':910,
     'sold':190,
     'price':699900
     },
     {'prod_id':14,
     'name':'Knit Boat Neck Shift Mini Dress',
     'category':'Dresses',
     'stock':65,
     'sold':105,
     'price':650000
     },
     {'prod_id':15,
     'name':'Pleated Boat Neck Crop Top',
     'category':'Tops',
     'stock':61,
     'sold':475,
     'price':459900
     },
     {'prod_id':16,
     'name':'Shoulder Padded V-neck Top',
     'category':'Tops',
     'stock':488,
     'sold':8,
     'price':599900
     },
     {'prod_id':17,
     'name':'Tweed Blouse',
     'category':'Tops',
     'stock':383,
     'sold':120,
     'price':650900
     },
     {'prod_id':18,
     'name':'Polka Dot Tiered Sleeve Top',
     'category':'Dresses',
     'stock':6,
     'sold':450,
     'price':559000
     },
     {'prod_id':19,
     'name':'Peplum Collar Shirt',
     'category':'Dresses',
     'stock':100,
     'sold':35,
     'price':999900
     },
]

cart = []
# [
#     [5, 10, price5*10],
#     [1, 1, price1*1]
# ]

# UTIL
def find_index(dicts, key, value):
    class Null: pass
    for i, d in enumerate(dicts):
        if d.get(key, Null) == value:
            return i
    else:
        return -999

def valiDate(dateString):
    try:
        datetime.strptime(dateString, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    
# MENU FUNCTIONS
def menuAdmin():
    global loggedIn
    global isAdmin
    while True:
        print('\n-------------------------- NewThreads Administrator Menu -------------------------')
        print(''' 
    1. View data\r
    2. Add new data\r
    3. Update data\r
    4. Delete data\r
    5. Log out
              ''')
        menu = input("Enter the menu number you want to run: ")
        if menu.isdigit():
            menu=int(menu)
        if (menu==1):
            # READ MENU
            print('\n========== READ MENU ==========')
            while True:
                print('\nWhich data would you like to view?')
                print('''
    1. Customer data\r
    2. Product data\r
    3. Back
                      ''')
                opt = (input("Enter your choice: "))
                if opt.isdigit():
                    opt=int(opt)
                if (opt==1):
                    readMenu(True,'customer')
                    continue
                elif (opt==2):
                    readMenu(True,'product')
                    continue
                elif (opt==3):
                    break
                else:
                    print('Invalid input, please try again.\n')
                continue
            continue
        elif (menu==2):
            # CREATE MENU
            print('\n========== CREATE MENU ==========')
            while True:
                print('\nWhich data would you like to add?')
                print('''
    1. Customer data\r
    2. Product data\r
    3. Back
                      ''')
                opt = (input("Enter your choice: "))
                if opt.isdigit():
                    opt=int(opt)
                if (opt==1):
                    createMenu(True,'customer')
                    continue
                elif (opt==2):
                    createMenu(True,'product')
                    continue
                else:
                    print('Invalid input, please try again.\n')
                    break
            continue
        elif (menu==3):
            # UPDATE MENU
            print('\n========== UPDATE MENU ==========')
            while True:
                print('\nWhich data would you like to update?')
                print('''
    1. Customer data\r
    2. Product data\r
    3. Back
                      ''')
                opt = (input("Enter your choice: "))
                if opt.isdigit():
                    opt=int(opt)
                if (opt==1):
                    updateMenu('customer')
                    continue
                elif (opt==2):
                    updateMenu('product')
                    continue
                else:
                    print('Invalid input, please try again.\n')
                    break
            continue
        elif (menu==4):
            # DELETE MENU
            print('\n========== DELETE MENU ==========')
            while True:
                print('\nWhich data would you like to delete?')
                print('''
        1. Customer data\r
        2. Product data\r
        3. Back
                      ''')
                opt = (input("Enter your choice: "))
                opt=int(opt) if opt.isdigit() else opt
                if (opt==1):
                    deleteMenu('customer')
                    continue
                elif (opt==2):
                    deleteMenu('product')
                    continue
                elif (opt==3):
                    break
                else:
                    print('Invalid input, please try again.\n')
                    continue
            continue
        elif (menu==5):
            loggedIn=False
            isAdmin=False
            print('You are logged out of admin account.\n')
            break
        else:
            print('Invalid input, please try again.\n')
            continue

def menuCustomer():
    global loggedIn
    global isShopping
    name=customer[username]['name']
    while True:
        print('''\n----------------------------------------------------------------------------------
---------------------------- NewThreads Official Store ---------------------------
----------------------------------------------------------------------------------''')
        print(f'''Welcome back, {name}!\r
What would you like to do?\r
    1. View my data\r
    2. Go to shop\r
    3. View shopping cart\r
    4. Log out
              ''')
        menu = (input("Enter the menu number you want to run: "))
        menu=int(menu) if menu.isdigit() else menu
        if (menu==1):
            printOwnData(customer,username)
            print('\nWould you like to update your data? (y/n)')
            while True:
                option = input("Enter y/n: ")
                if (option=='y'):
                    while True:
                        print('''\nWhich attribute would you like to update?\r
                              1. Password\r
                              2. Name''')
                        att = (input("Enter your choice: "))
                        att=int(att) if att.isdigit() else att
                        if att==1 or att==2:
                            attribute='password' if att==1 else 'name'
                            msg=f'Enter the new {attribute}: '
                            att_val = input(msg)
                            updateCustomer(username,attribute,att_val)
                            printOwnData(customer,username)
                            print('Would you like to update your data again?')
                            break
                        else:
                            print('Invalid input, please try again.\n')

                    continue
                elif (option=='n'):
                    break
                else:
                    print('\nInvalid input, please try again.\n')
                    continue
            continue
        elif (menu==2):
            isShopping=True
            # shopping()
            shopping()
            continue
        elif (menu==3):
            menuCart()
            continue
        elif (menu==4):
            loggedIn=False
            print('You are logged out of your account.\n')
            break
        else:
            print('Invalid input, please try again.')
            continue

def menuCart():
    global total
    global cart
    global isBuying
    printCart()
    if cart:
        print('''\nWould you like to:\r
        1. Check out\r
        2. Clear shopping cart\r
        3. Exit
    ''')
        while True:
            cMenuInput=input('Enter your choice: ')
            cMenuInput=int(cMenuInput) if cMenuInput.isdigit() else cMenuInput
            if cMenuInput==1:
                checkOut()
                break
            elif cMenuInput==2:
                for item in cart:
                    idx=find_index(product,'prod_id',item[0])
                    product[idx]['stock']+=item[1]
                cart=[]
                total=0
                isBuying=False
                break
            elif cMenuInput==3:
                isBuying=False
                break
            else:
                print('Invalid input, please try again.\n')
                continue

def createMenu(admin,which):
    # which: customer or product
    if (admin==True):
        print(f'\n--- Create New {which.title()} ---')
        print(f'Please enter values for the new ', {which},':')
        if (which=='product'):
            while True:
                pName=(input('Product name                    :'))
                while True:
                    pCat=(input('Product category (Dresses/Tops) :'))
                    if pCat in ('Dresses','Tops'):
                        break
                    else:
                        print('Only "Dresses" and "Tops" categories are accepted. Please try again.\n')
                        continue
                pStock=(input('Product stock (numbers only)    :'))
                pPrice=(input('Product price (numbers only)    : Rp'))
                if pStock.isdigit() and pPrice.isdigit():
                    createProduct(pName,pCat,pStock,pPrice)
                    print('New product created.\n')
                    break
                else:
                    print('Invalid input, please try again.\n Tip: stock and price must contain only numbers.')
                    continue
        else:
            # CREATE CUSTOMER
            while True:
                cUname=(input('Customer username   :'))
                if cUname not in customer:
                    cPass=(input('Customer password   :'))
                    cName=(input('Customer name       :'))
                    createCustomer(cUname,cPass,cName)
                    print('New customer created.')
                    break
                else:
                    print('That username already exists, please choose another.')
                    continue  
    else:
        # Customer sign up
        print('\n---------------------------------- Sign Up Page ----------------------------------')
        while True:
            print('Please enter your data: ')
            cUname=(input('Your username   : '))
            if cUname not in customer:
                cPass=(input('Your password   : '))
                cName=(input('Your name       : '))
                createCustomer(cUname,cPass,cName)
                print('Your account has been created. Please login to continue.\n')
                break
            else:
                print('That username already exists, please choose another.\n')
                continue

             
def readMenu(admin,which):
    # admin: Boolean, isAdmin
    # which: int, 1 for customer, 2 for product
    global listProduct
    global isShopping
    global isBuying
    if admin==True:
        print(f'\n========== VIEW {which.upper()} DATA ==========')
    else:
        print('\n-------------------------- NewThreads Product Catalogue --------------------------')

    if (which=='product') and (admin==True):
        listProduct=product
        # READ PRODUCT MENU --ADMIN
        print('''
    1. View all products
    2. View by category
    3. View best-selling items
    4. View products with empty stock
    5. Sort products
    6. Back
              ''')
        while True:
            rMenuInput=(input('Enter your choice: '))
            rMenuInput=int(rMenuInput) if rMenuInput.isdigit() else rMenuInput
            if rMenuInput==1:
                printProduct(listProduct)
                break
            elif rMenuInput ==2:
                selection='category'
                filterProduct('category')
                break
            elif rMenuInput ==3:
                filterProduct('best')
                break
            elif rMenuInput ==4:
                filterProduct('empty')
                break
            elif rMenuInput==5:
                while True:
                    listProduct=product
                    print('''--------------------------------- Sort Products ----------------------------------\n
By what category would you like to sort the products?
    1. Items sold\r
    2. Price\r  
    3. Name\r
    4. Back
        ''')
                    sMenuInput=input('Enter your choice: ')
                    sMenuInput=int(sMenuInput) if sMenuInput.isdigit() else sMenuInput
                    if sMenuInput in (1,2,3):
                        if sMenuInput==1:
                            type='sold'
                        elif sMenuInput==2:
                            type='price'
                        elif sMenuInput==3:
                            type='name'
                        print(f'\n--- SORT BY {type.upper()} ---')
                        print('Would you like ascending or descending order?')
                        while True:
                            opt=input('Enter A for ascending or D for descending: ')
                            if opt.upper()=='A':
                                printProduct(sortProduct(type,'ASC'))
                                break
                            elif opt.upper()=='D':
                                printProduct(sortProduct(type,'DESC'))
                                break
                            else:
                                print('Invalid input, please input A or D.')
                                continue
                    elif sMenuInput==4:
                        break
                    else:
                        print('Invalid input, please try again.\n')
                        continue
                break
            elif rMenuInput==6:
                break
            else:
                print('Invalid input, please try again.\n')
                continue
    elif (which=='product') and (admin==False):
        # READ PRODUCT MENU --CUSTOMER
        # filter out products w/o stock
        listProduct=list(filter(lambda filProd: filProd['stock'] >0, product))
        print('''
    1. View all products
    2. View by category
    3. View best-selling items
    4. Sort products
    5. View shopping cart
    6. Back
              ''')
        while True:
            rMenuInput=(input('Enter your choice: '))
            rMenuInput=int(rMenuInput) if rMenuInput.isdigit() else rMenuInput
            if rMenuInput==1:
                printProduct(listProduct)
                isBuying=True
                break
            elif rMenuInput ==2:
                selection='category'
                filterProduct('category')
                isBuying=True
                break
            elif rMenuInput ==3:
                filterProduct('best')
                isBuying=True
                break
            elif rMenuInput==4:
                isBuying=True
                sort=True
                while sort:
                    print('''\n--------------------------------- Sort Products ----------------------------------\n
By what category would you like to sort the products?
        1. Items sold\r
        2. Price\r
        3. Name\r
        4. Back
        ''')
                    sMenuInput=input('Enter your choice: ')
                    sMenuInput=int(sMenuInput) if sMenuInput.isdigit() else sMenuInput
                    if sMenuInput in (1,2,3):
                        if sMenuInput==1:
                            type='sold'
                        elif sMenuInput==2:
                            type='price'
                        elif sMenuInput==3:
                            type='name'
                        print(f'\n--------------------------------- Sort by {type.title():<5} ----------------------------------')
                        print('Would you like ascending or descending order?')
                        while True:
                            opt=input('Enter A for ascending or D for descending: ')
                            if opt.upper()=='A':
                                listProduct=sortProduct(type,'ASC')
                                printProduct(listProduct)
                                sort=False
                                break
                            elif opt.upper()=='D':
                                listProduct=sortProduct(type,'DESC')
                                printProduct(listProduct)
                                sort=False
                                break
                            else:
                                print('Invalid input, please input A or D.')
                                continue
                    elif sMenuInput==4:
                        break
                    else:
                        print('Invalid input, please try again.\n')
                        continue
                break
            elif rMenuInput==5:
                menuCart()
                break
            elif rMenuInput==6:
                isShopping=False
                break
            else:
                print('Invalid input, please try again.\n')
                continue
    else:
        # READ CUSTOMER MENU
        print('''
    1. View all customers
    2. View one customer
    3. View customers filtered by join date
    4. View customers filtered by transactions
    5. Sort customers
    6. Back
        ''')
        while True:
            rMenuInput=(input('Enter your choice: '))
            rMenuInput=int(rMenuInput) if rMenuInput.isdigit() else rMenuInput
            if rMenuInput==1:
                printCustomer(customer)
                break
            elif rMenuInput==2:
                while True:
                    print('\nPlease enter username of the customer you would like to view:')
                    u_input=input('Username: (or Q to exit)')
                    if u_input not in customer:
                        print('Customer does not exist.\n')
                        break
                    elif u_input in ('Q','q'):
                        break
                    else:
                        printOwnData(customer,u_input)
                        break
                break
            elif rMenuInput in (3,4):
                selection='join' if rMenuInput==3 else 'trans'
                filterCustomer(selection)
                break
            elif rMenuInput==5:
                while True:
                    print('''--- SORT CUSTOMERS ---\n
By what category would you like to sort the customers?
    1. Name\r
    2. Join date\r
    3. Total purchase\r
    4. Number of transactions\r
    5. Back
        ''')
                    sMenuInput=input('Enter your choice: ')
                    sMenuInput=int(sMenuInput) if sMenuInput.isdigit() else sMenuInput
                    if sMenuInput in (1,2,3,4):
                        if sMenuInput==1:
                            type='name'
                        elif sMenuInput==2:
                            type='date_joined'
                        elif sMenuInput==3:
                            type='total purchase'
                        elif sMenuInput==4:
                            type='transaction count'
                        print(f'\n--- SORT BY {type.upper()} ---')
                        print('Would you like ascending or descending order?')
                        while True:
                            opt=input('Enter A for ascending or D for descending: ')
                            if opt.upper()=='A':
                                printCustomer(sortCustomer(type,'ASC'))
                                break
                            elif opt.upper()=='D':
                                printCustomer(sortCustomer(type,'DESC'))
                                break
                            else:
                                print('Invalid input, please input A or D.')
                                continue
                    elif sMenuInput==5:
                        break
                    else:
                        print('Invalid input, please try again.\n')
                        continue
                break
            elif rMenuInput==6:
                break
            else:
                print('Invalid input, please try again.\n')

def updateMenu(which):
    # which: customer or product
    update=True
    id='username' if which=='customer' else 'ID'
    print(f'\n========== UPDATE {which.upper()} DATA ==========')
    print(f'''Please enter the {id} of the {which} you would like to update.
                Enter Q if you would like to cancel.''')
    
    # Update product
    if (which=='product'):
        while update==True:
            pID=(input('Product ID: '))
            idx=find_index(product,'prod_id',pID)
            if idx!=-999: 
                pID=int(pID)
                printOneProduct(pID)
                print('''
                    \nWhich attribute would you like to change?\n
    1. Name
    2. Category
    3. Stock
    4. Price
    5. Cancel
                    ''')
                pAtt=(input("Enter your choice: "))
                pAtt=int(pAtt) if pAtt.isidigit() else pAtt
                while update:
                    if pAtt==1:
                        pKey='name'
                        pValue=input(f'\nEnter the new product {pKey}: ')
                        break
                    elif pAtt==2:
                        pKey='category'
                        pValue=input(f'\nEnter the new product {pKey}: ')
                        break
                    elif pAtt==3:
                        pKey='stock'
                        while True:
                            pValue=(input(f'\nEnter the new product {pKey}: '))
                            if pValue.isdigit():
                                break
                            else:
                                print('Invalid input. Please only enter numbers.\n')
                                continue
                        break
                    elif pAtt==4:
                        pKey='price'
                        while True:
                            pValue=(input(f'\nEnter the new product {pKey}: '))
                            if pValue.isdigit():
                                break
                            else:
                                print('Invalid input. Please only enter numbers.\n')
                                continue
                        break
                    elif pAtt==5:
                        update=False
                        break
                    else:
                        print('Invalid value, please enter again.\n')
                        continue
                updateProduct(pID,pKey,pValue)
                print('\nProduct has been updated to:')
                printOneProduct(pID)
                print('------------------------------------------------------------------------')
                break
            elif pID in ('Q','q'):
                update=False
                break
            elif pID.isdigit()==False:
                print('The ID you entered is not valid, please enter numbers only\n')
            else:
                print('Product ID not found.')
                break
    else:
        # UPDATE CUSTOMER
        while update==True:
            cID=(input('Customer username: '))
            if cID in customer: 
                printOneCustomer(cID)
                print('''
                    \nWhich attribute would you like to change?\n
    1. Name
    2. Password
    3. Cancel
                    ''')
                cAtt=input("Enter your choice:")
                if cAtt.isdigit:
                    cAtt=int(cAtt)
                while update:
                    if cAtt==1:
                        cKey='name'
                        cValue=input(f'\nEnter the new product {cKey}: ')
                        break
                    elif cAtt==2:
                        cKey='password'
                        cValue=input(f'\nEnter the new product {cKey}: ')
                        break
                    elif cAtt==3:
                        update=False
                        break
                    else:
                        print('Invalid value, please enter again.')
                        continue
                updateCustomer(cID,cKey,cValue)
                print('\nProduct has been updated to:')
                printOneCustomer(cID)
                print('------------------------------------------------------------------------')
                break
            elif cID in ('Q','q'):
                update=False
                break
            else:
                print('Customer username not found.')
                break 

def deleteMenu(which):
    # which: customer or product
    delete=True
    idx='username' if which=='customer' else 'ID'
    print(f'\n========== DELETE {which.upper()} DATA ==========')
    print(f'''Please enter the {idx} of the {which} you would like to delete.
                Enter Q if you would like to cancel.''')
    while True:
        id=input(f'Enter {idx}: ')
        if id in ('Q','q'):
            delete=False
            break
        else:
            if which=='product':
                if id.isdigit():
                    # check if product exists
                    id=int(id)
                    if find_index(product,'prod_id',id)!=-999:
                        break
                    else:
                        print('Product not found.\n')
                        delete=False
                        break
                else:
                    print('Invalid input, please enter only numbers.\n')
                    continue
            elif which=='customer':
                # check if customer exists
                if id in customer:
                    break
                else:
                    print('Customer not found.\n')
                    delete=False
                    break
            
    while delete:
        delete=deleteWarn(which,id)
        if delete:
            deleteOne(which,id)
            print(f'{which} has been deleted.\n')
            delete=False
        else:
            break

## FUNCTIONS FOR SHOPPING
def shopping():
    global isBuying
    global listProduct
    while isShopping:
        readMenu(False,'product')
        while isBuying==True :
            print('\n Enter the index of the product you would like to buy, or enter Q if you would like to go back.')
            shopMenuInput=input('Index (or Q to cancel): ')
            if shopMenuInput in ('Q','q'):
                isBuying=False
                break
            elif int(shopMenuInput)<=(len(listProduct)):
                idx=int(shopMenuInput)-1
                # input not out of bond
                while True:
                    # check amount
                    buyAmt=(input('Enter the amount you want to buy: '))
                    if buyAmt.isdigit():
                        buyAmt=int(buyAmt)
                        if buyAmt<=0:
                            print('Purchase cancelled.\n')
                            break
                        elif buyAmt>listProduct[idx]['stock']:
                            print('Not enough stock, ',listProduct[idx]['name'],' stock: ',listProduct[idx]['stock'],' left')
                            continue
                        else:
                            # print(idx)
                            # print(listProduct[idx]['name'])
                            addToCart(listProduct[idx]['prod_id'],buyAmt)
                            buyAmt=0
                            idx=0
                            menuCart()
                            break
                    else:
                        print('Invalid input, please enter only numbers.\n')
            else:
                print('Invalid input, please try again.\n')
                continue

def checkOut():
    global total
    global cart
    global isBuying
    print('Would you like to check out and continue to payment?')
    while True:
        coInput=input('Enter y/n: ')
        if coInput in ('N','n'):
            isBuying=False
            break
        elif coInput in('Y'',y'):
            print('\n----------------------------------- Check Out ------------------------------------\n')
            while True:
                pay= (input('Enter the amount of money (numbers only): Rp '))
                if pay.isdigit():
                    pay=int(pay)
                    if (pay<total):
                        print(f'Your payment is insufficient, your total is Rp {total}.')
                        continue
                    else:
                        break
                else:
                    print('Your input is invalid. Please enter only the number of your money.\n')
                    continue
            for items in cart:
                updateProductBuy(items[0],items[1],'paid')
            customer[username]['transactions'].append(total)
            cart=[]
            isBuying=False
            print('\nPurchase Completed')
            if (pay==total):
                print("\nThank you for your purchase.")
            else:
                print("\nThank you for your purchase.")
                print(f'Your change is : Rp {pay-total}')
            break
        else:
            print('Invalid input, please try again.')
            continue

def addToCart(p_id,amt):
    global total
    exist=False
    idx=find_index(product,'prod_id',p_id)
    price=product[idx]['price']
    if cart:
        for item in cart:
            if item[0]==p_id:
                exist=True
                break
        if exist:
            item[1]+=amt
            item[2]+=(price*amt)
        else:
            cart.append([p_id,amt,(price*amt)])
    else:
        cart.append([p_id,amt,(price*amt)])
    total+=price*amt
    updateProductBuy(idx,amt,'cart')
    
# CREATE FUNCTIONS
def createCustomer(uname,pw,name):
    customer[uname]={
        'password':pw, 
        'name':name, 
        'date_joined':datetime.now().strftime('%Y-%m-%d'),
        'transactions':[]}

def createProduct(name,cat,stock,price):
    lastIdx=product[len(product)-1]['prod_id']
    product.append({'prod_id':lastIdx+1,
                    'name':name,
                    'category':cat,
                    'stock':stock,
                    'sold':0,
                    'price':price
                    })


# def createTransaction(u_name,total):
#     customer[u_name]['transactions'].append(total)

# READ FUNCTIONS
## CUSTOMER -- CUSTOMER ACCESS
def printOwnData(dict1,uname):
    fDate=datetime.strptime(dict1[uname]['date_joined'], '%Y-%m-%d').strftime('%d-%m-%Y')
    print('\nUsername\t: ',uname)
    print('Password\t: ',dict1[uname]['password'])
    print('Name\t\t: ',dict1[uname]['name'])
    print(f'Date joined\t: {fDate:<14}')
    if not dict1[uname]['transactions']:
        print('Transactions\t: ')
        print('-')
    else:
        print('Transactions\t: ')
        i=1
        for items in dict1[uname]['transactions']:
            print(f'{i}. Total: {items}')
            i+=1

## CUSTOMER -- ADMIN ACCESS
def printCustomer(dict1):
    if (dict1):
        head=['Index','Username','Password','Name','Date Joined','Transactions']
        i=0
        customerList = (
            f"\n {head[0]:<5} | "
            f"{head[1]:<15} | "
            f"{head[2]:<15} | "
            f"{head[3]:<25} | "
            f"{head[4]:<14} | "
            f"{head[5]}\n "
        )
        for key in dict1:
            customerList += (
                f"{i:<5} | "
                f"{key:<15} | "
                f"{dict1[key]['password']:<15} | "
                f"{dict1[key]['name']:<25} | "
                f"{datetime.strptime(dict1[key]['date_joined'], '%Y-%m-%d').strftime('%d-%m-%Y'):<14} | "
                f"{dict1[key]['transactions']}\n "
            )
            i+=1
        print(customerList)
    else:
        print('Data empty.')

def printOneCustomer(cID):
    printCustomer({cID:customer[cID]})

## PRODUCT
def printProduct(list1):
    head=['Index','ID','Category','Name','Stock','Sold','Price']
    productlist= (f"\n {head[0]:<5} | ") if isAdmin==False else (f" {head[1]:<3} | ")
    if (list1):
        i=0
        productlist += (
            f"{head[2]:<10} | "
            f"{head[3]:<30} | "
            f"{head[4]:<5} | "
            f"{head[5]:<5} | "
            f"{head[6]:<10}\n "
        )
        for items in list1:
            productlist += (f"{i+1:<5} | ") if isAdmin==False else (f"{items['prod_id']:<3} | ")
            productlist += (
                f"{items['category']:<10} | "
                f"{items['name']:<30} | "
                f"{items['stock']:<5} | "
                f"{items['sold']:<5} | "
                f"{items['price']:<10}\n "
            )
            i+=1
        print(productlist)
        print(i,' product(s) displayed')
    else:
        print('Data is empty.')

def printOneProduct(pID):
    printProduct([product[find_index(product,'prod_id',pID)]])
    
# # FILTER FUNCTIONS
# # # Filter product
def filterProduct(selection):
    global listProduct
    if selection=='category':
        while True:
            print('\nWhich category would you like to view?')
            print('''
    1. Dresses
    2. Tops
    3. Back
                  ''')
            in_cat=(input('Enter your choice: '))
            if in_cat.isdigit():
                in_cat=int(in_cat)
            if in_cat==1:
                listProduct=list(filter(lambda filProd: filProd['category'] == 'Dresses', listProduct))
                printProduct(listProduct)
                break
            elif in_cat==2:
                listProduct=list(filter(lambda filProd: filProd['category'] == 'Tops', listProduct))
                printProduct(listProduct)
                break
            elif in_cat==3:
                break
            else:
                print('Invalid input, please try again.')
                continue
    elif selection=='best':
        tot=0
        for item in product:
            if item['stock']>0:
                tot+=item['sold']
        avg=tot//len(product)
        listProduct=list(filter(lambda filProd: filProd['sold'] >= avg, listProduct))
        printProduct(listProduct)
    elif selection=='empty':
        listProduct=list(filter(lambda filProd: filProd['stock'] == 0, listProduct))
        printProduct(listProduct)
    # listProduct=filProd

def filterCustomer(selection):
    filCust={}
    if selection=='join':
        while True:
            print('\n-- Filter by join date --\n')
            print('''
                  Please enter the start and end date you would like to select.\n
                  FORMAT: DD-MM-YYYY, enter Q in either field to cancel.
                  ''')
            while True:
                start=input('Enter the start date (DD-MM-YYYY): ')
                end=input('Enter the end date (DD-MM-YYYY): ')
                # check validity
                if valiDate(start) and valiDate(end):
                    if start<end:
                        start=datetime.strptime(start, '%d-%m-%Y').strftime('%Y-%m-%d')
                        end=datetime.strptime(end, '%d-%m-%Y').strftime('%Y-%m-%d')
                        filCust={k: v for k, v in customer.items() if v['date_joined'] >= start and v['date_joined'] <= end }
                        printCustomer(filCust)
                        filCust={}
                        break
                    else:
                        print('Start date has to be before end date. Please try again.\n')
                elif start in ('Q','q') or end in ('Q','q'):
                    break
                else:
                    print('Invalid input. Please input date as DD-MM-YYYY.\n')
                    continue

            break
    else:
        # selection==trans, filter by transactions
        tot=0
        while True:
            print('\n-- Filter by transactions --')
            print('''
    View customers:
    1. With no transactions
    2. With total transactions >= average
    3. Back
                  ''')
            in_cat=(input('Enter your choice: '))
            if in_cat.isdigit():
                in_cat=int(in_cat)
            if in_cat==1:
                for k,v in customer.items():
                    if not (v['transactions']):
                        filCust[k]=v
                printCustomer(filCust)
                filCust={}
                break
            elif in_cat==2:
                for k,v in customer.items():
                    tot+=sum(v['transactions'])
                avg=tot//len(customer)
                for k,v in customer.items():
                    if (v['transactions']) and sum(v['transactions'])>avg:
                        filCust[k]=v
                printCustomer(filCust)
                filCust={}
                break
            elif in_cat==3:
                break
            else:
                print('Invalid input, please try again.')
                continue

# # SORT FUNCTIONS
def sortProduct(type,order):
    global listProduct
    rev=True if order=='DESC' else False
    sort=sorted(listProduct,key=lambda x: x[type],reverse=rev)
    return sort

def sortCustomer(type,order):
    rev=True if order=='DESC' else False
    if type=='total purchase':
        sort=sorted(customer.items(),key=lambda x:sum(x[1]['transactions']),reverse=rev)
    elif type=='transaction count':
        sort=sorted(customer.items(),key=lambda x:len(x[1]['transactions']),reverse=rev)
    else:
        sort=sorted(customer.items(),key=lambda x:x[1][type],reverse=rev)
    return OrderedDict(sort)

# # # CART

def printCart():
    global total
    print('\n--------------------------------- Shopping Cart ----------------------------------\n')
    if (cart):
        i=1
        header=['No','Category','Name','Amount','Price','Total']
        productList = (
                f" {header[0]:<3} | "
                f"{header[1]:<10} | "
                f"{header[2]:<25} | "
                f"{header[3]:<8} | "
                f"{header[4]:<10} | "
                f"{header[5]:<10}\n "
            )
        for items in cart:
            idx=find_index(product,'prod_id',items[0])
            productList += (
                # f"{product[idx]['prod_id']:<3} | "
                f"{i:<3} | "
                f"{product[idx]['category']:<10} | "
                f"{product[idx]['name']:<25} | "
                f"{items[1]:<7}x | "
                f"{product[idx]['price']:<10} | "
                f"{items[2]:<10}\n "
            )
            i+=1
        print(productList)
        print('Total purchase = Rp ',total)

    else:
        print('Cart is empty.')

# [
#     [prod_id,amt, totalprice],
#     [5, 10, price5*10],
#     [1, 1, price1]
# ]
        



# UPDATE FUNCTIONS
## UPDATE CUSTOMER
def updateCustomer(uname,attribute,value):
    customer[uname][attribute]=value

## UPDATE PRODUCT
def updateProduct(idx,attribute,value):
    product[idx][attribute]=value

def updateProductBuy(idx,amt,type):
    if (type=='cart'):
        product[idx]['stock']-=amt
    elif (type=='paid'):
        product[idx]['sold']+=amt


# DELETE FUNCTIONS
## DELETE CUSTOMER
def deleteOne(which,id):
    if which=='product':
        del product[find_index(product,'prod_id',id)] 
    else:
        del customer[id]

## DELETE WARNING
def deleteWarn(type,id):
    print(f'''==== WARNING! ====\n
Are you sure you would like to delete this {type}? This data will be deleted permanently.
          ''')
    printOneCustomer(id) if type=='customer' else printOneProduct(id)
    while True:
        delOpt=input(f'Delete this {type} (y/n)? ')
        if delOpt in ('y','Y'):
            delete=True
            break
        elif delOpt in ('n','N'):
            delete=False
            break
        else:
            print('Invalid input, please try again.\n')
            continue
    return delete


#  MAIN PROGRAM

# Login
while True:
    print('\n----------------------------- Welcome to NewThreads ------------------------------')
    print('''
    What would you like to do?\r
    1. Log in\r
    2. New customer? Sign up here\r
    3. Exit
          ''')
    menu = (input("Enter the menu number you want to run: "))
    if menu.isdigit():
        menu=int(menu)
    if menu==1:
        # login
        print('''\n------------------------------------- Login --------------------------------------
(enter Q in both fields to cancel)\n''')
        while True:
            username = input("Enter your username: ")
            pw = input("Enter your password: ")
            if username == 'admin'and pw=='admin':
                loggedIn=True
                isAdmin=True
                break
            elif username in customer:
                # customer exist, check
                if (customer[username]['password']==pw):
                    loggedIn=True
                    isAdmin=False
                    break
                else:
                    print('Wrong password, please try again!\n')
                    continue
            elif (username in ('Q','q')) and (pw in ('Q','q')):
                loggedIn=False
                break
            else:
                print('Username does not exist, please try again!\n')
                continue
        
        if (isAdmin) and (loggedIn):
            menuAdmin()
        elif (loggedIn):
            menuCustomer()
            break
    elif menu==2:
        # Create customer
        createMenu(False,'customer')
        continue
    elif menu==3:
        break
    else:
        print('Invalid input, please try again.\n')
        continue
