# author heather
# we are importing from different files
from Caps_Clothes_Class import *
from CropTop_Clothes_Class import *
from Hoody_Clothes_Class import *


di = {  "Caps": {"SMALL": ("pink", "$5"), "MEDIUM": ("white", "$5"), "LARGE": ("black", "$5")},
        "CropTop": {"SMALL": ("white", "$5"), "MEDIUM": ("red", "$10"), "LARGE": ("black", "$5")},
        "Hoody": {"SMALL": ("yellow", "$15"), "MEDIUM": ("black", "$30"), "LARGE": ("white", "$20")}}

# this is the function to get some basic information about the owner
class Owner:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    # this is the function for printing the details of the owner
    def __str__(self):
        print('\nYour first name is :', self.first_name,
              "\nYour last name is: ", self.last_name,
              "\nYour password is :" + self.password)

    def login(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has started as an owner\n")
        file.close()


    def menu_owner(self):
        print("Enter 1 to add a new item to the list\n"
              "Enter 2 to remove a product to the list\n"
              "Enter 3 to view all products\n")


    # this is the add a clothes function
    def add(self, di):
        clothes_type = int(input("Enter 1 to add a cap\n"
                                "Enter 2 to add a crop top \n"
                                "Enter 3 to add a hoody"))
        if clothes_type == 1:
            print(di["Caps"])
            print("Add a product which the size doesn't exist, we can only have one of each size ")
            size = input("What is the size e.g(small)").upper()
            color = input("What color is it")
            price = input("What is the price ")
            di['Caps'][size] = (color, '$' + price)
            print("You have added a new cap. The details\n"
                    "Cap Size: "+ size, " Cap Color: " + color, " Cap Price:$" + price)

        if clothes_type == 2:
            print(di["CropTop"])
            print("Add a product which the size doesn't exist, we can only have one of each size ")
            size = input("What is the size e.g(small)").upper()
            color = input("What color is it")
            price = input("What is the price ")
            di['CropTop'][size] = (color, '$' + price)
            print("You have added a new croptop. The details\n"
                    "CropTop Size: "+ size, " CropTop: " + color, " CropTop:$" + price)

        if clothes_type == 3:
            print(di["Hoody"])
            print("Add a product which the size doesn't exist, we can only have one of each size ")
            size = input("What is the size e.g(small)").upper()
            color = input("What color is it e.g(red)")
            price = input("What is the price e.g(5)")
            di['Hoody'][size] = (color, '$' + price)
            print("You have added a new hoody. The details\n"
                    "Hoody Size: "+ size, " Hoody Color: " + color, " Hoody Price:$" + price)
    #

    # this is the remove a clothes function
    def remove(self, di):
        clothes_type = int(input("Enter 1 to delete a cap\n"
                                 "Enter 2 to delete a crop top \n"
                                 "Enter 3 to delete a hoody"))
        if clothes_type == 1:
            print(di["Caps"])
            print("Remove a product which the size exist above.")
            size = input("What is the size e.g(small)").upper()
            del di["Caps"][size]
            print(di["Caps"])
            print("You have deleted the " , size, " cap")

        if clothes_type == 2:
            print(di["CropTop"])
            print("Remove a product which the size exist above.")
            size = input("What is the size e.g(small)").upper()
            del di["CropTop"][size]
            print("You have deleted the " , size, " crop top")

        if clothes_type == 2:
            print(di["Hoody"])
            print("Remove a product which the size exist above.")
            size = input("What is the size e.g(small)").upper()
            del di["Hoody"][size]
            print("You have deleted the ", size, " hoody")


    def view(self,di):
        print("Available clothes are: ")
        for key, value in di.items():
            print(key, ' : ', value)
