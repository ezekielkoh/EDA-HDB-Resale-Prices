import requests
import pandas as pd
import numpy as np

# Get hdb_resale prices from data.gov.sg
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=f1765b54-a209-4718-8d38-a39237f502b3'
search_params = {'limit': 0}
response = requests.get(url)
data = response.json()
# get total number of records
total_records = data['result']['total']
# get all records
search_params['limit'] = total_records
response = requests.get(url, params=search_params)
data = response.json()

# convert to pandas dataframe
df = pd.DataFrame(data['result']['records'])
