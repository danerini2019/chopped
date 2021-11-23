import pandas as pd
import csv

# openfoodata = pd.read_csv('data/fr.openfoodfacts.org.products.csv', error_bad_lines=False, engine = 'python', lineterminator='\n', header=None)
# df = pd.DataFrame(openfoodata)

# df = pd.read_csv('data/fr.openfoodfacts.org.products.csv', header=None   )

# df = df[0].str.split('\s\|\s', expand=True)

# with open('data/fr.openfoodfacts.org.products.csv', 'rb') as file_obj:
#     reader = csv.reader(file_obj)
#     line_no = 1
#     try:
#         for row in reader:
#             line_no += 1
#     except Exception as e:
#         print (("Error in the line number %d: %s %s" % (line_no, str(type(e)), e.message)))

