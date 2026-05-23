pikachu_hp = 35
charizard_hp = 78

print(pikachu_hp > charizard_hp)   # False
print(pikachu_hp < charizard_hp)   # True
print(pikachu_hp == 35)            # True
print(pikachu_hp != charizard_hp)  # True

# The result is a bool!
is_stronger = pikachu_hp > charizard_hp
print(f"Pikachu stronger? {is_stronger}")  # False
print(type(is_stronger))                   # <class 'bool'>