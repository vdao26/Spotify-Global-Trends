import os
import pandas as pd

class CSVManager:
    """Handles loading, validating, and slicing of Spotify Top 50 data.
    
    Example:
    >>> manager = CSVManager("SpotifyTopSongsByCountry - May 2020.csv") 
    >>> manager.load_and_validate_csv() 
    >>> print(manager.count_tracks()) 5000 
    >>> print(manager) CSVManager(SpotifyTopSongsByCountry - May 2020.csv) with 5000 rows
    

    """
    
    def __init__(self, csv_filename: str):
        """
        Initialize the CSVManager with a given filename.

        Args:
            csv_filename (str): The name or path of the CSV file.

        Raises:
            TypeError: If csv_filename is not a string.
            ValueError: If csv_filename does not end with '.csv'.
        """
        if not isinstance(csv_filename, str):
            raise TypeError("csv_filename must be a string")
        if not csv_filename.lower().endswith(".csv"):
            raise ValueError("csv_filename must end with .csv")
        # Private attributes (encapsulation)
        self._csv_filename = csv_filename
        self._dataframe = None

    # ---- PROPERTIES ----
    @property 
    def csv_filename(self):
        return self._csv_filename
    @property
    def dataframe(self):
        """Returns the loaded DataFrame."""
        return self._dataframe

    # ---- CORE FUNCTIONALITY ----
    def load_and_validate_csv(self) -> pd.DataFrame:
        """Loads the CSV and checks for required columns.
        
        Args: file_path (str): Path to the CSV file.
        Returns: pd.DataFrame: DataFrame containing the CSV data if valid, else None.
        Handles:
            FileNotFoundError – when file path is invalid.
            pd.errors.EmptyDataError – when CSV is empty.
            Other exceptions – prints generic error message.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, self._csv_filename)
        try:
            df = pd.read_csv(csv_path)
            required = {"Country", "Rank", "Title", "Artists", "Genre"}
            if not required.issubset(df.columns):
                raise ValueError(f"CSV file must contain: {required}")
            self._dataframe = df
            return df
        except FileNotFoundError:
            print(f"Error: File not found: {csv_path}")
        except pd.errors.EmptyDataError:
            print("Error: CSV is empty.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return None

    def count_tracks(self) -> int:
        """Counts number of rows (tracks) in the CSV file.
        
        Counts the number of tracks (songs) that are present in the dataframe.

        Args:
        df(DataFrame): The dataframe to keep track of the number of songs.

        Returns:
            int: The total number of songs.
        """
        if self._dataframe is None:
            self.load_and_validate_csv()
        return len(self._dataframe)
    # ---- STRING REPRESENTATIONS ----
    def __str__(self):
        return f"CSVManager({self._csv_filename}) with {len(self._dataframe) if self._dataframe is not None else 0} rows"

    def __repr__(self):
        return f"CSVManager(csv_filename='{self._csv_filename}')"