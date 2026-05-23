hp = 25
max_hp = 100
percent = hp / max_hp * 100

if percent > 50:
    status = "🟢 Healthy"
elif percent > 20:
    status = "🟡 Injured"
else:
    status = "🔴 Critical!"

print(f"HP: {hp}/{max_hp} ({percent}%) — {status}")

# Try different values of hp!