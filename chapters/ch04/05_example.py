# Counting manually with a list of numbers
print("Counting with a list:")
for i in [0, 1, 2, 3, 4]:
    print(f"  Step {i}")

# Each number is a training session!
xp = 0
for session in [1, 2, 3, 4, 5]:
    xp = xp + 10
    print(f"  Session {session} — XP: {xp}")

print(f"\nFinal XP: {xp}")