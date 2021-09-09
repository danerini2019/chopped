import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pprint

pd.set_option('display.max_columns', None, 'display.max_rows', None)  
pd.options.display.max_colwidth = None

chopped_read = pd.read_csv('data/archive/chopped.csv')
df = pd.DataFrame(chopped_read)
df['dessert'].replace('', np.nan, inplace=True)
df.dropna(subset=['dessert'], inplace=True)

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

# Function to clean dataset - will add functionality that will add columns with added information
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
ingredients = all.pivot_table(columns=['ingredients'], aggfunc='size').sort_values(ascending=False, ignore_index=False).reset_index()
ingredients.rename(columns = {list(ingredients)[1]: 'count'}, inplace = True)

# filter tests
poblano = ingredients[ingredients['ingredients'].str.contains('poblano')]
unique_items = ingredients[ingredients['count'] == 1]
repeat_items = ingredients[ingredients['count'] > 1]

# ingredients_set = pd.read_csv('data/archive/ingredients v1.csv')
ingredients_set = pd.read_csv('data/archive/food.csv')
df_compare = pd.DataFrame(ingredients_set)
pprint.pprint(df_compare[['Category', 'Description']].iloc[-100:])


# Plotting section


# bar plot for frequency of item appearence
# plt.style.use('ggplot')

# x = repeat_items['ingredients'][:50]
# count = repeat_items['count'][:50]

# x_pos = [i for i, _ in enumerate(x)]

# plt.bar(x_pos, count, color='green')
# plt.xlabel("Ingredient")
# plt.ylabel("# of Appearences")
# plt.title("Chopped Ingredient Frequency")


# plt.xticks(x_pos, x, rotation=90)

# plt.show()
# plt.close()