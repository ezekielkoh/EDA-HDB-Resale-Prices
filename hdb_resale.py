import requests
import pandas as pd
import numpy as np

def get_hdb_resale_price():
    """
    Function:
    ---------
    Retrieves HDB resale prices from https://data.gov.sg

    Initial data pull is limited to 100 records. Total record count is retrieved through the API and used to pull all records.
    ---------

    Returns:
    ---------
    df: pandas dataframe
    """
    search_params = {}

    # pull hdb resale transactions from data.gov.sg
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=f1765b54-a209-4718-8d38-a39237f502b3'
    response = requests.get(url)
    data = response.json()

    # get total number of records
    total_records = data['result']['total']
    search_params['limit'] = total_records

    response = requests.get(url, params=search_params)
    data = response.json()

    return pd.DataFrame(data['result']['records'])

pd = get_hdb_resale_price()
print(pd.head())
