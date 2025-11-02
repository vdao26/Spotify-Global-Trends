## Class/method reference

This document provides reference information for the 4 classes in the Spotify Global Trends Analysis

## Table of Contents

1. [CSVManager](#csv-manager-class)
2. [DataCleaner](#data-cleaner-class)
3. [MusicAnalyzer](#music-analyzer-class)
4. [DatabaseManagement](#database-management-class)

---

## CSV Manager Class

### Description

- The CSVManager class provides functionality for loading, validating, and summarizing Spotify Top 50 CSV data files.
- It ensures proper file handling, column validation, and encapsulated access to loaded data using Python properties.

### Constructor
`__init__(self, csv_filename: str)`

**Parameters:**
- `csv_filename` (str): Filename or path to CSV file

**Raises:**
- `TypeError:` If csv_filename is not a string.
- `ValueError:` If the filename does not end with .csv

**Properties**
- `_csv_filename`: Returns the filename of the CSV file currently managed by the instance.
- `_dataframe`: Provides read-only access to the loaded pandas.DataFrame.
### Methods
- `load_and_validate_csv(self) -> pd.DataFrame`
- `count_tracks(self) -> int`

### Example Usage 
```python
    # Initialize manager 
    manager = CSVManager("SpotifyTopSongsByCountry.csv") 
    # Load and validate 
    data = manager.load_and_validate_csv() 
    # Get number of songs 
    print(manager.count_tracks()) 
    # Display summary 
    print(manager)

```

---
## Data Cleaner Class

---

## Music Analyzer Class

### Description

- The MusicAnalyzer class provides analytical tools for exploring, summarizing, and comparing Spotify Top 50 chart data across multiple countries.

### Constructor
`__init__(self, dataframe: pd.DataFrame)`

**Parameters:**
- `dataframe` (pd.DataFrame): A DataFrame containing Spotify Top 50 data with the following columns: Country, Rank, Title, Artists, and Genre

**Raises:**
- `ValueError`: If any required columns are missing.

**Properties**
- `_dataframe`: Provides access to the dataset for analysis.
    - **Getter**: Returns the DataFrame
    - **Setter**: Allows replacing the internal DataFrame with a new validated DataFrame. 
### Methods
- `get_top_50_songs_by_countries(self, country_list: list[str]) -> dict`
- `top_genres_per_country(self, top_50_by_country: dict) -> pd.DataFrame`
- `number_one_genre_per_country(self, top_50_by_country: dict) -> pd.DataFrame`
- `artist_country_counts(self, top_50_by_country: dict) -> pd.DataFrame`
- `most_popular_artist_per_country(self, top_50_by_country: dict) -> pd.DataFrame`
### Example Usage 
```python
    # Load dataset 
    df = pd.read_csv("SpotifyTopSongsByCountry - May 2020.csv") 
    # Initialize analyzer 
    analyzer = MusicAnalyzer(df) 
    # Analyze top songs 
    top_50 = analyzer.get_top_50_songs_by_countries(["Spain", "United States"]) 
    # Find top genres and artists 
    genres = analyzer.top_genres_per_country(top_50) 
    artists = analyzer.most_popular_artist_per_country(top_50) 
    print(genres.head()) 
    print(artists.head())
```
---
## Database Management Class


---