"""
Creates custom class for encoding and decoding
"""

# Import Libraries
import pandas as pd

class Encode():
    def __init__(self, df) -> None:
        self.encoder_map = {}
        self.df = df

    def transform(self, col:list, target:str=None ):
        """
        Performs mean encoding on specified columns indicated in variable 'col'.
        """
        
        def columns_to_tuples(df, col):
            """
            Converts columns to tuples for indexing
            """
            return tuple(df[c] for c in col)


        # Check if target is specified
        if target is None:
            raise ValueError("Target variable not specified")

        # Check if target is in dataframe
        if target not in self.df.columns:
            raise ValueError("Target variable not in dataframe")

        # Check if columns are in dataframe
        if not all([c in self.df.columns for c in col]):
            raise ValueError("Column not in dataframe")

        # mean_encode identified columns into a dictionary
        mean_encoded = self.df.groupby(col)[target].mean().to_dict()
        self.df = self.df.apply(lambda x: columns_to_tuples(x, col), axis=1)

        # create column 'encoded_value' and map the mean_encoded dictionary to the tuples
        self.df['mean_encoded'] = self.df.apply(lambda x: mean_encoded[x])

        return self.df

    def get_encoded_keys(self):
        return mean_encoded.keys()

# if __name__ == '__main__':
#     pass

mock_df = {
    'col1': ['a','a','b','b','c','c'],
    'col2': ['d','d','e','e','f','f'],
    'value': [1,2,3,4,5,6]

}
mock_df = pd.DataFrame(mock_df)
encoded_df = Encode(mock_df).transform(['col1','col2'], 'value')
print(encoded_df)

