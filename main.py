from abc import ABC, abstractmethod

class Fighter():

    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon


class Monster():
    pass

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):

    def attack(self):
        pass

class Bow(Weapon):

    def attack(self):
        pass
