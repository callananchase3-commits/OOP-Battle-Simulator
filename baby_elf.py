from enemy import Enemy

class Baby_Elf(Enemy):
    # NEW ABILITY
    def cry():
        print("WAHHHH WAHHHH")
    
    #Override Take Damagge
    def take_damage(self, damage):
        print("YOU HIT A BABY! YOU MONSTER!!!! 😭😭😭")
        return super().take_damage(damage)
