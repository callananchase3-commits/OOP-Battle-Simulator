import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 200
        self.strength = 25
        self.defence = 5

    def strike(self):
        return self.strength + random.randint(-3, 3)

    def receive_damage(self, damage):
        reduced_damage = max(0, damage - self.defence)
        self.hp -= reduced_damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

