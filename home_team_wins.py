import season_data
import numpy as np
import pandas as pd

all_seasons = season_data.all_seasons
n_matches = all_seasons.shape[0]
n_home_wins = len(all_seasons[all_seasons['FTR'] == 'H'])
home_wr = (n_home_wins/n_matches) * 100

print('Total Number of Matches: {}' .format(n_matches))
print('Total Number of Home Wins: {}' .format(n_home_wins))
print('Home Win Rate: {}'.format(n_home_wins/n_matches * 100))