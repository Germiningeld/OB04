from abc import ABC, abstractmethod

class Fighter():

    def __init__(self, weapon):
        self.weapon = weapon
        print(f'Боец берет {weapon.name}')

    def change_weapon(self, new_weapon):
        print(f'Боец меняет {self.weapon.name} на {new_weapon.name}')
        self.weapon = new_weapon

    def attack(self):
        self.weapon.attack()


class Monster():

    def dead(self):
        print(f'Монстр побежден')

class Weapon(ABC):
    def __init__(self):
        self.name = ''

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        self.name = 'меч'

    def attack(self):
        print(f'Боец наносит удар мечом')

class Bow(Weapon):
    def __init__(self):
        self.name = 'лук'

    def attack(self):
        print(f'Боец стреляет из лука')

sword = Sword()
bow = Bow()
fighter = Fighter(sword)
monster = Monster()

fighter.attack()
monster.dead()
fighter.change_weapon(bow)
fighter.attack()
monster.dead()
