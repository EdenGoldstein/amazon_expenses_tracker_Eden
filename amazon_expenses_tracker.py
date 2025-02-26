import re
import time
from datetime import datetime

def password_validation(password):
    '''
    the function get a name and a password and check if the password is valid
    get phone number and and chech the valid 
    '''
    l, u, s , d = 0, 0, 0, 0
    
    password = password.strip()
    if len(password) > 6 and len(password) < 20:
        for char in password:
            if char.islower():
                l+=1
            if char.isupper():
                u+=1
            if char.isdigit():
                d+=1
            if char == '!' or char == '@' or char == '%' or char == '#' or char == '$' or char == '^' or char == '&':
                s+=1
                
        if l >= 1 and u >= 1 and s >= 1 and d >= 1:
            return 'valid'
            
        else:
            return 'invalid'
    
    
def login(user_name, password):

    login_name = input('enter your user name: ')

    login_password = input('enter your password: ')
    if user_name == login_name and password == login_password:
        return True
    else:
        return False
    
    
def phone_validation(phone_number):
    pattern = r'\+49([0-9]{10})'
    result = re.fullmatch(pattern, phone_number)
    if result is None:
        return None
    else:
        return 'valid phone'
    
def change_phone_number(phone_number):
    fixed_phone_number = re.sub('[0-9]{10}', '49***', phone_number)
    return fixed_phone_number
    
    
def change_date():
    now = datetime.now()
    current_date = now.strftime('%d/%m/%Y')
    return current_date
     

def calculate_delivery_cost(users_items_info):
    total_delivery_cost = 0
    for item in users_items_info[user_name]:
        
        quantity = item['quantity']
        quantity = float(quantity)
        weight = item['item_weight']
        weight = float(weight)*quantity
        total_delivery_cost += weight
        
    return total_delivery_cost


def calculate_items_cost(users_items_info):
    total_items_cost = 0
    for item in users_items_info[user_name]:
        
        quantity = item['quantity']
        quantity = int(quantity)
        cost = item['item_cost']
        cost = int(cost)*quantity
        total_items_cost += cost
        
    return total_items_cost


def most_expensive(users_items_info):
    
    highest_price = 0
    for item in users_items_info[user_name]:
        
        price = item['item_cost']
        price = int(price)
        if price > highest_price:
            highest_price = price
    highest_price = int(highest_price)
            
    return highest_price


def item_name_highest_price(users_items_info, highest_price):
    
    name = None
    for item in users_items_info[user_name]:
        
        price = item['item_cost']
        price = int(price)
        
        if price == highest_price:
            name = item['purchased_item']
            break
        else:
            continue
            
    return name



def least_expensive(users_items_info):
    lowest_price = 500
    for item in users_items_info[user_name]:
        
        price = item['item_cost']
        price = int(price)
        if price < lowest_price:
            lowest_price = price
    lowest_price = int(lowest_price)
        
    return lowest_price


def item_name_lowest_price(users_items_info, lowest_price):
    
    name = None
    for item in users_items_info[user_name]:
        
        price = item['item_cost']
        price = int(price)
        
        if price == lowest_price:
            name = item['purchased_item']
            break
        else:
            continue
            
    return name

def calculate_average_cost(users_items_info):
    
    total_price = 0
    total_items = 0 

    for item in users_items_info[user_name]:
        
        quantity = item['quantity']
        quantity = int(quantity)
        cost = item['item_cost']
        cost = int(cost)*quantity
        total_price += cost

        total_items += quantity
    average_cost = int(total_price/total_items)
    
    return average_cost

def calculate_limit(users_items_info):
    
    total_price = 0

    for item in users_items_info[user_name]:
        
        cost = item['item_cost']
        cost = int(cost)
        total_price += cost
        
    total_price = int(total_price)
    if total_price >= 500:
        return True
    else:
        return False
    
    
    
    
     
     
user_name =input('enter user name: ')
password = input('enter a password\n(6-20 char long, include at least one uppercase char, lowercase char, number and special symbol): ')
password_check = (password_validation(password))
print(password_check)

enter_attempt = 0
if password_check == 'invalid':
    print('invalid password , please enter a password again')
    exit()
else:
    print('You are registered')
    login_check = False
    while enter_attempt < 2 and login_check != True:
        login_check = login(user_name, password)
        if login_check == True:
            print('\nRegistration successful!\n','--------------------\n|Welcome to Amazon!|\n--------------------\n')
        else: 
            print('your user name/password you entered is not correct, try again in 5 seconds')
            enter_attempt += 1
            time.sleep(5)
            
    if enter_attempt > 2:
        print('please register again')
        exit()
        
phone_number = input('please enter a phone number to continue ')
phone_check = phone_validation(phone_number)

while phone_check is None:
    phone_number = input('Enter phone number again ')
    phone_check = phone_validation(phone_number)
    

print(f'\nHello, {user_name}!, Welcome to the Amazon Expense Tracker!\nWhat would you like to do?')
print('1.Enter a purchase\n2.Generate a report\n3.Quit')
choice = -1

item_info= {'purchased_item': None ,'purchase_date': None , 'item_cost': None, 'item_weight': None,'quantity': None}
all_items_info = []
users_items_info = {}

while choice != 3:
    choice = input('\nEnter your choice (1/2/3): ')
    choice = int(choice)
    if choice == 1:
        
    
    
        purchased_item_value= str(input('Enter the item purchased(string min 3 char): '))
        while len(purchased_item_value) < 3:
            purchased_item_value= str(input('Enter again the item purchased(string min 3 char): '))
        item_info.update(purchased_item = purchased_item_value)
       
       
        while True:
            purchase_date_value= input('Enter the date of the purchase (MM/DD/YYYY or MM-DD-YYYY): ')
            try:
                purchase_date_value = datetime.strptime(purchase_date_value, '%m/%d/%Y')
            except:
                try:
                    purchase_date_value = datetime.strptime(purchase_date_value, '%m-%d-%Y')
                except:
                    continue
            break

        purchase_date_value = purchase_date_value.strftime('%m/%d/%Y')
        item_info.update(purchase_date = purchase_date_value)
        
        item_cost_value = input('Enter the total cost of the item in Euro: ') 
        while item_cost_value.isdigit() == False:
            item_cost_value = input('Enter again the total cost of the item in Euro(only numbers): ')
        item_info.update(item_cost = item_cost_value)
        
 
        
        item_weight_value = input('Enter the weight of the item in kg:(example- 3.2) ')
        pattern = r'\d+\.\d+'
        item_weight_check = re.fullmatch(pattern, item_weight_value)


        while item_weight_check == None:
            item_weight_value = input('Enter the weight again:(example- 3.0) ')
            item_weight_check = re.fullmatch(pattern, item_weight_value)    

        item_info.update(item_weight = item_weight_value)
        
        while True:
            try:
                quantity_value = input('Enter the quantity purchased: ')
                quantity_value = int(quantity_value)
            except:
                continue
            break
        
        item_info.update(quantity = quantity_value)
        
        all_items_info.append(item_info.copy())
        
        users_items_info[user_name] = all_items_info
        
    
        
        
        print('\nWhat would you like to do?\n1.Enter a purchase\n2.Generate a report\n3.Quit')
        
    elif choice == 2:
        print('            --------------------------')
        print('            | Amazon Expense Report |')
        print('            --------------------------')
        
        print(f'name: {user_name}   ')
        print('password: ***   ')
        fixed_phone_number = change_phone_number(phone_number)
        print(f'Tel: {fixed_phone_number}   ')
        current_date = change_date()
        print(f'Date: {current_date}')
        print('\n---------------------------------\n')
        
        delivery_cost = calculate_delivery_cost(users_items_info)
        
        items_cost = calculate_items_cost(users_items_info) - delivery_cost
        
        print('DELIVERY CHARGES:\n')
        print(f'{delivery_cost} EURO\n')
        
        print('TOTAL ITEM COST:\n')
        print(f'{items_cost} EURO\n')
    
    
        most_expensive_item = most_expensive(users_items_info)
        item_name_most_expensive = item_name_highest_price(users_items_info, most_expensive_item)
        least_expensive_item = least_expensive(users_items_info)
        item_name_least_expensive = item_name_lowest_price(users_items_info, least_expensive_item)
        
        print('MOST EXPENSIVE:\n')
        print(f'name: {item_name_most_expensive}\n')
        print(f'cost: {most_expensive_item} EURO\n')
        
        
        print('LEAST EXPENSIVE:\n')
        print(f'name: {item_name_least_expensive}\n')
        print(f'cost: {least_expensive_item} EURO\n')
        
    
        
        average_cost = calculate_average_cost(users_items_info)
        print(f'AVEGARE COST OF ITEM PER ORDER: {average_cost} EURO\n')
        
        limit_check = calculate_limit(users_items_info)
        if limit_check == True:
            print('NOTE: You have exceeded the spending limit of 500 EURO')
        else: 
            print('NOTE: You have not exceeded the spending limit of 500 EURO')
            
        
        print('\nWhat would you like to do?\n1.Enter a purchase\n2.Generate a report\n3.Quit')
         
    else:
        print('\nThe operation you entered is not valid .please choose option from here:\n1.Enter a purchase\n2.Generate a report\n3.Quit')
        
    
        
print(f'\nThank you for your visit, {user_name}. Goodbye!')
exit ()
    
    
    
    
