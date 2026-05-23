import pandas as pd

# TODO: keep only Ferrari rows  (df[df['team'] == 'Ferrari'])
ferrari = ???

ferrari_wins   = int(ferrari['wins'].sum())
ferrari_points = int(ferrari['points'].sum())
n_ferrari      = len(ferrari)

print(f'🐎 Ferrari summary')
print(f'   drivers : {n_ferrari}')
print(f'   wins    : {ferrari_wins}')
print(f'   points  : {ferrari_points}')