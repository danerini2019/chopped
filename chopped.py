import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np

pd.set_option('display.max_columns', None, 'display.max_columns', None)  
pd.options.display.max_colwidth = None

read = pd.read_csv('data/archive/chopped.csv')
df = pd.DataFrame(read)
df['dessert'].replace('', np.nan, inplace=True)
df.dropna(subset=['dessert'], inplace=True)

# print(df['dessert'].iloc[555])

# Function that accumulates ingredients and adds episode IDs for each row
def get_ingredients(meal):
    episodes = []
    ingredients = []
    meal_list = []
    for i in range(len(df[meal])):
        item_list = df[meal].iloc[i].split(',', -1)
        episode_id = int(str(df['season'].iloc[i]) + str(df['season_episode'].iloc[i]) + str(df['series_episode'].iloc[i]))
        for j in range(len(item_list)):
            episodes.append(episode_id)
            meal_list.append(meal)
            ingredients.append(item_list[j].strip())
    df_ingredients = pd.DataFrame({'episode_id':episodes, 'ingredients':ingredients})
    return df_ingredients

# Function to add columns to ingredients
def add_item_data(dataframe):
    dataframe['count']


# Function accumulates ingredients but cannot add episode IDs
def do_not_use(dataframe, meal):
    item_list = df[meal].str.split(',', -1)
    dataframe['ingredients'] = item_list.apply(pd.Series).stack().reset_index(drop = True)
        
app_items = get_ingredients('appetizer')
ent_items = get_ingredients('entree')
des_items = get_ingredients('dessert')
all = app_items.append(ent_items.append(des_items))
counts = all.groupby('ingredients')['ingredients'].value_counts()
print(counts.head(20))
# print(counts.sort_values(by=[0]))

# freq = all_basket_items['ingredients'].value_counts(bins=4)
# print(freq)

# print(all[all['ingredients'] == 'mustard greens'])