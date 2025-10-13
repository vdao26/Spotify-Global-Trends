## Function Library Overview

This document provides comprehensive reference information for all functions in the Spotify Global Trends Analysis

## Table of Contents

1. [Data Loading](#data-loading-functions)
2. [Organization](#organization-functions)
3. [SQLite Database Functions](#SQLite-Database-Functions)
4. [Query and Analysis](#Query-Analysis-functions)

---

## Data Loading Functions

### get_top_50_songs_by_countries(csv_filename, country_list)

**Purpose:** Reads a CSV file and returns the top 50 songs for each country in country_list. Filters for the columns: Country, Rank, Title, and Artists.

**Parameters:**
- `csv_filename` (str): Name of CSV file.
- `country_list` (list): List of country names (e.g., ['Spain', 'France']). 

**Returns:** `dict` - Dictionary where keys are country names and values are DataFrames containing the top 50 songs for each country.

**Example Usage**
```python
    top_50_by_country = get_top_50_songs_by_countries(
        "SpotifyTopSongsByCountry - May 2020.csv",
        ["Spain", "South Africa", "Japan", "United States"]
    )

    for country, df in top_50_by_country.items():
        print(f"\nTop 50 Songs in {country}:\n")
        print(df)
```
---


### load_and_validate_csv(file_path)

**Purpose:** Loads a CSV file into a pandas DataFrame and validates its structure. 

**Parameters**
- `file_path` (str): Path to the CSV file.

**Returns:** - `pd.DataFrame` - DataFrame containing the CSV data if valid, else None.

**Example Usage**
```python

    df = load_and_validate_csv(csv_path) #Returns the DataFrame containing the CSV data if valid
    if df is None:
        print("CSV could not be loaded or validated. Exiting.")
        return
    print(" CSV successfully loaded and validated.") 
    print(f"Total records in CSV: {len(df)}") #Counts the total amount of records in the CSV file
```
---


### organize_track_title(title)

**Purpose:** Cleans each track title by removing extra spaces and characters that are not letters or numbers


**Parameters**
- `title` (str): This is the title of the song listed in the dataset.

**Returns:** - `str`: a more organized and updated version of the title.


**Example Usage**
```python
    print(organize_track_title("Happy???    Birthday 100")) # Returns 'Happy Birthday 100'
```
---

### count_tracks(df)

**Purpose:** Counts the number of tracks (songs) that are present in the dataframe.

**Parameters**
- `df` (DataFrame): The dataframe to keep track of the number of songs.

**Returns:** - `int`: The total number of songs


**Example Usage**
```python
    print(count_tracks(df)) #Returns total number of songs in the Dataframe -> 3150
```
---