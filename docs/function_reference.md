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

## Organization Functions

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

### filter_country(df, country: str)

**Purpose:** Filters the dataset by returning rows for a specific country.

**Parameters**
- `df` (DataFrame): The dataset that is being filtered.
- `country`(str): The country name being analyzed.

**Returns:** - `pd.DataFrame`: An updated dataset that only lists information for the specifc country that was filtered.


**Example Usage**
```python
    print(filter_country(df, "South Africa")) #Lists the track records of South Africa
```
---

### delete_repeated_tracks(df)

**Purpose:** Remove tracks that appear more than once based on both title and artist(s)

**Parameters**
- `df` (DataFrame): The dataframe being organized.

**Returns:** - `pd.DataFrame`: Updated dataframe with duplicate tracks removed.


**Example Usage**
```python
       print(delete_repeated_tracks(df)) #Returns the updated dataframe
```
---


### standardize_genre(genre)

**Purpose:** Remove tracks that appear more than once based on both title and artist(s)

**Parameters**
- `genre` (str): The genre that needs to be standardized.

**Returns:** - `str`: An updated version of the genre name that is consistent with other genres in the dataset.


**Example Usage**
```python
       print(standardize_genre("  hiphop")) #'Hip-Hop' More standardized genre
```
---

### fix_empty_genres(df)

**Purpose:** Replace empty genre columns with "Genre Unknown" so that there are no empty spaces.


**Parameters**
- `genre` (str): The genre that needs to be standardized.

**Returns:** - `pd.DataFrame`: An updated version of the dataset that has no empty genre values.

**Example Usage**
```python
       fix_empty_genres(df) #Empty genre values will be placed with 'Genre Unknown'
```
---

## SQLite Database Functions

### create_and_connect_db(db_path: str)

**Purpose:** Creates (if not exists) and connects to an SQLite database.

**Parameters**
- `db_path' (str): Full path to the SQLite database.

**Returns:** - `sqlite3.Connection`: Active SQLite connection object.

**Example Usage**
```python
       db_filename = "Spotify_Top_Tracks_Queries.db" #database name
       conn = create_and_connect_db(os.path.join(script_dir, db_filename)) #Create and connect the database.

```
---

### save_dataframe_to_sqlite(df: pd.DataFrame, conn: sqlite3.Connection, table_name: str, if_exists: str = "replace")

**Purpose:** Saves a pandas DataFrame into an SQLite database using an active connection.

**Parameters**
- `df` (pd.DataFrame): The DataFrame to save.
- `conn`(sqlite3.Connection): Active SQLite connection.
- `table_name` (str): Name of the table to create or append to.
- `if_exists` (str): What to do if the table already exists.
    Options: 'fail', 'replace', 'append'. Default = 'replace'.

**Raises:**
- `ValueError`: If the DataFrame is empty.
- `sqlite3.DatabaseError`: If there’s an issue writing to the database.


**Example Usage**
```python
       for country, df in top_50_by_country.items(): #Goes through the 4 countries we want in the database
        table_name = country.lower().replace(" ", "_")
        save_dataframe_to_sqlite(df, conn, table_name, if_exists="replace") #each country has its own table
        print(f" Saved {country} table to database.")

```
---

## Query-Analysis Functions

### top_genres_per_country(top_50_by_country)

**Purpose:** Finds which genres appear most frequently in each country's Top 50 songs.

**Parameters**
- `top_50_by_country` (dict): Dictionary where keys are country names and values are DataFrames of top 50 songs.

**Returns:** - `pd.DataFrame`: DataFrame showing the top 5 genres for each country.

**Example Usage**
```python
       print(top_genres_per_country(top_50_by_country)) #Top 5 genres per Country

```
---
### number_one_genre_per_country(top_50_by_country)

**Purpose:** Identifies the #1 (most frequent) genre per country.

**Parameters**
- `top_50_by_country` (dict): Dictionary where keys are country names and values are DataFrames of top 50 songs.

**Returns:** - `pd.DataFrame`: DataFrame with each country and its most common genre along with its count.

**Example Usage**
```python
        print(number_one_genre_per_country(top_50_by_country))  # Most popular genre per country
```
---

### artist_country_counts(top_50_by_country)

**Purpose:** Counts how many different countries each artist appears in.

**Parameters**
- `top_50_by_country` (dict): Dictionary of DataFrames keyed by country.

**Returns:** - `pd.DataFrame`: DataFrame showing artists and number of countries they appear in.

**Example Usage**
```python
        artist_counts = artist_country_counts(top_50_by_country)
        print(artist_counts.head()) #Top artists by country count
```
---

### classify_artists(artist_counts_df)

**Purpose:** Categorizes artists as global, regional, or local based on the number of countries they appear in.

**Parameters**
- `artist_counts_df` (pd.DataFrame): DataFrame with columns ['Artist', 'Country Count'].

**Returns:** - `pd.DataFrame`: DataFrame with an additional 'Category' column.

**Example Usage**
```python
       classified = classify_artists(artist_counts) ## Shows Global/Regional/Local classification
       print(classified.head())
```
---
### most_popular_artist_per_country(top_50_by_country)

**Purpose:** Identifies the most popular (most frequently appearing) artist in each country's Top 50 list.

**Parameters**
- `top_50_by_country` (dict): Dictionary where keys are country names and
values are DataFrames of top 50 songs.

**Returns:** - `pd.DataFrame`: DataFrame with columns ['Country', 'Most Popular Artist', 'Song Count'].

**Example Usage**
```python
       print(most_popular_artist_per_country(top_50_by_country)) #Most popular artist by country and returns song count
```
---