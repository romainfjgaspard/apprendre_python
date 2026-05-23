import random, json
import matplotlib.pyplot as plt

random.seed(2024)

DRIVERS = [
    {'name': 'Verstappen', 'team': 'Red Bull', 'skill': 95},
    {'name': 'Norris',     'team': 'McLaren',  'skill': 90},
    {'name': 'Leclerc',    'team': 'Ferrari',  'skill': 88},
    {'name': 'Sainz',      'team': 'Ferrari',  'skill': 85},
    {'name': 'Hamilton',   'team': 'Mercedes', 'skill': 87},
    {'name': 'Russell',    'team': 'Mercedes', 'skill': 84},
    {'name': 'Alonso',     'team': 'Aston',    'skill': 82},
    {'name': 'Pérez',      'team': 'Red Bull', 'skill': 80},
]

TRACKS = ['Bahrain', 'Saudi', 'Australia', 'Japan', 'China',
          'Miami', 'Monaco', 'Spain', 'Silverstone', 'Monza']

POINTS_TABLE = [25, 18, 15, 12, 10, 8, 6, 4]   # P1..P8

print(f'{len(DRIVERS)} drivers, {len(TRACKS)} races to go!')