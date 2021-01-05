import numpy as np
import pandas as pd
import all_teams
import season_data
import pl_data
from season_data import all_seasons
from all_teams import all_teams
from pl_data import processSingleSeason
separated_into_teams = []

for i in range(0, (len(all_teams) - 1)):
    addition = []
    separated_into_teams.append(addition)
    addition.append(all_teams[i])
    addition.append(processSingleSeason(all_seasons, all_teams[i]))

print(separated_into_teams[0][1])

