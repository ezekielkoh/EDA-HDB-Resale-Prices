"""
Creates custom class for encoding and decoding
"""

# Import Libraries
import numpy as np
import pandas as pd
from exceptions import ValueError

class Encode():
    def __init__(self) -> None:
        pass

    def transform(self, df:pd.DataFrame, target:str=None, col:list, method:str):
        """
        Encodes incoming dataframe based on specified method.

        Limits methods to the following strings. Returns error if method is not in list:
            - 'mean'
            - 'median'
            - 'onehot'

        """

