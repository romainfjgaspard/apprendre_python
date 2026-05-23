# range() replaces a manual list of numbers
print("Manual list:  [0, 1, 2, 3, 4]")
print("range(5):    ", list(range(5)))   # same thing!

# Train 5 times with range()
level = 1
for i in range(5):
    level = level + 1
    print(f"  Session {i + 1}: level {level}")

print(f"\n🎉 Final level: {level}")