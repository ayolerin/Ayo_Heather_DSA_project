# author Heather Mataruse
#we are importing the plane class
from Clothes_Class import *

#this is the Caps Clothesclass
#a child to the Clothes class, that is the reason we used super
class Caps_Clothes (Clothes):

    def __init__(self, Clothes_type, color, price, size):
        super().__init__(Clothes_type, color, price, size)

# this is the print function
    def __str__(self):
        print(' Your Clothes type:' + self.Clothes_type + ' ' + 'Price: ' + self.price)