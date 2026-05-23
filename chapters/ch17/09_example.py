save_data = {
    'champion': champion,
    'standings': [{'driver': n, 'points': p} for n, p in ranking],
    'season': season,
}

with open('f1_season.json', 'w', encoding='utf-8') as f:
    json.dump(save_data, f, indent=2, ensure_ascii=False)

print('✅ Saved to f1_season.json')