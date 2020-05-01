# Ayo-fisher Oluwapamilerin
# this is where we are importing
from Main_File_Customer_Class import *
from Main_File_Owner_Class import *
from Caps_Clothes_Class import *
from CropTop_Clothes_Class import *
from Hoody_Clothes_Class import *


# this is the clothes list
clothes_list = []
clothes1 = Caps_Clothes("Cap", "white", "$5", "medium")
clothes2 = Caps_Clothes("Cap", "pink", "$5", "small")
clothes3 = Caps_Clothes("Cap", "black", "$5", "large")
clothes4 = CropTop_Clothes("Crop Top", "red", "$10", "medium")
clothes5 = CropTop_Clothes("Crop Top", "white", "$5", "small")
clothes6 = CropTop_Clothes("Crop Top", "black", "$5", "large")
clothes7 = Hoody_Clothes("Hoody", "yellow", "$15", "small")
clothes8 = Hoody_Clothes("Hoody", "white", "$20", "large")
clothes9 = Hoody_Clothes("Hoody", "black", "$30", "medium")

clothes_list.append(clothes1)
clothes_list.append(clothes2)
clothes_list.append(clothes3)
clothes_list.append(clothes4)
clothes_list.append(clothes5)
clothes_list.append(clothes6)
clothes_list.append(clothes7)
clothes_list.append(clothes8)
clothes_list.append(clothes9)

first_name = input("What is your first name? ")
last_name = input("What is your surname? ")
passport_number = input("What is your passport number? ")
menu = print("Select 1 if you are a customer\n"
             "Select 2 if you are an owner\n")
while True:
    try:
        user_input = int(input("Enter your choice: e.g(1) "))

        if user_input >= 3:
            print('This is out of range')
        break
    except ValueError:
        print("This is an invalid input ,Try again")

if user_input == 1:
    customer1 = Customer("Heather", "Mataruse", "1010")
    new_customer = Customer(first_name, last_name, passport_number)
    new_customer.login()

if user_input == 2:
    owner1 = Owner("Heather", "Mataruse", "1010")
    new_owner = Owner(first_name, last_name, passport_number)
    new_owner.login()

# this is where our while loop begins
answer = "yes"
while answer == "yes":
    if user_input == 1:
        # this is where we are calling our customer menu
        new_customer.menu_customer()
        while True:
            try:
                choice = int(input("Enter your choice: e.g(1) "))
                if choice >= 5:
                    print("This number is out of range")
                break
            except ValueError:
                print("This is an invalid input ,Try again")

        if choice == 1:
            new_customer.buy_CropTop()

        if choice == 2:
            new_customer.buy_Hoody()

        if choice == 3:
            # this is where we are calling our buying a clothes function
            new_customer.buy_Cap()

        if choice == 4:
            # this is where we are calling our crop top function
            new_customer.view(clothes_list)

        answer = input("Do you want to do anything else? Please enter yes or no:\n ").lower()

    if user_input == 2:
        # this is where we are calling our owners menu
        new_owner.menu_owner()
        while True:
            try:
                choice = int(input("Enter your choice: e.g(1) "))
                if choice >= 4:
                    print("This is out of range")
                break
            except ValueError:
                print("This is an invalid input ,Try again")

        if choice == 1:
            # this is where we are calling our add a clothes function
            new_owner.add(clothes_list, new_owner)
        if choice == 2:

            new_owner.remove(clothes_list, new_owner)
        if choice == 3:
            # this is where we are calling our view clothes function
            new_owner.view(clothes_list)

            # this is the end of our while loop
        answer = input("Do you want to do anything else? Please enter yes or no:\n ").lower()
else:
    print("Thank you for using our But Comfortable Shopping app")