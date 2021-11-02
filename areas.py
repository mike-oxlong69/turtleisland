# Course: CS 30
# Period: 3
# Date created: Ocotober 20th, 2021
# Date modified: October 20th, 2021
# Name: Muhammad Munshi
# Description: Areas for Text-Based Adventure

# Areas (Starting locations)
area_s = {
    "Tower":
        {"Description": "Water tower ",
         "Risk": 5, "Loot Value": 10},
    "Kitchen":
        {"Description": "Abandoned soup kitchen",
            "Risk": 15, "Loot Value": 20},
    "Bathroom":
        {"Description": "Dorty poopy bafroom,",
            "Risk": -10, "Loot Value": 2}
        }


def start_area_fnct():
    '''Function to only list name of areas'''
    for area in area_s:
        print(f"{area}")


def area_description():
    '''Function to list name of areas plus description'''
    for area in area_s:
        print(f"\n{area}:")
        for item in area_s[area]:
            print(f"{item} - {area_s[area][item]}")
