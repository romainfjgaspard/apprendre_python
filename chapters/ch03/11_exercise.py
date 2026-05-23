# --- Pokemon Health Check ---

pokemon = "Charizard"
hp = 25
max_hp = 100
level = 12

# 1. Is the Pokemon alive?
is_alive = ???

# 2. What percentage of HP does it have left?
health_pct = ???

# 3. What is its status?
#    Above 50% -> "Healthy"
#    Above 20% -> "Injured"
#    Otherwise -> "Critical"
if ???:
    status = "Healthy"
elif ???:
    status = "Injured"
else:
    status = "Critical"

# 4. Can it evolve? Must be alive and at least level 16
can_evolve = ???

print(f"{pokemon}: {hp}/{max_hp} HP ({health_pct}%%)")
print(f"Status: {status}")
print(f"Alive? {is_alive}")
print(f"Can evolve? {can_evolve}")