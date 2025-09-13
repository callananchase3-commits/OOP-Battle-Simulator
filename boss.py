from enemy import Enemy
import random

class MegaKnight(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 10

    def jump(self):
        print("MEAGAAA KNIGHTTTTT!")
        return 100

    def attack(self):
        choice = random.choice(['normal', 'jump'])

        if choice == 'jump':
            return self.jump()
        else:
            if self.health < 10:
                self.attack_power = 50
            elif self.health < 50:
                self.attack_power = 30
            elif self.health < 150:
                self.attack_power = 20
            else:
                self.attack_power = 10  # default attack power
            
            return random.randint(1, self.attack_power)
        #fawdddadwa
        

