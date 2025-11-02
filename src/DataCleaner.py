import os
import pandas as pd

class DataCleaner:
     """The functions that will be in this class:
    __init__(dataframe: pd.DataFrame)

    clean_titles() -> pd.DataFrame

    standardize_genres() -> pd.DataFrame

    remove_duplicates() -> pd.DataFrame

    fix_empty_genres() -> pd.DataFrame

    clean_all() -> pd.DataFrame
    """
def __init__(self, dataframe: pd.DataFrame):
     """
     Initialize the DataCleaner with a pandas DataFrame.

     Args:
          dataframe (pd.DataFrame): The spotify dataset that needs to be cleaned.

     Raises:
          TypeError: If dataframe is not a pandas DataFrame.
     """

# ---- PROPERTIES ----
@property
def dataframe(self):
     """Returns cleaned DataFrame."""
     return self._dataframe
#

