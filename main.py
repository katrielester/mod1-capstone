# Import datetime library
from datetime import datetime
datetime.now().strftime('%d-%m-%Y')

isAdmin=False
username=0   
filProd=[]
filCust={}

customer = {
    'user1': {
        'password':'abc123', 
        'name':'Obiwan', 
        'date_joined':'01-01-2021',
        'transactions':[100000,20000]},
    'user2': {
        'password':'abc123', 
        'name':'Leia', 
        'date_joined':'01-02-2020',
        'transactions':[400000]},
    'user3': { 
        'password':'abc123', 
        'name':'Anakin', 
        'date_joined':'27-09-2023',
        'transactions':[]},
    'user4': {
        'password':'abc123', 
        'name':'Padme',
        'date_joined':'27-09-2023',
        'transactions':[50000000,1000000]}
    }

product = [
    # Dresses
    {'prod_id':0,
     'name':'Mini Dress with Zip',
     'category':'Dresses',
     'stock':12345,
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
     'stock':1010,
     'sold':999,
     'price':1099000
     },
    #  Tops
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
     'sold':1500,
     'price':4999000
     }   
]

cart = []
# [
#     [5, 10],
#     [1, 1]
# ]

# UTIL
def find_index(dicts, key, value):
    class Null: pass
    for i, d in enumerate(dicts):
        if d.get(key, Null) == value:
            return i
    else:
        raise ValueError('no dict with the key and value combination found')
    
# MENU FUNCTIONS
def menuAdmin():
    while True:
        print('NEW THREADS ADMINISTRATOR MENU')
        print(''' 
    1. View data\r
    2. Add new data\r
    3. Update data\r
    4. Delete data\r
    5. Exit
              ''')
        menu = int(input("Enter the menu number you want to run: "))
        if (menu==1):
            print('\nWhich data would you like to view?')
            print('''
        1. Customer data\r
        2. Product data\r
        3. Back
                  ''')
            while True:
                opt = int(input("Enter your choice: "))
                if (opt==1):
                    readMenu(True,'Customer')
                    continue
                else:
                    isAdmin=False
                    break
            continue
        elif (menu==2):
            continue
        elif (menu==5):
            break

def menuCustomer():
    while True:
        print('\nWelcome to NewThreads!')
        print(''' 
    1. View my data\r
    2. Go to shop\r
    3. View shopping cart\r
    4. Exit
              ''')
        menu = int(input("Enter the menu number you want to run: "))
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
                        att = int(input("Enter your choice: "))
                        if att==1 or att==2:
                            attribute='password' if att==1 else 'name'
                            msg=f'Enter the new {attribute}: '
                            att_val = input(msg)
                            updateCustomer(username,attribute,att_val)
                            printOwnData(customer,username)
                            print('Would you like to update your data again?')
                            break
                        else:
                            print('Invalid input, please try again.')

                    continue
                elif (option=='n'):
                    break
                else:
                    print('\nInvalid input, please try again.')
                    continue
            continue
        elif (menu==2):
            shopping()
            continue
        elif (menu==4):
            break

def shopping():
    readMenu(False,'product')
    if filProd:
        productList=filProd
    else:
        productList=product
    while True:
        print('\n Enter the index of the product you would like to buy, or enter "Q" if you would like to go back.')
        shopMenuInput=input('Index (or Q to cancel): ')
        if shopMenuInput=='Q':
            break
        elif int(shopMenuInput)<=(len(productList)):
            idx=int(shopMenuInput)
            # input not out of bond
            while True:
                # check amount
                buyAmt=int(input('Enter the amount you want to buy: '))
                if buyAmt>productList[idx]['stock']:
                    print('Not enough stock, ',productList[idx]['name'],' stock: ',productList[idx]['stock'],' left')
                else:
                    addToCart(productList[idx]['prod_id'],buyAmt)
        else:
            print('Invalid input, please try again.')
            continue
        

# CREATE FUNCTIONS
def createCustomer(uname,pw,name):
    customer[uname]={
        'password':pw, 
        'name':name, 
        'date_joined':datetime.now().strftime('%d-%m-%Y'),
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


def createTransaction(u_name,total):
    customer[u_name]['transactions'].append(total)

# READ FUNCTIONS
## CUSTOMER -- CUSTOMER ACCESS
def printOwnData(dict1,uname):
    print('\nUsername\t: ',uname)
    print('Password\t: ',dict1[uname]['password'])
    print('Name\t\t: ',dict1[uname]['name'])
    print('Date joined\t: ',dict1[uname]['date_joined'])
    if not dict1[uname]['transactions']:
        print('Transactions\t: ')
        print('-')
    else:
        print('Transactions\t: ')
        i=1
        for items in dict1[uname]['transactions']:
            print(' ',i,'. Total: ',items)
            i+=1

## CUSTOMER -- ADMIN ACCESS
def printCustomer(dict1):
    head=['Index','Username','Password','Name','Date Joined','Transactions']
    i=0
    customerList = (
        f" {head[0]:<3} | "
        f"{head[1]:<15} | "
        f"{head[2]:<15} | "
        f"{head[3]:<25} | "
        f"{head[4]:<14} | "
        f"{head[5]}\n "
    )
    for key in dict1:
        customerList += (
            f"{i:<3} | "
            f"{key:<15} | "
            f"{dict1[key]['password']:<15} | "
            f"{dict1[key]['name']:<25} | "
            f"{dict1[key]['date_joined']:<14} | "
            f"{dict1[key]['transactions']}\n "
        )
        i+=1
    print(customerList)

## PRODUCT
def printProduct(s_type=0,s_opt=0):
    global filProd
    head=['Index','ID','Category','Name','Stock','Sold','Price']
    i=0
    productList = (
        f" {head[0]:<5} | "
        # f"{head[1]:<3} | "
        f"{head[2]:<10} | "
        f"{head[3]:<25} | "
        f"{head[4]:<5} | "
        f"{head[5]:<5} | "
        f"{head[6]:<10}\n "
    )
    if s_type==0:
        for items in product:
            productList += (
                f"{i+1:<5} | "
                # f" {items['prod_id']:<3} | "
                f"{items['category']:<10} | "
                f"{items['name']:<25} | "
                f"{items['stock']:<5} | "
                f"{items['sold']:<5} | "
                f"{items['price']:<10}\n "
            )
            i+=1
    elif s_type=='category':
        filProd=list(filter(lambda filProd: filProd['category'] == s_opt, product))
        for items in filProd:
            if items['category']==s_opt:
                productList += (
                    f" {i+1:<5} | "
                    # f"{items['prod_id']:<3} | "
                    f"{items['category']:<10} | "
                    f"{items['name']:<25} | "
                    f"{items['stock']:<5} | "
                    f"{items['sold']:<5} | "
                    f"{items['price']:<10}\n "
                )
                i+=1
            else:
                pass
    print(productList)
    print(i,' products displayed\n')
 
def readMenu(admin,which):
    # admin: Boolean, isAdmin
    # which: int, 1 for customer, 2 for product
    if admin==True:
        type='Customer' if which==1 else 'Product'
        print('\n',type,' data menu')
    else:
        print('--- NewThreads Product Catalogue ---')

    if (which=='product'):
        # READ PRODUCT MENU
        print('''
    1. View all products
    2. View by category
    3. View best-selling items
    4. Back
              ''')
        while True:
            rMenuInput=int(input('Enter your choice: '))
            if rMenuInput==1:
                printProduct()
                break
            elif rMenuInput in (2,3):
                selection='category' if rMenuInput==2 else 'best'
                filterProduct(selection)
                break
            elif rMenuInput==4:
                break
    else:
        # READ CUSTOMER MENU
        print('''
    1. View all customers
    2. View selected
        ''')

def filterProduct(selection):
    if selection=='category':
        while True:
            print('\nWhich category would you like to view?\n')
            print('''
    1. Dresses
    2. Tops
    3. Back
                  ''')
            in_cat=int(input('Enter your choice: '))
            if in_cat==1:
                printProduct(product,'category','Dresses')
            elif in_cat==2:
                printProduct(product,'category','Tops')
            elif in_cat==3:
                break
            else:
                print('Invalid input, please try again.')
                continue


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
    elif (type=='cancel'):
        product[idx]['stock']+=amt
    elif (type=='paid'):
        product[idx]['sold']+=amt


## CUSTOMER ACCESS
### CART
def addToCart(p_id,amt):
    cart.append([p_id,amt])
    idx=find_index(product,'prod_id',p_id)
    updateProductBuy(idx,amt,'cart')


#  MAIN

# Login
while True:
    print('Welcome to New Threads')
    print('''
        What would you like to do?\r
        1. Log in\r
        2. New customer? Sign up here\r
        3. Exit
          ''')
    menu = int(input("Enter the menu number you want to run: "))
    if menu==1:
        # login
        print('\nLog in')
        while True:
            username = input("Enter your username: ")
            pw = input("Enter your password: ")
            if username == 'admin':
                isAdmin=True
                break
            elif username in customer:
                # customer exist, check
                if (customer[username]['password']==pw):
                    isCustomer=True
                    break
                else:
                    print('Wrong password, please try again!')
                    break
            else:
                print('Username does not exist, please try again!')
                break
        
        if (isAdmin):
            menuAdmin()
        else:
            menuCustomer()
            break
    elif menu==2:
        # Create customer
        continue
    elif menu==3:
        break
    else:
        print('Invalid input, please try again.')
        continue
    