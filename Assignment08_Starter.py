# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Kellen Hunter, 08/31/20, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {ProductName, ProductPrice}
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    #pass
    # TODO: Add Code to the Product class
    # -- Fields --
    strProductName = ""
    intProductPrice = ""
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # product_name
    @property  # DON'T USE NAME for this directive!
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # product_price
    @property  # DON'T USE NAME for this directive!
    def product_price(self): # (getter or accessor)
        return int(self.__product_price).title()  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        if int(value).isinstance():
            self.__product_price = value
        else:
            raise Exception("Prices cannot be letters, please enter in a number")
    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + self.product_price
# Data -------------------------------------------------------------------- #
#objP1 = Product("Kellen", "Hunter")
#print(objP1)

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    #pass
    @staticmethod
    def add_data_to_list(product, price, list_of_rows):
        # TODO: Add Code Here!
        # strTask = input("Enter a task: ")
        # strPriority = input("Enter an priority: ")
        dicRow = {"Product": strProductName, "Price": intProductPrice.strip()}
        lstOfProductObjects.append(dicRow)
        # for objRow in lstTable:
        # print(lstTable)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(product, list_of_rows):
        # TODO: Add Code Here!
        for row in list_of_rows:
            if row["Product"] == product:
                list_of_rows.remove(row)
                # print("The Selected product has been removed from your list")
            return list_of_rows, 'Success'


    # TODO: Add Code to process data from a file
    def ReadFileDataToString(self, file_name):
        with open("products.txt", 'r') as file:
            return file.read()
f = FileProcessor()  # create an object
print(f.ReadFileDataToString("products.txt"))  # use its method

    # TODO: Add Code to process data to a file
def WriteFileDataToString(self, file_name):
    with open("products.txt", 'w') as file:
        return file.write()
f = FileProcessor()  # create an object
#print(f.WriteFileDataToString("products.txt"))  # use its method

# Processing  ------------------------------------------------------------- #

#strProductName = input("Enter a Product Name: ")
#intProductPrice = input("Enter a price:$ ")

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Remove an existing Product
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        #pass  # TODO: Add Code Here!
        Product = input("Enter a New Product: ")
        Price = input("Enter a Price:$ ")
        return Product.strip(), Price.strip()
        # return Product , Price

    @staticmethod
    def input_task_to_remove():
        #pass  # TODO: Add Code Here!
        Product = input("Enter the Product you want to remove: ")
        return Product.strip()
        # return task

    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
# Step 1 - When the program starts, Load data from ToDoFile.txt.
#FileProcessor.ReadFileDataToString(strFileName, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_Products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        strProductName, intProductPrice = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(strProductName.lower(),intProductPrice.lower(), lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        strProductName = IO.input_task_to_remove()
        FileProcessor.remove_data_from_list(strProductName.lower(), lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
        #     FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            FileProcessor.ReadFileDataToString(strFileName, lstOfProductObjects)  # read file data
            IO.input_press_to_continue(strStatus)
            IO.print_current_Tasks_in_list(lstOfProductObjects)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
