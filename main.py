menu=[
    {'dishId':1,'name':'Burger','price':99,'isAvailabe':True}
]

customerIndex=0;
itemIndex=1
status=['canceled','received','preparing','ready for pickup','delivered']
def addProduct(name,price,bol):
    global itemIndex;
    itemIndex=itemIndex+1
    item={'dishId':itemIndex,'name':name,'price':price,'isAvailabe':bol}
    menu.append(item)
    return item

def removeProduct(id):
    fl=False;
    for i in menu:
        if i['dishId']==id :
            fl=True
            menu.remove(i);
            print('Item removed Successfully')
    if not fl:
        print('Item  not Found')
def changeAvailablity(id):
    fl=False;
    dish=None;
    for i in menu:
        if i['dishId']==id :
            fl=True
            i.update({'isAvailabe':not i.get('isAvailabe')})
            dish=i
    if fl:
        return dish
    else:
        print("Item Not Found")

    
orders=[];
def addOrder(name,dishId):
    dish={};
    global customerIndex;
    customerIndex=customerIndex+1
    for i in menu:
        if i['dishId']==dishId :
            dish=i;
            if not i.get('isAvailabe'):
                print("Sorry Product is not available")
                orders.append({'OrderId':customerIndex,'name':name,'dishName':i.get('name'),'Status':status[0],'Rating':None})
                return
            
            orders.append({'OrderId':customerIndex,'name':name,'dishName':i.get('name'),'Status':status[1],'Rating':None})
            print('Order is Successful')
            return ;
    print('No Item Found')
    return

def changeStatusForOrder(orderId,thisstatus):
    existingOrder={};
    index=None;
    for i in orders:
        if i.get('OrderId')==orderId:
            existingOrder=i
            index=orders.index(i)
            break;
    if existingOrder==None or existingOrder.get('Status')==status[0]:
        print('Order is not available or Already Cancelled')
    if thisstatus==4:
        rate=0;
        while True:
            try:
                rate=int(input("Please give Rating to us between 1 to 5   "))
                if rate >5 or rate<1:
                    print("Rating should be between 1 and 5")
                    continue
                break;
            except ValueError:
                print("Please Provide Valid Input ")
        existingOrder.update({'Rating':rate,'Status':status[4]})
        orders[index]=existingOrder
    existingOrder.update({'Status':status[thisstatus]})
    orders[index]=existingOrder
    return existingOrder;

def displayDish():
    for i in menu:
        print(i)  
def displayOrders():
    for i in orders:
        print(i)
        
                








while(True) :
    print('Select 1 to add new Dish \nSelect 2 to display Products\nSelect 3 to changeAvailablity of a Product \n Select 4 to remove product')
    print('Select 5 to take Order from Customer \n Select 6 to see all the orders \n Select 7 to change the status of a order')
    print('Select 8 to close Shop')
    choice =input('Enter your Choice= ')
    
    if not choice.isdigit:
        print('Please provide valid input')
    if choice=='1':
        
        name=None;
        price=None;
        bol=None;
        while True:
            name=input('Enter the name of the Dish= ')
            if not ((name.isalnum or name.isalpha) and len(name)>4):
                print('Please Provide Valid Name= ');
                continue
            price=input('Enter the Price of the Item')
            while True:
                if(not price.isnumeric):
                    print('Please Provide Valid Input');
                    continue
                else:
                    break
            price=int(price)
            bol=input('is It available type 1 for True 2 for False')
            
            while True:
                if not (bol.isnumeric and (bol=='1' or bol=='0') ):
                    print('Please Provide Valid Input');
                    continue
                else:
                    bol=bool(bol)
                    break
            print(addProduct(name,price,bol))
            break
    elif choice=='2':
        displayDish()
    elif choice=='3':
        dishid=None
        while True:
            dishid=input('Enter the dish Id to change Availability')
            if not dishid.isnumeric:
                continue
            else:
                dishid=int(dishid)
                break
        print(changeAvailablity(dishid))
    elif choice=='4':
        dishid=None
        while True:
            dishid=input('Enter the dish Id to change Availability ')
            if not dishid.isnumeric:
                continue
            else:
                dishid=int(dishid)
                break
        removeProduct(dishid)
    elif choice=='5':
        dishid=None
        name=input('Enter Your Name Of Customer')
        while True:
            dishid=input('Enter the dish Id to change Availability ')
            if not dishid.isnumeric:
                continue
            else:
                dishid=int(dishid)
                break
        addOrder(name,dishid)
    elif choice=='6':
        displayOrders();
    elif choice=='7':
        dishid=None
        changeSt=None;
        while True:
            dishid=input('Enter the dish Id to change Availability ')
            if not dishid.isnumeric:
                continue
            else:
                dishid=int(dishid)
                break
        while True:
            
            
            changeSt=input('1 for Cancel, 2 for received, 3 for preparing, 4 for ready for PickUp, 5 for Delivered')
            if not (changeSt.isnumeric and (int(changeSt)>=1 or int(changeSt)<=5)):
                continue
            else:
                changeSt=int(changeSt)
                break
        changeStatusForOrder(dishid,changeSt)
        break
    elif choice=='8':
        print('Thank You For using this Service')
        break;
    else:continue

        




# status=['canceled','received','preparing','ready for pickup','delivered']



    


