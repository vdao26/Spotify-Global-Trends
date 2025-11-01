import os
import pandas as pd

class CSVManager:
    """Handles loading, validating, and slicing of Spotify Top 50 data."""
    """The functions that will be in this class:
    
    __init__(csv_filename: str)

    load_and_validate_csv() -> pd.DataFrame

    count_tracks() -> int
    
    
    
    """
    def __init__(self, csv_filename: str):
        if not isinstance(csv_filename, str):
            raise TypeError("csv_filename must be a string")
        if not csv_filename.lower().endswith(".csv"):
            raise ValueError("csv_filename must end with .csv")
        self._csv_filename = csv_filename
        self._dataframe = None



    @property 
    def csv_filename(self):
        return self._csv_filename
    @property
    def dataframe(self):
        """Returns the loaded DataFrame."""
        return self._dataframe

    def load_and_validate_csv(self) -> pd.DataFrame:
        """Loads the CSV and checks for required columns."""
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
        """Counts number of rows (tracks) in the CSV file."""
        if self._dataframe is None:
            self.load_and_validate_csv()
        return len(self._dataframe)

    def __str__(self):
        return f"CSVManager({self._csv_filename}) with {len(self._dataframe) if self._dataframe is not None else 0} rows"

    def __repr__(self):
        return f"CSVManager(csv_filename='{self._csv_filename}')"