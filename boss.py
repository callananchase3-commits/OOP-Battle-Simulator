from enemy import Enemy
import random
class Brute(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 10

    def flamethrower(self):
        return 60

    def attack(self):
        choice = random.choice(["normal", "fireball"])
        if choice == "fireball":
            return self.flamethrower()
        else:
            if self.health < 50:
                self.attack_power = 75
            elif self.health < 150:
                self.attack_power = 50
            elif self.health < 225:
                self.attack_power = 30
            return self.attack_power