# author Ayo
#we are importing the plane class
from Clothes_Class import Clothes

#this is the hoody class
#a child to the clothes class, that is the reason we used super
class Hoody_Clothes (Clothes):
    def __init__(self, Clothes_type, color, price, size):
        super().__init__(Clothes_type, color, price, size)
        self.Clothes_type_type = Clothes_type

    # this is the print function
    def __str__(self):
        print(' Your Clothes type:' + self.Clothes_type + ' ' + 'Price: ' + self.price)
