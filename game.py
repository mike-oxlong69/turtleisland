# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Description: Main File for Text Based Adventure
try:
    import sys
    import inventory as inv
    import characters as char
    import gamemap as gmap
except ModuleNotFoundError:
    print("Error, import failed")
    print("Game over")
    sys.exit()

# Starting function to create username for player
print("Text-Based Adventure")
print("Welcome player")
playerName = input("What shall we call you? ")
print("Alright, " + playerName + " choose your option:")

# Actions and directions possible
possible_actions = ["[1] Attack", "[2] Inventory", "[3] Explore",
                    "[4] Map", "[5] Quit"]
possible_directions = ["North [1]", "East [2]", "South [3]", "West [4]"]

# Function to choose character
while char.chrselect:
    char.character_selected()

# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    """Function for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menuSelection = str(input("\nChoose an action: "))
    if menuSelection == "1":
        print("Attack!\n")
    elif menuSelection == "2":
        print("\nInventory:")
        inv.inventory_test()
        ''' inv.start_inventory_fnct()
        inv_desc = input("\nShow descriptions? \nYes [1], No [2] ")
        if inv_desc == "1":
            inv.inventory_description()
        else:
            print("Alright")
        '''
    elif menuSelection == "3":
        for direction in possible_directions:
            print(f" {direction}")
        chosenDirection = str(input("What direction would you like to go? "))
        if chosenDirection == "1":
            print("Going North!")
        elif chosenDirection == "2":
            print("Going East!")
        elif chosenDirection == "3":
            print("Going South!")
        elif chosenDirection == "4":
            print("Going West!")
    elif menuSelection == "4":
            print("World Map")
            gmap.print_map()
    # Quit function will work with the sys.exit command
    elif menuSelection == "5":
        if menuSelection == "5":
            choice_s = str(input("Are you sure you would like to exit? [1] "))
            if choice_s.lower() == "1":
                print("Exiting, Goodbye " + playerName)
                sys.exit()
        else:
            print("Continue!")
    else:
        print("Please enter a valid response")
