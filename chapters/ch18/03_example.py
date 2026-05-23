class Pokemon:
    def __init__(self, name, hp, attack, ptype):
        self.name   = name
        self.hp     = hp
        self.attack = attack
        self.ptype  = ptype

# Create two Pokémon
pikachu = Pokemon('Pikachu', 35, 55, 'Electric')
charizard = Pokemon('Charizard', 78, 84, 'Fire')

print(f'{pikachu.name}: HP={pikachu.hp}, Attack={pikachu.attack}, Type={pikachu.ptype}')
print(f'{charizard.name}: HP={charizard.hp}, Attack={charizard.attack}, Type={charizard.ptype}')