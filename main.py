from abc import ABC, abstractmethod

class Fighter():
    pass

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
    