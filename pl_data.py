import numpy as np
import pandas as pd
import season_data
import all_teams
import IPython
import sklearn
import matplotlib.pyplot as plt
from IPython.display import display
from season_data import *
from all_teams import *
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

'''
# this function takes in a df and a team as args, and outputs
# the df with all the wanted columns
def processSingleSeason(dataframe, team):
    new_df = dataframe[(dataframe['HomeTeam'] == team) | (dataframe['AwayTeam'] == team)]
    new_df_final = new_df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']]
    return new_df_final

def processAllSeason(dataframe):
    new_df = dataframe[['FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']]
    return new_df

## a series for all the seasons
seasonSeries = pd.Series([df_09_10, df_10_11, df_11_12, df_12_13, 
                        df_13_14, df_14_15, df_15_16, df_16_17, 
                        df_17_18, df_18_19, df_19_20])

all_seasons_processed = processAllSeason(season_data.all_seasons)
'''from pandas.plotting import scatter_matrix
scatter_matrix(all_seasons_processed)
plt.show()
'''

x_data = all_seasons_processed.drop(['FTR'], 1)
y_data = all_seasons_processed['FTR']


from sklearn.preprocessing import scale
cols = [['FTHG', 'FTAG', 'HTHG', 'HTAG']]
for col in cols:
    x_data[col] = scale(x_data[col])


for col, col_data in x_data.items():

    # If data type is categorical, convert to dummy variables
    if col_data.dtype == object:
        col_data = pd.get_dummies(col_data, prefix=col)
        x_data[col] = col_data

                    
        # Collect the revised columns
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=50, random_state=2, stratify=y_data)