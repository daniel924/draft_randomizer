import random

teams = [
    'Springer Bell',
    'Ladle\'s Bour Hour',
    'The American Dream',
    'Highlanders',
    'Lenny Dykstra\'s',
    'Charlie CHAPMAN',
    'Rockets',
    'Team Pavelock',
    'Stinky Wizzleteats',
    'Bombers',
]

while teams:
  i = random.randint(0, len(teams)-1)
  print teams.pop(i)
