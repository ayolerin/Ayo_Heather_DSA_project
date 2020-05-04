# Ayo-fisher Oluwapamilerin
# this is where we are importing
from Main_File_Customer_Class import *
from Main_File_Owner_Class import *
from Caps_Clothes_Class import *
from CropTop_Clothes_Class import *
from Hoody_Clothes_Class import *


first_name = input("What is your first name? e.g(Heather) ")
last_name = input("What is your surname? e.g(Mataruse) ")
passport_number = int(input("What is your passport number? e.g(1233) "))
print("Your log in details are\n" +"First Name: " +first_name ," \n" + "Last Name: "+ last_name , "\n "
      + "Passport Number:" + str(passport_number))

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
    user_tuple = ()
    user_list = list(user_tuple)
    customer1 = Customer("Heather", "Mataruse", "1010")
    new_customer = Customer(first_name, last_name, passport_number)
    user_list.append(new_customer)
    new_customer.login()



if user_input == 2:
    user_tuple = ()
    user_list = list(user_tuple)
    owner1 = Owner("Heather", "Mataruse", "1010")
    new_owner = Owner(first_name, last_name, passport_number)
    user_list.append(new_owner)
    new_owner.login()

    # user_tuple= tuple(user_list)
    # print(user_tuple)

# this is where our while loop begins
answer = "yes"
while answer == "yes":
    if user_input == 1:
        # this is where we are calling our customer menu
        new_customer.menu_customer()
        while True:
            try:
                choice = int(input("Enter your choice: e.g(1) "))
                if choice >= 3:
                    print("This number is out of range")
                break
            except ValueError:
                print("This is an invalid input ,Try again")

        if choice == 1:
            new_customer.buy(di)

        if choice == 2:
            # this is where we are calling our crop top function
            new_customer.view(di)

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
            new_owner.add(di)
        if choice == 2:
            new_owner.remove(di)

        if choice == 3:
            # this is where we are calling our view clothes function
            new_owner.view(di)

            # this is the end of our while loop
        answer = input("Do you want to do anything else? Please enter yes or no:\n ").lower()
else:
    print("Thank you for using our But Comfortable Shopping app")