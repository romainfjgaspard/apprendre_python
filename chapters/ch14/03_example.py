csv_text = '''race,driver,team,position,points
Bahrain,Verstappen,Red Bull,1,25
Bahrain,Leclerc,Ferrari,2,18
Bahrain,Norris,McLaren,3,15
Saudi,Verstappen,Red Bull,1,25
Saudi,Norris,McLaren,2,18
Saudi,Leclerc,Ferrari,3,15
Australia,Norris,McLaren,1,25
Australia,Verstappen,Red Bull,2,18
Australia,Hamilton,Mercedes,3,15
'''

with open('f1_results.csv', 'w', encoding='utf-8') as f:
    f.write(csv_text)

print('✅ f1_results.csv created')