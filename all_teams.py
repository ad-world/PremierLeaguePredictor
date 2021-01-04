import numpy as np
import pandas as pd
import season_data
from season_data import *

all_teams = []
for team in all_seasons['HomeTeam']:
    if team in all_teams:
        pass
    else: 
        all_teams.append(team)
all_teams.sort()
print(repr(all_teams)) 
print('Length: ' + str(len(all_teams)))