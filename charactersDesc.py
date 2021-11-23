# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Desscription: Classes for characters
import inventory as inv


class MainCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw instances of MainCharacter objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    def __getinventory__(self, inventory):
        return self.inventory


class FatBoiBari(MainCharacter):
    """
    Chunky monkey, upcoming drill artist
    """
    def __init__(self):
        self.name = "FatBoiBari"
        self.identity = "+1 Speed, +5 Damage"
        self.hp = 100
        self.inventory = inv.inventory_description()
        self.supplies = []
 

class SkinnyPete(MainCharacter):
    """
    Average joe who might have lifted 
    a little too much weights.
    """
    def __init__(self):
        self.name = "Skinny Pete"
        self.bonus = "+1 Damage, +4 Defense"
        self.hp = 100
        self.inventory = inv.inventory_description()
        self.supplies = []


# assign variables to hero classes and put them in a list
FatBoiBari = FatBoiBari()
SkinnyPete = SkinnyPete()
heroes = [FatBoiBari, SkinnyPete]

def hero_check(hero):
    """Prints characteristics for character"""
    if hero == "FatBoiBari":
        hero_characteristics(FatBoiBari)
    elif hero == "Skinny Pete":
        hero_characteristics(SkinnyPete)

def hero_characteristics(hero):
    """Prints out the hero's characteristics"""
    print(f"{hero.name}'s true identy is {hero.identity}")
    print(f"{hero.name}'s super power is {hero.power}")
    print(f"{hero.name} has {hero.hp} health points")
    if len(hero.supplies) != 0:
        protection = hero.supplies[0]
        weapon = hero.supplies[1]
        if len(protection) != 0:
            print(f"{hero.name}'s current protection items:")
            for items in protection:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no protection items")
        if len(weapon) != 0:
            print(f"{hero.name}'s current weapons:")
            for items in weapon:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no weapons.")
    else:
        print(f"{hero.name} has no supplies.")
    if len(hero.inventory) != 0:
        protection = hero.inventory[0]
        weapon = hero.inventory[1]
        if len(protection) != 0:
            print(f"{hero.name}'s current protection items:")
            for items in protection:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no protection items")
        if len(weapon) != 0:
            print(f"{hero.name}'s current weapons:")
            for items in weapon:
                print(f"* {items}")
        else:
            print(f"{hero.name} has no weapons.")
    else:
        print(f"{hero.name} has no weapons or protection items.")
