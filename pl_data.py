import numpy as np
import pandas as pd
import season_data
import all_teams
from season_data import *
from all_teams import all_teams
'''
#print('{}\n' .format(df_2014))
sorted_df_2014 = df_2014.sort_values(['HomeTeam', 'AwayTeam'])
man_united = df_2014[(df_2014['HomeTeam'] == 'Man United') | (df_2014['AwayTeam'] == 'Man United')]
#print('{}\n' .format(man_united_home))
#print('{}\n' .format(sorted_df_2014))
man_united_final = man_united[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
#print('{}\n' .format(man_united_final))

converted = pd.get_dummies(man_united_final)
#print(converted.columns)
n_matrix = converted.values
#print(repr(n_matrix))

teams = []

for team in df_2014['HomeTeam']:
    if team in teams:
        pass
    else: 
        teams.append(team)

#teams.sort()
#print(teams)

print('{}\n' .format(df_09_10))
print('{}\n' .format(df_10_11))
print('{}\n' .format(df_11_12))
print('{}\n' .format(df_12_13))
print('{}\n' .format(df_13_14))
print('{}\n' .format(df_14_15))
print('{}\n' .format(df_15_16))
print('{}\n' .format(df_16_17))
print('{}\n' .format(df_17_18))
print('{}\n' .format(df_18_19))
'''
def processSingleSeason(dataframe, team):
    new_df = dataframe[(dataframe['HomeTeam'] == team) | (dataframe['AwayTeam'] == team)]
    new_df_final = new_df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
    return new_df_final

seasonSeries = pd.Series([df_09_10, df_10_11, df_11_12, df_12_13, 
                        df_13_14, df_14_15, df_15_16, df_16_17, 
                        df_17_18, df_18_19])







