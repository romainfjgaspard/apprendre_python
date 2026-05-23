with open('f1_results.csv', encoding='utf-8') as f:
    lines = f.readlines()

header = lines[0].strip().split(',')
rows   = [line.strip().split(',') for line in lines[1:]]

print('Columns:', header)
print(f'\n{len(rows)} rows loaded:')
for r in rows[:5]:
    print(' ', r)