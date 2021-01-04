import numpy as np
import pandas as pd

df_09_10 = pd.read_csv('data/season-0910_csv.csv')
df_10_11 = pd.read_csv('data/season-1011_csv.csv')
df_11_12 = pd.read_csv('data/season-1112_csv.csv')
df_12_13 = pd.read_csv('data/season-1213_csv.csv')
df_13_14 = pd.read_csv('data/season-1314_csv.csv')
df_14_15 = pd.read_csv('data/season-1415_csv.csv')
df_15_16 = pd.read_csv('data/season-1516_csv.csv')
df_16_17 = pd.read_csv('data/season-1617_csv.csv')
df_17_18 = pd.read_csv('data/season-1718_csv.csv')
df_18_19 = pd.read_csv('data/season-1819_csv.csv')
all_seasons = pd.concat([df_09_10, df_10_11, df_11_12, df_12_13,
                        df_13_14, df_14_15, df_15_16, df_16_17,
                        df_17_18, df_18_19], axis=0)
print('{}\n' .format(all_seasons))