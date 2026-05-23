# Read the file we just created
with open("battle_log.txt", "r") as f:   # "r" = read mode
    content = f.read()

print(content)

# Read line by line
with open("battle_log.txt", "r") as f:
    lines = f.readlines()

print(f"The file has {len(lines)} lines.")
print(f"First line: {lines[0].strip()}")