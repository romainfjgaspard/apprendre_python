# Battle! Attack until the enemy faints.
enemy_hp = 100
my_attack = 25
turns = 0

while enemy_hp > 0:
    enemy_hp = enemy_hp - my_attack
    turns = turns + 1
    print(f"  Turn {turns}: enemy HP = {enemy_hp}")

print(f"\n🏆 Enemy fainted after {turns} turns!")
