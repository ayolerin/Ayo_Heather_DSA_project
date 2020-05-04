# author Ayo
# this is where we are importing

di = [{  "Caps": {"SMALL": ("pink", "$5"), "MEDIUM": ("white", "$5"), "LARGE": ("black", "$5")},
        "CropTop": {"SMALL": ("white", "$5"), "MEDIUM": ("red", "$10"), "LARGE": ("black", "$5")},
        "Hoody": {"SMALL": ("yellow", "$15"), "MEDIUM": ("black", "$30"), "LARGE": ("white", "$20")}}]

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
        file.write(self.first_name + " has started as an customer\n")
        file.close()



    # this is where our customer menu function is
    def menu_customer(self):
        print("Enter 1 to buy a product\n"
              "Enter 2 to view all our products\n")


    def buy(self, di):
                clothes_type = int(input("Enter 1 to buy a cap\n"
                                         "Enter 2 to buy a crop top \n"
                                         "Enter 3 to buy a hoody"))
                if clothes_type == 1:
                    for key, value in di["Caps"].items():
                        print(key, ' : ', value)
                    a =  int(input("Enter 1 to buy a small cap\n"
                                    "Enter 2 to buy a medium cap \n"
                                    "Enter 3 to buy a large cap"))
                    if a == 1:
                        print("You have purchased a small cap, details are as follows", di["Caps"]["SMALL"])
                    if a == 2:
                        print("You have purchased a medium cap, details are as follows", di["Caps"]["MEDIUM"])
                    if a == 3:
                        print("You have purchased a large cap, details are as follows", di["Caps"]["LARGE"])

                if clothes_type == 2:
                    for key, value in di["CropTop"].items():
                        print(key, ' : ', value)
                    a = int(input("Enter 1 to buy a small crop top\n"
                                      "Enter 2 to buy a medium crop top \n"
                                      "Enter 3 to buy a large crop top"))
                    if a == 1:
                        print("You have purchased a small crop top, details are as follows", di["CropTop"]["SMALL"])
                    if a == 2:
                        print("You have purchased a medium crop top, details are as follows", di["CropTop"]["MEDIUM"])
                    if a == 3:
                        print("You have purchased a large crop top, details are as follows", di["CropTop"]["LARGE"])

                if clothes_type == 3:
                    for key, value in di["Hoody"].items():
                        print(key, ' : ', value)
                    a = int(input("Enter 1 to buy a small hoody\n"
                                      "Enter 2 to buy a medium hoody \n"
                                      "Enter 3 to buy a large hoody"))
                    if a == 1:
                        print("You have purchased a small hoody, details are as follows", di["Hoody"]["SMALL"])
                    if a == 2:
                        print("You have purchased a medium hoody, details are as follows", di["Hoody"]["MEDIUM"])
                    if a == 3:
                        print("You have purchased a large hoody, details are as follows", di["Hoody"]["LARGE"])

    def view(self, di):
        for key, value in di.items():
            print(key, ' : ', value)
