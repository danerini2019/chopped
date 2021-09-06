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
    # df_ingredients = clean(df_ingredients)
    return df_ingredients

# Function to add columns to ingredients - Not used atm
def add_item_data(dataframe):
    dataframe['count']

# Function to clean dataset
def clean(dataframe):
    dataframe['ingredients'] = dataframe['ingredients'].str.lower()
    return dataframe

# Function accumulates ingredients but cannot add episode IDs
def do_not_use(dataframe, meal):
    item_list = df[meal].str.split(',', -1)
    dataframe['ingredients'] = item_list.apply(pd.Series).stack().reset_index(drop = True)
        
app_items = get_ingredients('appetizer')
ent_items = get_ingredients('entree')
des_items = get_ingredients('dessert')
all = app_items.append(ent_items.append(des_items))
all = clean(all)
ingredients_count = all.pivot_table(columns=['ingredients'], aggfunc='size').sort_values(ascending=False, ignore_index=False).reset_index()
print(ingredients_count.head())
ingredients_count.rename(columns = {list(ingredients_count)[1]: 'count'}, inplace = True)
print(ingredients_count.head())

rambutan = ingredients_count[ingredients_count['ingredients'].str.contains('poblano')]
unique_items = ingredients_count[ingredients_count['count'] == 1]
print(unique_items.head(50))

# freq = all_basket_items['ingredients'].value_counts(bins=4)
# print(freq)

# print(all[all['ingredients'] == 'mustard greens'])