# Save tournament results to JSON
tournament_data = {
    "trainer": "Basile",
    "rounds": len(results),
    "winners": results,
    "fighters": [p["name"] for p in fighters],
}

with open("tournament_results.json", "w") as f:
    json.dump(tournament_data, f, indent=2)

print("✅ Results saved to tournament_results.json!")
print()
print(json.dumps(tournament_data, indent=2))