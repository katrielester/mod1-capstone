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
        raise ValueError('no dict with the key and value combination found')
    
# MENU FUNCTIONS
def menuAdmin():
    while True:
        print('\n--- NEWTHREADS ADMINISTRATOR MENU ---')
        print(''' 
    1. View data\r
    2. Add new data\r
    3. Update data\r
    4. Delete data\r
    5. Exit
              ''')
        menu = int(input("Enter the menu number you want to run: "))
        if (menu==1):
            # READ MENU
            while True:
                print('\nWhich data would you like to view?')
                print('''
        1. Customer data\r
        2. Product data\r
        3. Back
                      ''')
                opt = int(input("Enter your choice: "))
                if (opt==1):
                    readMenu(True,'customer')
                    continue
                elif (opt==2):
                    readMenu(True,'product')
                    continue
                else:
                    break
            continue
        elif (menu==2):
            # CREATE MENU
            while True:
                print('\nWhich data would you like to add?')
                print('''
        1. Customer data\r
        2. Product data\r
        3. Back
                      ''')
                opt = int(input("Enter your choice: "))
                if (opt==1):
                    createMenu('customer')
                    continue
                elif (opt==2):
                    createMenu('product')
                    continue
                else:
                    break
            continue
        elif (menu==3):
            # UPDATE MENU
            while True:
                print('\nWhich data would you like to update?')
                print('''
        1. Customer data\r
        2. Product data\r
        3. Back
                      ''')
                opt = int(input("Enter your choice: "))
                if (opt==1):
                    updateMenu('customer')
                    continue
                elif (opt==2):
                    updateMenu('product')
                    continue
                else:
                    break
            continue
            continue
        elif (menu==4):
            # DELETE MENU

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
        elif (menu==3):
            printCart()
            continue
        elif (menu==4):
            break

def createMenu(admin,which):
    # which: customer or product
    type='Customer' if which=='customer' else 'Product'
    if (admin==True):
        print('\n--- Create New ', type, ' ---')
        print('Please enter values for the new ', type.lower())
        if (which=='product'):
            
            pName=(input('Product name: '))
            pCat=(input('Product category: '))
            pStock=int(input('Product stock (numbers only): Rp'))
            pPrice=int(input('Product price (numbers only): Rp'))
            createProduct(pName,pCat,pStock,pPrice)
            print('New product created.')
        else:
            # CREATE CUSTOMER
            while True:
                print('Please enter your data: ')
                cUname=(input('Customer username: '))
                if cUname not in customer:
                    cPass=(input('Customer password: '))
                    cName=(input('Customer name: '))
                    createCustomer(cUname,cPass,cName)
                    print('New customer created.')
                    break
                else:
                    print('That username already exists, please choose another.')
                    continue  
    else:
        # Customer sign up
        print('\n--- Sign Up Page ---')
        while True:
            print('Please enter your data: ')
            cUname=(input('Your username: '))
            if cUname not in customer:
                cPass=(input('Your password: '))
                cName=(input('Your name: '))
                createCustomer(cUname,cPass,cName)
                print('Your account has been created. Please login to continue.\n')
                break
            else:
                print('That username already exists, please choose another.\n')
                continue

             
def readMenu(admin,which):
    # admin: Boolean, isAdmin
    # which: int, 1 for customer, 2 for product
    if admin==True:
        type='Customer' if which=='customer' else 'Product'
        print('\n',type,' data menu')
    else:
        print('\n--- NewThreads Product Catalogue ---')

    if (which=='product'):
        # READ PRODUCT MENU
        print('''
    1. View all products
    2. View by category
    3. View best-selling items
    4. View products with empty stock
    5. Back
              ''')
        while True:
            rMenuInput=int(input('Enter your choice: '))
            if rMenuInput==1:
                printProduct(product)
                break
            elif rMenuInput ==2:
                selection='category'
                filterProduct(selection)
                break
            elif rMenuInput ==3:
                selection='best'
                filterProduct(selection)
            elif rMenuInput ==4:
                selection='empty'
                filterProduct(selection)
            elif rMenuInput==5:
                break
    else:
        # READ CUSTOMER MENU
        print('''
    1. View all customers
    2. View customers filtered by join date
    3. View customers filtered by transactions
    4. View one customer
    5. Back
        ''')
        while True:
            rMenuInput=int(input('Enter your choice: '))
            if rMenuInput==1:
                printCustomer(customer)
                break
            elif rMenuInput in (2,3):
                selection='join' if rMenuInput==2 else 'trans'
                filterCustomer(selection)
                break
            elif rMenuInput==4:
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
            elif rMenuInput==5:
                break
            else:
                print('Invalid input, please try again.\n')

def updateMenu(which):
    # which: customer or product
    type='Customer' if which=='customer' else 'Product'
    print('\n--- Create New ', type, ' ---')
    print('Please enter values for the new ', type.lower())
    if (which=='product'):
        pName=(input('Product name: '))
        pCat=(input('Product category: '))
        pStock=int(input('Product stock (numbers only): Rp'))
        pPrice=int(input('Product price (numbers only): Rp'))
        createProduct(pName,pCat,pStock,pPrice)
        print('New product created.')
    else:
        # CREATE CUSTOMER
        while True:
            print('Please enter your data: ')
            cUname=(input('Customer username: '))
            if cUname not in customer:
                cPass=(input('Customer password: '))
                cName=(input('Customer name: '))
                createCustomer(cUname,cPass,cName)
                print('New customer created.')
                break
            else:
                print('That username already exists, please choose another.')
                continue  

def shopping():
    readMenu(False,'product')
    buy=True
    if filProd:
        productList=filProd
    else:
        productList=product
    while buy==True:
        print('\n Enter the index of the product you would like to buy, or enter "Q" if you would like to go back.')
        shopMenuInput=input('Index (or Q to cancel): ')
        if shopMenuInput in ('Q','q'):
            break
        elif int(shopMenuInput)<=(len(productList)):
            idx=int(shopMenuInput)
            # input not out of bond
            while True:
                # check amount
                buyAmt=int(input('Enter the amount you want to buy: '))
                if buyAmt>productList[idx-1]['stock']:
                    print('Not enough stock, ',productList[idx-1]['name'],' stock: ',productList[idx-1]['stock'],' left')
                    continue
                else:
                    addToCart(productList[idx-1]['prod_id'],buyAmt)
                    printCart()
                    buy=False
                    break
        else:
            print('Invalid input, please try again.')
            continue
 

def checkOut():
    print('Would you like to check out?')

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
    if (dict1):
        head=['Index','Username','Password','Name','Date Joined','Transactions']
        i=0
        customerList = (
            f" {head[0]:<8} | "
            f"{head[1]:<15} | "
            f"{head[2]:<15} | "
            f"{head[3]:<25} | "
            f"{head[4]:<14} | "
            f"{head[5]}\n "
        )
        for key in dict1:
            customerList += (
                f"{i:<8} | "
                f"{key:<15} | "
                f"{dict1[key]['password']:<15} | "
                f"{dict1[key]['name']:<25} | "
                f"{dict1[key]['date_joined']:<14} | "
                f"{dict1[key]['transactions']}\n "
            )
            i+=1
        print(customerList)
    else:
        print('Data empty.')

## PRODUCT
def printProduct(list1):
    if (list1):
        head=['Index','ID','Category','Name','Stock','Sold','Price']
        i=0
        productlist = (
            f" {head[0]:<8} | "
            # f"{head[1]:<3} | "
            f"{head[2]:<10} | "
            f"{head[3]:<25} | "
            f"{head[4]:<5} | "
            f"{head[5]:<5} | "
            f"{head[6]:<10}\n "
        )
        for items in list1:
            productlist += (
                f"{i+1:<8} | "
                # f"{items['prod_id']:<3} | "
                f"{items['category']:<10} | "
                f"{items['name']:<25} | "
                f"{items['stock']:<5} | "
                f"{items['sold']:<5} | "
                f"{items['price']:<10}\n "
            )
            i+=1
        print(productlist)
        print(i,' products displayed\n')
    else:
        print('Data is empty.')
        
# # FILTER
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
                filProd=list(filter(lambda filProd: filProd['category'] == 'Dresses', product))
                printProduct(filProd)
                break
            elif in_cat==2:
                filProd=list(filter(lambda filProd: filProd['category'] == 'Tops', product))
                printProduct(filProd)
                break
            elif in_cat==3:
                break
            else:
                print('Invalid input, please try again.')
                continue
    elif selection=='best':
        total=0
        for item in product:
            if item['stock']>0:
                total+=item['sold']
        avg=total//len(product)
        filProd=list(filter(lambda filProd: filProd['sold'] >= avg, product))
        printProduct(filProd)
    elif selection=='empty':
        filProd=list(filter(lambda filProd: filProd['stock'] == 0, product))
        printProduct(filProd)



def filterCustomer(selection):
    filCust={}
    if selection=='join':
        while True:
            print('\n-- Filter by join date --\n')
            print('''
                  Please enter the start and end date you would like to select.\n
                  FORMAT: DD-MM-YYYY
                  ''')
            start=input('Enter the start date (DD-MM-YYYY): ')
            end=input('Enter the end date (DD-MM-YYYY): ')
            # check validity?
            break
    else:
        # selection==trans, filter by transactions
        total=0
        while True:
            print('\n-- Filter by transactions --')
            print('''
    View customers:
    1. With no transactions
    2. With total transactions >= average
    3. Back
                  ''')
            in_cat=int(input('Enter your choice: '))
            if in_cat==1:
                for k,v in customer.items():
                    if not (v['transactions']):
                        filCust[k]=v
                printCustomer(filCust)
                break
            elif in_cat==2:
                for k,v in customer.items():
                    total+=sum(v['transactions'])
                avg=total//len(customer)
                for k,v in customer.items():
                    if (v['transactions']) and sum(v['transactions'])>avg:
                        filCust[k]=v
                printCustomer(filCust)
                break
            elif in_cat==3:
                break
            else:
                print('Invalid input, please try again.')
                continue

# # # CART

def printCart():
    print('\n--- Shopping Cart ---')
    if (cart):
        header=['Product ID','Category','Name','Amount','Price','Total']
        productList = (
                f" {header[0]:<8} | "
                f"{header[1]:<10} | "
                f"{header[2]:<25} | "
                f"{header[3]:<8} | "
                f"{header[4]:<10} | "
                f"{header[5]:<10}\n "
            )
        for items in cart:
            idx=find_index(product,'prod_id',items[0])
            i=0
            productList += (
                f"{product[idx]['prod_id']:<8} | "
                f"{product[idx]['category']:<10} | "
                f"{product[idx]['name']:<25} | "
                f"{items[1]:<7}x | "
                f"{product[idx]['price']:<10} | "
                f"{items[2]:<10}\n "
            )
            i+=1
        print(productList)

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
    elif (type=='cancel'):
        product[idx]['stock']+=amt
    elif (type=='paid'):
        product[idx]['sold']+=amt


## CUSTOMER ACCESS
### CART
def addToCart(p_id,amt):
    idx=find_index(product,'prod_id',p_id)
    price=product[idx]['price']
    cart.append([p_id,amt,(price*amt)])
    updateProductBuy(idx,amt,'cart')


#  MAIN

# Login
while True:
    print('--- Welcome to New Threads Store ---')
    print('''
        What would you like to do?\r
        1. Log in\r
        2. New customer? Sign up here\r
        3. Exit
          ''')
    menu = int(input("Enter the menu number you want to run: "))
    if menu==1:
        # login
        print('\n--- Log in ---')
        while True:
            username = input("Enter your username: ")
            pw = input("Enter your password: ")
            if username == 'admin'and pw=='admin':
                isAdmin=True
                break
            elif username in customer:
                # customer exist, check
                if (customer[username]['password']==pw):
                    isAdmin=False
                    break
                else:
                    print('Wrong password, please try again!\n')
                    continue
            else:
                print('Username does not exist, please try again!\n')
                continue
        
        if (isAdmin):
            menuAdmin()
        else:
            menuCustomer()
            break
    elif menu==2:
        # Create customer
        createMenu(False,'customer')
        continue
    elif menu==3:
        break
    else:
        print('Invalid input, please try again.')
        continue
    