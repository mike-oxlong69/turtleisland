# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Description: Inventory System for Text-Based Adventure

# Inventory (Starting weapons)
meleeItems = ["Spoon", "Butter Knife", "Sword, Pot Lid"]
rangedItems = ["Bow", "Pistol", "Rifle"]
inventory_s = {
    "Spoon":
        {"Description": "Provides small damage and "
            "can be used for utilities", "Damage": 5, "Protection": 0},
    "Pot Lid":
        {"Description": "Provides projectile protection,",
            "Damage": 0, "Protection": 20}
        }
rangedDesc = {
    "Bow":
        {"Description": "Old wooden Bow, ",
            "Damage": 20, "Ammo": 1},
    "Pistol":
        {"Description": "Small Handheld revolver,",
            "Damage": 15, "Ammo": 20},
    "Rifle":
        {"Description": "Long range rifle,",
            "Damage": 5, "Ammo": 5}
        }
meleeDesc = {
       "Butter Knife":
        {"Description": "Can cut wood and butter toast",
            "Damage": 15, "Protection": 0},
    "Sword":
        {"Description": "Small rusty sword,",
            "Damage": 10, "Protection": 0},
        }


class Weapon():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return "{}\n=======\n{}\nDamage: {}\n".format(self.name,
                                                      self.description,
                                                      self.damage)


class Melee(Weapon):
    def __init__(self, name, description, damage, defense):
        super().__init__(name, description, damage)
        self.defense = defense

    def __str__(self):
        return "{}\n====\n{}\nDamage: {}\nDefense: {}".format(self.name,
                                                              self.description,
                                                              self.damage,
                                                              self.defense)


class Sword(Melee):
    def __init__(self):
        super().__init__(name="Sword",
                         description="An old sword. Rusty and rugged but does damage.",
                         damage=10,
                         defense=0)

class Shield(Melee):
    def __init__(self):
        super().__init__(name="Shield",
                        description="Grants protection from melee and ranged attacks",
                        damage=0,
                        defense=10)

class Range(Weapon):
    def __init__(self, name, description, damage, ammo):
        super().__init__(name, description, damage)
        self.ammo = ammo
    
    def __str__(self):
        return "{}\n=======\n{}\nDamage: {}\nDefense: {}".format(self.name,
        self.description, self.damage, self.ammo)

class Rifle(Range):
    def __init__(self):
        super().__init__(name="Rifle",
                         description="Long range rifle, can shoot twice before reload required, harder to use up close",
                         damage=15,
                         defense=0,
                         ammo=5)

class Pistol(Range):
    def __init__(self):
        super().__init__(name="Pistol",
                         description="Small Handheld revolver",
                         damage=5,
                         defense=0,
                         ammo=20)


def inventory_test():
    print(f"Here is your current melee selection{*meleeItems,}")
    print(f"\nHere is your current ranged selection{*rangedItems,}")
