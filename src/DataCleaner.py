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
         if not isinstance(dataframe, pd.DataFrame):
              raise TypeError("The dataframe is not a pandas DataFrame.")
          self._dataframe = dataframe
    # ---- PROPERTIES ----
    @property
    def dataframe(self):
        """Returns cleaned DataFrame."""
        return self._dataframe
# ---- CORE FUNCTIONALITY ----
    def clean_titles(self) -> pd.DataFrame:
         """Removes extra spaces from song titles."""
         for i, row in self._dataframe.iterrows():
              title = row["Title"]
              if type(title) == str:
                   self._dataframe.at[i, "Title"] = title.strip()
     return self._dataframe

    def standardize_genres(self) -> pd.DataFrame:
         """Standardizes the genre names so that it is uniform for the entire dataset."""
         for i, row in self._dataframe.iterrows():
              genre = row["Genre"]
              if type(genre) != str:
                   self._dataframe.at[i, "Genre"] = "Genre Unknown"
              else:
                   genre = genre.strip().lower()
                   if genre in ["hiphop", "hip-hop", "hip hop"]:
                        self._dataframe.at[i, "Genre"] = "Hip-Hop"
                   elif genre in ["r and b", "r&b"]:
                        self._dataframe.at[i, "Genre"] = "R&B"
                   elif genre in ["afro beats", "afro-beats", "afrobeats"]:
                        self._dataframe.at[i, "Genre"] = "Afrobeats"
                   else:
                        self._dataframe.at[i, "Genre"] = genre.title()
          return self._dataframe
          

    def remove_duplicates(self) -> pd.DataFrame:
         """Removes tracks that appear more than once."""
            seen_tracks = []
            updated_data = []
         for i, row in self._dataframe.iterrows():
             title = row["Title"]
             artist = row["Artists"]
             if type(title) == str and type(artist) == str:
                track_id = title + artist
                if track_id not in seen_tracks:
                    seen_tracks.append(track_id)
                    updated_data.append(self._dataframe[i: i+1])
     self._dataframe = pd.concat(updated_data, ignore_index = True)
     return self._dataframe

def fix_empty_genres(self) -> pd.DataFrame:
     """Updates empty genre cells with 'Genre Unknown'"""
     for i, row in self._dataframe.iterrows():
          genre = row["Genre"]
          if type(genre) != str or genre.strip() == "":
               self._dataframe.at[i, "Genre"] = "Genre Unknown"
     return self._dataframe

def clean_all(self) -> pd.DataFrame:
     """Uses all data cleaning functions for the entire dataset."""
     self.clean_titles()
     self.standardize_genres()
     self.remove_duplicates()
     self.fix_empty_genres()
     return self._dataframe

# ---- STRING REPRESENTATIONS ---
def __str__(self):
    return f"DataCleaner with {len(self._dataframe)} rows"
def __repr__(self):
    return "DataCleaner()"

                    
                                   
                    

