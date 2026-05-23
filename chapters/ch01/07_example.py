name = "Pikachu"
hp = 35
attack = 55
level = 5

# f-strings — notice the f before the quote!
print(f"⚡ {name}")
print(f"   Level: {level}")
print(f"   HP: {hp}")
print(f"   Attack: {attack}")
print()

# You can do math inside f-strings!
print(f"{name} at level {level + 1} would have {hp + 10} HP!")