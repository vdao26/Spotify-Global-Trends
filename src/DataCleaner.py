import os
import pandas as pd

class DataCleaner:
    """
    Designed to prepare and clean a Spotify Top 50 songs dataset so that it is consistent, 
    accurate, and ready for analysis or storage
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
            if isinstance(title, str):
                self._dataframe.at[i, "Title"] = title.strip()
        return self._dataframe

    def standardize_genres(self) -> pd.DataFrame:
        """Standardizes the genre names so that it is uniform for the entire dataset."""
        for i, row in self._dataframe.iterrows():
            genre = row["Genre"]
            if not isinstance(genre, str):
                self._dataframe.at[i, "Genre"] = "Genre Unknown"
            else:
                genre_lower = genre.strip().lower()
                if genre_lower in ["hiphop", "hip-hop", "hip hop"]:
                    self._dataframe.at[i, "Genre"] = "Hip-Hop"
                elif genre_lower in ["r and b", "r&b"]:
                    self._dataframe.at[i, "Genre"] = "R&B"
                elif genre_lower in ["afro beats", "afro-beats", "afrobeats"]:
                    self._dataframe.at[i, "Genre"] = "Afrobeats"
                else:
                    self._dataframe.at[i, "Genre"] = genre.title()
        return self._dataframe

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Removes duplicate tracks within each country, based on Title + Artists,
        but allows the same track/artist to appear in different countries.
        """
        updated_data = []

        # Group by country
        for country, group in self._dataframe.groupby("Country"):
            seen_tracks = set()
            group_rows = []
            for i, row in group.iterrows():
                title = row["Title"]
                artist = row["Artists"]
                if isinstance(title, str) and isinstance(artist, str):
                    track_id = title.strip() + artist.strip()
                    if track_id not in seen_tracks:
                        seen_tracks.add(track_id)
                        group_rows.append(self._dataframe.loc[i:i])
            if group_rows:
                updated_data.append(pd.concat(group_rows, ignore_index=True))

        self._dataframe = pd.concat(updated_data, ignore_index=True)
        return self._dataframe

    
    def fix_empty_genres(self) -> pd.DataFrame:
        """Updates empty genre cells with 'Genre Unknown'."""
        for i, row in self._dataframe.iterrows():
            genre = row["Genre"]
            if not isinstance(genre, str) or genre.strip() == "":
                self._dataframe.at[i, "Genre"] = "Genre Unknown"
        return self._dataframe

    def clean_all(self) -> pd.DataFrame:
        """Uses all data cleaning functions for the entire dataset."""
        self.clean_titles()
        self.standardize_genres()
        self.remove_duplicates()
        self.fix_empty_genres()
        return self._dataframe

    # ---- STRING REPRESENTATIONS ----
    def __str__(self):
        return f"DataCleaner with {len(self._dataframe)} rows"

    def __repr__(self):
        return "DataCleaner()"


                        
                                    
                        

