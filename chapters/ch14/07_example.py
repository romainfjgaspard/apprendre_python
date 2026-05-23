import csv

with open('f1_results.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print('Type of one row:', type(rows[0]).__name__)
print('First row:      ', rows[0])
print('Driver column:  ', rows[0]['driver'])