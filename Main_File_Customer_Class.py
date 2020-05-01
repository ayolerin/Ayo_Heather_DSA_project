# author Ayo
# this is where we are importing

class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    # this is where we print our customer details

    def __str__(self):
        print('\nYour first name is: ', self.first_name,
          "\nYour last name is: ", self.last_name,
          "\nYour password is: " + self.passport_number)


    def login(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has started as an owner\n")
        file.close()


    def select(self, select):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " input" + str(select) + "\n")
        file.close()


    # this is where our customer menu function is
    def menu_customer(self):
        print("Enter 1 to buy a crop top\n"
              "Enter 2 to buy a sweater\n"
              "Enter 3 to buy a Cap\n"
              "Enter 4 to view all our products\n")

        # this is where our book a flight function is


    def buy_CropTop(self):
                a = int(input("Welcome to the Crop Top section\n"
                              "The available Crop Tops are as follows.\n"
                              "Enter 1 for a red Crop Top medium size at $10 \n"
                              "Enter 2 for a white Crop Top small size at $5 \n"
                              "Enter 3 for a black Crop Top large size at $5"))

                if a == 1:
                    print("You have purchased a red Crop Top medium size at $10 ")
                if a == 2:
                    print("You have purchased a white Crop Top small size at $5")
                if a == 3:
                    print("You have purchased a black Crop Top large size at $5")

    def buy_Hoody(self):
        a = int(input("Welcome to the Hoody section\n"
                      "The available Hoodies are as follows.\n"
                      "Enter 1 for a yellow hoody small size at $15 \n"
                      "Enter 2 for a white hoody large size at $20 \n"
                      "Enter 3 for a black hoody medium size at $30"))

        if a == 1:
            print("You have purchased a yellow hoody small size at $15 ")
        if a == 2:
            print("You have purchased a white hoody large size at $20")
        if a == 3:
            print("You have purchased a black hoody medium size at $30")

    def buy_Cap(self):
        a = int(input("Welcome to the Cap section\n"
                      "The available Caps are as follows.\n"
                      "Enter 1 for a white cap medium size at $5 \n"
                      "Enter 2 for a pink cap small size at $5 \n"
                      "Enter 3 for a black cap large size at $5"))

        if a == 1:
            print("You have purchased a white cap medium size at $5 ")
        if a == 2:
            print("You have purchased a pink cap small size at $5")
        if a == 3:
            print("You have purchased a a black cap large size at $5")


    def view(self, clothes_list):
        Customer.inside_view(self)
        print("Available clothes are: ")
        for x in clothes_list:
            print("Clothe type: " + x.Clothes_type + ". Clothe color:" + x.color)

    def inside_view(self):
        file = open(self.first_name + ".txt", "a")
        file.write(self.first_name + " has selected view \n")
        file.close()