from datetime import datetime, timedelta
now = datetime.now()
dateFormat = "%m/%d/%Y"

# Dictionary with food items in fridge as well as expiration date
Expiration = {
    "Yogurt": "1/17/2022",
    "Eggs": "1/23/2022",
    "Lamb Chops": "1/29/2022",
    "Chicken": "1/30/2022",
    "Cabbage": "2/12/2022"
}

# Dictionary with food items in fridge with their categories
Categories = {
    "Yogurt": "Dairy",
    "Eggs": "Protein",
    "Lamb Chops": "Protein",
    "Chicken": "Protein",
    "Cabbage": "Fruits/Veggies"
}

# Dictionary with expired items with their expiration dates
Garbage = {
    "Tomato": "1/15/2022",
    "Milk": "1/7/2022",
    "Bread": "1/1/2022",
    "Milk": "1/1/2022"
}

# Adds the food item to Expiration and Categories with expiration date and category, respectively
def addFood(food, category, date):
    Expiration[food] = date
    Categories[food] = category
    print("We have successfully added your food item. It will expire in %s days" % (findDifference(food)))

# Removes the food item from Expiration and Categories dictionaries
def useFood(food):
    if food in Expiration:
        Expiration.pop(food)
        Categories.pop(food)
        print("That food item has been removed")
    else:
        print("No food of that name")

# Finds the food item and displays its expiration date, the amount of days from today, and its category
def findFood(food):
    if food in Expiration:
        return "%s: Expiration date is %s, which is %s days from now. Category - %s" % (food, Expiration[food], findDifference(food), Categories[food])
    else:
        return "No food of that name"

# Lists each food item that has a given category
def listCategories(category):
    count = 0
    for food in Categories:
        if category == Categories[food]:
            print(findFood(food))
            count += 1
        elif count == 0:
            print("No food of that category")

# Finds the difference from the expiration date to today
def findDifference(food):
    expDate = datetime.strptime(Expiration[food], dateFormat)
    return (expDate - now).days

go = True
reply = ""

while go:
    answer = input(""" *** Welcome! *** 
    Answer A to add a new food item,
    Answer R to remove an item from the fridge,
    Answer F to find an item in your fridge,
    Answer V to view your fridge
    Answer G to view the garbage
    Answer E to exit out of Appetime """)

    if answer == "A":
        (addFood(input("Food name?"), input("Category?"), input("Expiration Date? In format MM/DD/YYYY")))
    elif answer == "R":
        (useFood(input("Food name?")))
        print("The food item has been succesfully removed")
    elif answer == "F":
        print(findFood(input("Food name?")))
    elif answer == "V":
        viewAnswer = input("View by category or by expiration date? C for category, D for expiration date")
        if viewAnswer == "C":
            listCategories(input("What kind of category?"))
        else:
            for food in Expiration:
                print("%s: Expiration date is %s, which is %s days from now." % (food, Expiration[food], findDifference(food)))
    elif answer == "G":
        print(Garbage)
    elif answer == "E":
        go = False
        reply = "N"
    else:
        print("Please try again: Invalid answer")

    while reply != "Y" and reply != "N":
        reply = input("Would you like to return to the main menu? Y/N")
        if reply == "N":
            go = False        
