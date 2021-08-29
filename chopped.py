import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np

pd.set_option('display.max_columns', None, 'display.max_columns', None)  
pd.options.display.max_colwidth = None

read = pd.read_csv('data/archive/chopped.csv')
df = pd.DataFrame(read)

appetizer_items = pd.DataFrame()
entree_items = pd.DataFrame()
dessert_items = pd.DataFrame()

# Function that accumulates ingredients and adds episode IDs for each row
def episode(meal):
    episodes = []
    ingredients = []
    for i in range(len(df[meal])):
        item_list = df[meal].iloc[i].split(',', -1)
        episode_id = int(str(df['season'].iloc[i]) + str(df['season_episode'].iloc[i]) + str(df['series_episode'].iloc[i]))
        for j in range(len(item_list)):
            episodes.append(episode_id)
            ingredients.append(item_list[j])
    df_ingredients = pd.DataFrame({'episode_id':episodes, 'ingredients':ingredients})
    return df_ingredients

# Function accumulates ingredients but cannot add episode IDs
def accumulate_ingredients(dataframe, meal):
    item_list = df[meal].str.split(',', -1)
    dataframe['ingredient'] = item_list.apply(pd.Series).stack().reset_index(drop = True)
        
app_items = episode('appetizer')
ent_items = episode('entree')
des_items = episode('dessert')

print(app_items.head(20))
print(ent_items.head(20))
print(des_items.head(20))