# Course: CS 30
# Period: 3
# Date created: November 23rd, 2021
# Date modified: November 23rd, 2021
# Name: Anas Munshi
# Description: enemies script

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class TaxBracket(Enemy):
    def __init__(self):
        super().__init__(name="Tax Bracket", hp=25, damage=3)


class Finances(Enemy):
    def __init__(self):
        super().__init__(name="Finances", hp=30, damage=15)
