# author Heather Mataruse
#we are importing the Clothes class
import PyPDF2
# import docx
from Clothes_Class import *
#this is the crop top clothes class
# a child to the clothes class, that is the reason we used super
class CropTop_Clothes (Clothes):
    def __init__(self, Clothes_type, color, price, size):
        super().__init__(Clothes_type, color, price, size)
        self.Clothes_type_type = Clothes_type

#this is the print function
    def __str__(self):
        print(' Your Clothes type:' + self.Clothes_type + ' ' + 'Price: ' + self.price)