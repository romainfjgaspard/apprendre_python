class Pokemon:
    def __init__(self, name, hp, attack, ptype):
        self.name   = name
        self.hp     = hp
        self.attack = attack
        self.ptype  = ptype

    def __str__(self):
        return f'🔴 {self.name} [{self.ptype}] HP:{self.hp} ATK:{self.attack}'

p = Pokemon('Gengar', 60, 65, 'Ghost')
print(p)  # calls __str__ automatically!