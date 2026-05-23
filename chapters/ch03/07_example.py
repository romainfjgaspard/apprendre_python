pokemon_type = "Fire"
level = 15
hp = 30

# Can evolve? Fire type AND level >= 16
can_evolve = pokemon_type == "Fire" and level >= 16
print(f"Can evolve? {can_evolve}")  # False — level too low

# Is it a starter?
name = "Charmander"
is_starter = (name == "Bulbasaur" or name == "Charmander"
              or name == "Squirtle")
print(f"{name} is starter? {is_starter}")  # True