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

