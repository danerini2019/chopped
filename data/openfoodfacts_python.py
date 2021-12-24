import openfoodfacts
import pprint
import requests

# products = openfoodfacts.products.get_by_country('USA')
# pprint.pprint(len(products))

# for product in openfoodfacts.products.get_all_by_country('USA'):
#     print (product['product_name'])

query_url = 'https://world.openfoodfacts.org/api/v0/product_name/banana.json'
resp_products = requests.get(query_url)
product_json = resp_products.json()
pprint.pprint(product_json)