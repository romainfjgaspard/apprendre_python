 import pandas as pd

data = {
    'driver':   ['Verstappen', 'Leclerc', 'Norris', 'Sainz', 'Hamilton', 'Russell'],
    'team':     ['Red Bull',   'Ferrari', 'McLaren','Ferrari','Mercedes','Mercedes'],
    'wins':     [12, 3, 4, 1, 2, 1],
    'podiums':  [18, 9, 11, 5, 7, 4],
    'points':   [410, 280, 350, 220, 190, 175],
}
df = pd.DataFrame(data)
df