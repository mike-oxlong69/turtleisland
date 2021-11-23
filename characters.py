# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Description: Character Selection and function for Text Based Adventure

# chrselect makes false until true
chrselect = True

# Characters with description
character_selection = ["FatBoiBari [1]", "Skinny Pete [2]"]
character_s = {
    "FatBoiBari":
        {"Description": "Chunky monkey and upcoming drill"
            " artist out of Chiraq" ,
            "Bonuses": "Has +1 Speed and +5 Damage points"},
    "Skinny Pete":
        {"Description": "Anorexic ",
            "Bonuses": "Has +1 Damage and +4 Defense points"}
            }


def character_choice():
    '''Function to write out characters with a small description'''
    for character in character_s:
        print(f"\n{character}")
        for item in character_s[character]:
            print(f"{item} - {character_s[character][item]}")


def character_selected():
    '''Function to allow user to choose charcater'''
    print("\nCharacters:")
    global chrselect
    character_choice()
    character_chosen = input("\nWhich character will you choose?\n")
    if character_chosen == "FatBoiBari":
        print("\nFatBoiBari 'SELECTED'")
        print("Great choice, Extra strength will help you\n")
        chrselect = False
    elif character_chosen == "Skinny Pete":
        print("\nSkinny Pete 'SELECTED'")
        print("Excellent, extra defense will come in handy\n")
        chrselect = False
    else:
        print("Please enter a valid character name")
