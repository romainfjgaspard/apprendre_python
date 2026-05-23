team = ["Pikachu", "Charizard"]
print("Before:", team)

team.append("Mewtwo")          # add at the end
print("After append:", team)

team.insert(1, "Gengar")        # insert at position 1
print("After insert:", team)

team.remove("Charizard")        # remove by name
print("After remove:", team)

last = team.pop()               # remove and return last
print(f"Popped: {last}")
print("Final:", team)