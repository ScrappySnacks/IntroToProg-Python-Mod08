# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# T. Ward,12-07-2020, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
lstOfProductObjects = []

class Product(object):
    """ Stores data about a product:
    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
        talk: prints product_name and product_price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        T. Ward, 12-07-2020, Modified code to complete assignment 8
    """

    # --Fields--

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --

    @property
    def product_name(self): # Function to get product_name value
        return str(self.__product_name).title() # Convert name to string data type and title case

    @product_name.setter  # Function to set product_name value
    # Input comes in as string
    def product_name(self, value):
        try:
            if value.isnumeric() == True:
                y = int(value) / 0
            else: self.__product_name = value
        except ZeroDivisionError:
            print("Product name cannot be a number")

    @property
    def product_price(self): # Function to get product_price value
        return float(self.__product_price) # Convert price to float data type

    @product_price.setter # Function to set product_price value
    # input comes in as a string
    def product_price(self, value):
        try:
            value = float(value)
        except ValueError:
            print("Price must be a number")
        else:
            self.__product_price = value

    #-- Methods


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        T. Ward, 12-07-2020, Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into lstOfProductObjects
        """
        file = open(file_name, "r")
        for row in file:
            product, price = row.split(",")
            newObj = Product(product, price)
            lstOfProductObjects.append(newObj)
        file.close()
        return lstOfProductObjects, 'Success'

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data to file
        """
        file = open(file_name, "w")
        for rowObj in list_of_product_objects:
            file.write(rowObj.product_name + ", " + rowObj.product_price.__str__() + "\n")
        file.close()
        return lstOfProductObjects, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes input and output

    methods:
        talk(self)  # unpacks the Product object for presentation
        user_input() # solicits product and pricing input from the user
        user_choice() # asks the user for a menu choice

    changelog: (When,Who,What)
        T. Ward, 12-07-2020, Modified code to complete assignment 8
    """

    @staticmethod
    def talk(self):
        print(self.product_name, ",", self.product_price)

    @staticmethod
    def user_input():
        #initialize object
        newObj = Product(product_name= "null", product_price= "0")
        newObj.product_name = input("Please enter a product: ").strip()
        newObj.product_price = input("Please enter the price: ").strip()
        lstOfProductObjects.append(newObj)
        return lstOfProductObjects

    @staticmethod
    def user_choice():
        intChoice = int(input("Please enter a menu choice [1 - 4]: "))
        print()
        return intChoice

    @staticmethod
    def print_menu_options():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
           Menu of Options
           1) Add a new product and price
           2) Show current data 
           3) Save data to file        
           4) Exit program
           ''')
        print()  # Add an extra line for looks

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts

while True:
# Read data from file
    try:
        loadFile = str(input("Please provide the file name for loading data: "))
        FileProcessor.read_data_from_file(loadFile.strip())

    except FileNotFoundError as e:
        print("That file was not found. Try again.")
        print("The built-in Python error message is: ")
        print(e, "\n")

    else: break

while True:

    try:
        # Show user a menu of options
        IO.print_menu_options()
        choice = IO.user_choice()

        if choice == 1:
            # Get user's menu option choice
            IO.user_input()

        # Let user add data to the list of product objects
        elif choice == 2:
            # Show user current data in the list of product objects
            print("Name" + " | " + "Price")
            for row in lstOfProductObjects:
                IO.talk(row)

        elif choice == 3:
            saveFile = str(input("Please provide the file name for saving: "))
            # Let user save current data to file and exit program
            FileProcessor.save_data_to_file(saveFile, lstOfProductObjects)

        elif choice == 4:
            print("Goodbye!")
            break

        else: print("Please enter a valid choice.  Try again. ")

    except ValueError as e:
        print("That was not a number! Try again.")
        print("The built-in Python error message is: ")
        print(e, "\n")

# Main Body of Script  ---------------------------------------------------- #
