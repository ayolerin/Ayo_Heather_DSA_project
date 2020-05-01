# author Ayo
# this is our Clothes class

class Clothes:
    def __init__(self, Clothes_type, color, price, size):
        self.Clothes_type = Clothes_type
        self.color=color
        self.price = price
        self.size = size

    # this is where we are printing our Clothes details
    def __str__(self):
        print(' Your Clothes type:' + self.Clothes_type + ' ' + 'Price: ' + self.price)