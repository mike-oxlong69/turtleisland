# Course: CS 30
# Period: 3
# Date created: Ocotober 20th, 2021
# Date modified: October 20th, 2021
# Name: Muhammad Munshi
# Description: Inventory for Text-Based Adventure

# Inventory (Starting weapons)
inventory_s = {
    "Spoon":
        {"Description": "Provides small damage and "
            "can be used for utilities", "Damage": 5, "Protection": 0},
    "Butter Knife":
        {"Description": "Can cut wood and butter toast",
            "Damage": 15, "Protection": 0},
    "Pot Lid":
        {"Description": "Provides projectile protection,",
            "Damage": 0, "Protection": 20}
        }


def start_inventory_fnct():
    '''Function to only list name of weapons'''
    for weapon in inventory_s:
        print(f"{weapon}")


def inventory_description():
    '''Function to list name of weapons plus description'''
    for weapon in inventory_s:
        print(f"\n{weapon}:")
        for item in inventory_s[weapon]:
            print(f"{item} - {inventory_s[weapon][item]}")
