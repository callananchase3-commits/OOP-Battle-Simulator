import random
from goblin import Goblin
from hero import Hero
from boss import MegaKnight

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop - Goblins
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero attacks a random alive goblin
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the goblin is defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins attack the hero
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Outcome after goblin battle
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated by the goblins. Game Over. (｡•́︿•̀｡)")
        print(f"Total goblins defeated: {defeated_goblins} / {len(goblins)}")
        return  # End the game if hero died to goblins

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

    # Boss Battle Begins
    print("\nA dark shadow looms over the battlefield... A BOSS approaches!")
    boss = MegaKnight("MegaKnight")

    while hero.is_alive() and boss.is_alive():
        print("\n--- Boss Battle Round ---")
        
        # Hero attacks boss
        damage = hero.strike()
        print(f"Hero attacks {boss.name} for {damage} damage!")
        boss.take_damage(damage)

        if not boss.is_alive():
            print(f"{boss.name} has been defeated by the hero!")
            break

        # Boss attacks hero
        damage = boss.attack()
        print(f"{boss.name} attacks Hero for {damage} damage!")
        hero.receive_damage(damage)

    # Final Outcome
    if hero.is_alive():
        print("\n🎉 The hero has triumphed over the MegaKnight and all enemies! 🎉")
    else:
        print("\n💀 The hero was slain by the MegaKnight... Game Over. 💀")

if __name__ == "__main__":
    main()

