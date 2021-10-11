# Course: CS 30
# Period: 3
# Date created: September 21st, 2021
# Date modified: September 28th, 2021
# Name: Muhammad Munshi
# Description: Menu for Text-Based Adventure
import sys
from time import sleep


# Slow text for unique visual opening text
def slow(text):
    """ Prints title of game in a typewriter style """
    words = str(text)

    for char in words:
        sleep(0.25)
        print(char, end="", flush=True)
# Start of menu player chooses name and is introduced to the game
print("Text-Based Adventure Menu")
print(slow("Welcome player - "))
name = input("What should we call you? ")
print("Alright, " + name + " choose your next move: ")
# Actions and directions possible
possible_actions = ["Sleep", "Study", "Explore", "Eat", "Quit"]
possible_directions = ["north", "east", "south", "west"]

def menu_():
    """Definition for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("Which action would you like to choose? "))
    if menu_c == "Sleep":
        print("Goodnight... ")
    elif menu_c == "Study":
        print("Pursuing educational prowess, please wait ")
    elif menu_c == "Explore":
        # The program's way of taking directions
        for direction in possible_directions:
                print(f" {direction}")
        directions_chosen = input("What direction would you like to go? ")
        if directions_chosen.lower() in possible_directions:
            print(f"Going {directions_chosen}!")
        else:
            print("Invalid direction, choose a direction!")
    elif menu_c == "Eat":
            print("Eating!")
    # Quit function will work with the sys.exit command
    elif menu_c == "Quit":
        choice_s = input("Are you sure? Enter 'yes' to quit, or any other key to return ")
        if choice_s.lower() == "yes":
            print("Exiting, Goodbye " + name)
            sys.exit()     
        else:
            print("Continue!")
    else:
        print("Please enter a valid option ")

# Infinite loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    menu_()
