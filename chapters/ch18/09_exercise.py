class Pokemon:
    def __init__(self, name, hp, attack, ptype):
        ???

    def battle_cry(self, attack_name):
        ???  # print(f'{self.name} uses {attack_name}!')

    def __str__(self):
        ???  # return a nice string

# Create at least 3 Pokémon
team = [
    Pokemon('Pikachu', 35, 55, 'Electric'),
    ???,
    ???,
]

print('📋 My Pokédex:')
for p in team:
    print(f'  {p}')
    p.battle_cry('Thunderbolt')

team_size = len(team)
first_name = team[0].name
print(f'\nTeam size: {team_size}')