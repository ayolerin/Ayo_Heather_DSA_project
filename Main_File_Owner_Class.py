# author heather
# we are importing from different files
from Caps_Clothes_Class import *
from CropTop_Clothes_Class import *
from Hoody_Clothes_Class import *

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

    def inside_add(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected add a clothes\n")
        file.close()

    def inside_remove(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected remove a clothes\n")
        file.close()

    def menu_owner(self):
        print("Enter 1 to add a new item to the list\n"
              "Enter 2 to remove a product to the list\n"
              "Enter 3 to view all products\n")

    def Caps_add(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected to add a cap\n")
        file.close()

    def CropTop_add(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected to add a Crop top\n")
        file.close()

    def Hoody_add(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected to add a hoody\n")
        file.close()
    # this is the add a clothes function
    def add(self, clothes_list, new_owner):
        clothes_type = int(input("Enter 1 to add a cap\n"
                                "Enter 2 to add a crop top \n"
                                "Enter 3 to add a hoody"))
        if clothes_type == 1:
                color = input("What color is it")
                size = input("What is the size")
                price= int(input("What is the price "))
                new_clothes = Caps_Clothes("Cap ", color, size, price)
                print('Your new cap  is: ')
                new_clothes.__str__()
                clothes_list.append(new_clothes)
        if clothes_type == 2:
                color = input("What color is it")
                size = input("What is the size")
                price = int(input("What is the price "))
                new_clothes = CropTop_Clothes("Crop Top",color, size, price)
                print('Your new crop top clothes is: ')
                new_clothes.__str__()
                clothes_list.append(new_clothes)
        if clothes_type == 3:
                color = input("What color is it")
                size = input("What is the size")
                price = int(input("What is the price "))
                new_clothes = Hoody_Clothes("Hoody", color, size, price)
                print('Your new hoody clothes is: ')
                new_clothes.__str__()
                clothes_list.append(new_clothes)

    def clothes_remove(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has removed a clothes\n")
        file.close()

    # this is the remove a clothes function
    def remove(self, clothes_list, new_owner):
        new_owner.view(clothes_list)
        for Caps_Clothes in clothes_list:
            print("Clothe type: " + Caps_Clothes.Clothes_type + ". Clothe color:" + Caps_Clothes.color)
    #         continue
    #     else:
    #         print(x.Clothes_type + ' has been removed from your clothes list')
    #         break

    # a = int(input("Enter 1, to remove a cap\n"
        #               "Enter 2, to remove a hoody\n"
        #               "Enter 3, to remove a crop top"))
        #
        # if a == 1:
        #     print("Available clothes are: ")
        #     for x in clothes_list:
        #         print("Clothe type: " + x.Clothes_type + ". Clothe color:" + x.color)
        # for x in Clothes_list:
        #     # print("Clothe type: " + x.Clothes_type + ". Clothe color:" + x.color)
        #     while True:
        #         try:
        #             ask = input("What brand of clothes do you want to remove from the list? ").upper()
        #
        #             break
        #         except ValueError:
        #             print("This is an invalid input ,Try again")
        # new_owner.inside_remove()
        # for x in Clothes_list:
        #     print("Clothe type: " + x.Clothes_type + ". Clothe color:" + x.color)
        #     new_owner.clothes_remove()
        #     if x.Clothes_type != ask:
        #         continue
        #     else:
        #         print(x.Clothes_type + ' has been removed from your clothes list')
        #         break



    def view(self, Clothes_list):
        Owner.inside_view(self)
        print("Available clothes are: ")
        for x in Clothes_list:
            print("Clothe type: " + x.Clothes_type + ". Clothe color:" + x.color)

    def inside_view(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected view \n")
        file.close()