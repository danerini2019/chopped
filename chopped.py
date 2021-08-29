import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np

pd.set_option('display.max_columns', None, 'display.max_columns', None)  
pd.options.display.max_colwidth = None

read = pd.read_csv('data/archive/chopped.csv')
df = pd.DataFrame(read)
df_ing = pd.DataFrame()

# df[['app_ing_1','app_ing_2','app_ing_3','app_ing_4','app_ing_5','app_ing_6']] = df['appetizer'].str.split(',', -1)
# df[['ent_ing_1','ent_ing_2','ent_ing_3','ent_ing_4','ent_ing_5','ent_ing_6']] = df['entree'].str.split(',', -1)
# df[['des_ing_1','des_ing_2','des_ing_3']] = df['dessert'].str.split(',', -1)

df['app_ing_type'] = type(df['appetizer'])

# df['app_ing'] = df['appetizer'].str.split(',', -1).apply(len)
# df['ent_ing'] = df['entree'].str.split(',', -1).apply(len)
# # df['des_ing_count'] = df['dessert'].str.count(',').apply(int) + 1
# # df['des_ing_count'] = int(df['des_ing_count'])
# df['des_ing'] = df['dessert'].str.split(',', -1).fillna(0).apply(len)

appetizer_items = pd.DataFrame()
entree_items = pd.DataFrame()
dessert_items = pd.DataFrame()


def episode(meal):
    df_ing['episode_id'] = np.nan
    df_ing['ingredient'] = ''
    for i in range(len(df[meal])):
        item_list = df[meal].str.split(',', -1)
        episode_id = df['season'].iloc[i] + df['season_episode'].iloc[i] + df['series_episode'].iloc[i]
        episode_break_point = len(df_ing['ingredient'])
        print(episode_break_point)
        for j in range(len(item_list)):
            df_ing['episode_id'] = episode_id
        
    df_ing['ingredient'] =  item_list.apply(pd.Series).stack().reset_index(drop = True)
        

def accumulate_ingredients(dataframe, meal):
    item_list = df[meal].str.split(',', -1)
    dataframe['ingredient'] = item_list.apply(pd.Series).stack().reset_index(drop = True)
        

episode('appetizer')
episode('entree')
episode('dessert')
# item_list = df['appetizer'].str.split(',', -1)
# df_ing['app_ing'] = item_list.apply(pd.Series).stack().reset_index(drop = True)

print(df_ing.head())
# print(df['num_ing'].apply(len))
# print(df.app_ing_count.unique())
# print(df.ent_ing_count.unique())
# print(df.des_ing_count.unique())