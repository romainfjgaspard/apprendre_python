class Pokemon:
    def __init__(self, name, hp, attack, ptype):
        self.name   = name
        self.hp     = hp
        self.attack = attack
        self.ptype  = ptype
        self.alive  = True

    def info(self):
        status = '❤️' if self.alive else '💀'
        return f'{status} {self.name} [{self.ptype}] HP:{self.hp} ATK:{self.attack}'

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f'  💀 {self.name} fainted!')
        else:
            print(f'  💥 {self.name} takes {dmg} damage! HP: {self.hp}')

p = Pokemon('Pikachu', 35, 55, 'Electric')
print(p.info())
p.take_damage(20)
print(p.info())
p.take_damage(20)
print(p.info())