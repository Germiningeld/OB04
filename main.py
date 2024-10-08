from abc import ABC, abstractmethod

class Fighter():
    pass

class Monster():
    pass

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass