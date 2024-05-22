# Class
    # - Player
    #     Method:
    #         - Name
    #         - health
# Class
    # - Monster
    #     Method:
    #         - Name
    #         - health

# Access_modifier
class Player:
    #attribute
    def __init__(self, health = 100, energy=100): #constructor
        self.health = health
        self.energy = energy
    #method
    def attack(self, target, damage = 1):
        target.health -= damage
        self.energy -= damage
        print(f"Attack to monster, monster health: {target.health} left & your energy is {self.energy}")

class Monster:
    def __init__(self, health = 500):
        self.health = health
        self.health_init = self.health

    def attack(self):
        if self.health < self.health_init:
            print("dragon siap serang balik")
        else:
            print("zzzzz")

player1 = Player()
player2 = Player()
dragon = Monster(health=500)
# print(player.__dict__)
player1.attack(target=dragon, damage=80)
player2.attack(target=dragon, damage=20)
# print(player.__dict__)
# print(monster.__dict__)

print(player1.__dict__)
print(player2.__dict__)
dragon.attack()