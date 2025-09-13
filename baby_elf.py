from enemy import enemy
class BabyElf(enemy):
    def cry():
        print("waaahhh!")


    def take_damage(self, damage):
        return super().take_damage(damage)