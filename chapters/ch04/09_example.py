# range() with 2 arguments: start and stop
print("Levels 1 to 5:")
for level in range(1, 6):   # 1, 2, 3, 4, 5
    print(f"  Level {level}")

# range() with step: count by 2
print("\nEven numbers (0 to 8):")
for n in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(f"  {n}")

# Countdown!
print("\nCountdown:")
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
    print(f"  {i}...")
print("  🚀 GO!")