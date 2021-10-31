# Course: CS 30
# Period: 3
# Date created: Ocotober 20th, 2021
# Date modified: October 26th, 2021
# Name: Anas Munshi
# Description: Character Selection and function for Text Based Adventure

# Variable used to maintain loop if user's selection is invalid
characterSelect = True

# Characters with description
characters = ["Mark Markothy [1]", "Jacob Jaqueefious [2]"]
characterDescriptions = {
    "Mark Markothy":
        {"Description": "Middle aged white man with kids, "
            "has no skills whatsoever, also disabled",
            "Bonuses": "None lol"},
    "Jacob Jaqueefious":
        {"Description": "Superman but black basically. "
            "Plus jimgunis bunda",
            "Bonuses": "Has +999 Damage and +999 Defense points"}
            }


def character_choice():
    '''Function to write out characters with a small description'''
    for character in characterDescriptions:
        print(f"\n{character}")
        for item in characterDescriptions[character]:
            print(f"{item} - {characterDescriptions[character][item]}")


def character_selector():
    '''Function to allow user to choose character'''
    print("\nCharacters:")
    global characterSelect
    character_choice()
    character_chosen = input("\nSelect character [1][2]\n")
    if character_chosen == "1":
        print("\nMark Markothy 'SELECTED'")
        print("lel ur screwed breh\n")
        characterSelect = False
    elif character_chosen == "2":
        print("\nJacob Jaqueefious 'SELECTED'")
        print("easy peasy from here\n")
        characterSelect = False
    else:
        print("Please select a valid number (1 or 2)")
