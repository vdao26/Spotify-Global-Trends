"""
Spotify Global Trends Function Library

This module provides utility functions for spotify global trends including data loading, data
cleaning and filtering, SQLite Database, query and analysis, and display/reporting. 

Team Members: Vivian Dao, Fatimah Shaw, Christiana Crabbe, Vince Baluis
Course: Object-Oriented Programming for Information Science
"""

import os
import pandas as pd
import sqlite3

def get_top_50_songs_by_countries(csv_filename, country_list):
    """
    Reads a CSV file and returns the top 50 songs for each country in country_list.
    Filters for the columns: Country, Rank, Title, and Artists.

    Args:
        csv_filename (str): Name of the CSV file.
        country_list (list): List of country names (e.g., ['Spain', 'France']).

    Returns:
        dict: Dictionary where keys are country names and values are DataFrames
              containing the top 50 songs for each country.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, csv_filename)
    
    df = pd.read_csv(csv_path)
    
    results = {}

    for country in country_list:
        country_df = df[df['Country'].str.lower() == country.lower()].copy()

        country_df = country_df[['Country', 'Rank', 'Title', 'Artists','Genre']]

        country_df['Rank'] = pd.to_numeric(country_df['Rank'], errors='coerce')
        top_50 = country_df.sort_values('Rank').head(50)

        results[country] = top_50

    return results

def load_and_validate_csv(file_path):
    """
    Loads a CSV file into a pandas DataFrame and validates its structure.
    Args: 
        file_path (str): Path to the CSV file.
    Returns: 
        pd.DataFrame: DataFrame containing the CSV data if valid, else None.
    """
    try:
        df = pd.read_csv(file_path)
        required_columns = {'Country', 'Rank', 'Title', 'Artists', 'Genre'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"CSV file must contain the following columns: {required_columns}")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the CSV file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def organize_track_title(title):
    """
    Cleans each track title by removing extra spaces and characters that are not letters or numbers

    Args:
    title(str): This is the title of the song listed in the dataset.

    Returns:
    str: a more organized and updated version of the title.

    Example:
    >>> organize_track_title("Happy???    Birthday 100")
    'Happy Birthday 100'
    """

    title = title.strip()
    useable_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    updated_title = ""

    for char in title:
        if char in useable_char:
            updated_title = updated_title + char
    return updated_title

def count_tracks(df):
    """
    Counts the number of tracks (songs) that are present in the dataframe.

    Args:
        df(DataFrame): The dataframe to keep track of the number of songs.

    Returns:
        int: The total number of songs.

        Example:
        >>> count_tracks(df)
        50
    """
    csv_filename = "SpotifyTopSongsByCountry - May 2020.csv"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, csv_filename)
    
    df = pd.read_csv(csv_path)
    total_num_tracks = 0
    for i in range(len(df)):
        total_num_tracks +=1
    return total_num_tracks

def filter_country(df, country: str):
    """
    Filters the dataframe by returning rows for a specific country.

    Args:
        df(DataFrame): The dataframe that is being filtered.
        country (str): The country name being analyzed.

    Returns:
        Dataframe: An updated dataframe that only lists information for the specifc country that was filtered.
        Example:
        >>> filter_country(df, "South Africa")
    """

    df = pd.read_csv("src/SpotifyTopSongsByCountry - May 2020.csv")
    if 'Country' not in df.columns:
        raise KeyError("DataFrame missing 'Country' column")

    normalized_country = str(country).strip().lower()
    df = df.copy()
    df['Country'] = df['Country'].astype(str).str.strip().str.lower()

    updated_dataset = df[df["Country"] == normalized_country]
    return updated_dataset

def delete_repeated_tracks(df):
    """
    Remove tracks that appear more than once based on both title and artist(s)

    Args:
        df (DataFrame): The dataframe being organized.
    Returns:
        DataFrame: Updated dataset with duplicate tracks removed.
    Example:
        >>> delete_repeated_tracks(df)
    """
    tracks = []
    updated_data = []

    for i in range(len(df)):
        for index, row in df.iterrows():
            title = row["Title"]
            artists = row["Artists"]
        track_identifier = title + artists

        if track_identifier not in tracks:
            tracks.append(track_identifier)
            updated_data.append(df[i:i+1])

    return pd.concat(updated_data, ignore_index = True)

def standardize_genre(genre):
    """
    Standardize the name of each genre for consistency

    Args:
        genre (str): The genre that needs to be standardized.
    Returns:
        str: An updated version of the genre name that is consistent with other genres in the dataset.

    Example:
        >>> standardize_genre("  hiphop")
        'Hip-Hop'
    """
    if type(genre) != str:
        return "invalid genre name"
    genre = genre.strip()
    genre = genre.lower()

    if genre in["hiphop", "hip-hop", "hip hop"]:
        return "Hip-Hop"
    if genre in["r&b", "r and b", "rnb"]:
        return "R&B"
    if genre in["afro beats", "afro-beats", "afrobeats"]:
        return "Afrobeats"
   
    return genre.title()

def fix_empty_genres(df):
    """
    Replace empty genre columns with "Genre Unknown" so that there are no empty spaces.

    Args:
        df (DataFrame): The dataset that needs genres to be organized.

    Returns:
        DataFrame: An updated version of the dataset that has no empty genre values.

    Example:
        >>> fix_empty_genres(df)
    """
    csv_filename = "SpotifyTopSongsByCountry - May 2020.csv"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, csv_filename)
    
    df = pd.read_csv(csv_path)
    df["Genre"] = df["Genre"].replace("", pd.NA)
    
    # Fill NA with 'Unknown'
    df["Genre"] = df["Genre"].fillna("Unknown")
    
    return df


def connect(db_path: str, conn: sqlite3.Connection = None) -> sqlite3.Connection:
    """
    Open a SQLite connection and return it (reuses existing connection).

    Args:
        db_path (str): Path to the SQLite database file.
        conn (sqlite3.Connection, optional): Existing connection to reuse.

    Returns:
        sqlite3.Connection: SQLite connection object.

    Raises:
        sqlite3.Error: If connection cannot be established.
    """
    if conn is None:
        dirpath = os.path.dirname(db_path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        conn = sqlite3.connect(db_path)
    return conn


def close_connection(conn: sqlite3.Connection):
    """
    Close the database connection if open.

    Args:
        conn (sqlite3.Connection): The connection to close.
    """
    if conn:
        conn.close()


def save_dataframe(df: pd.DataFrame, db_path: str, table_name: str, if_exists: str = "replace"):
    """
    Save a pandas DataFrame to the specified table in the SQLite database.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        db_path (str): Path to the database file.
        table_name (str): Table name to store the DataFrame in.
        if_exists (str): 'replace', 'append', or 'fail'. Defaults to 'replace'.

    Raises:
        TypeError: If df is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    conn = connect(db_path)
    df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    close_connection(conn)


def execute_query(db_path: str, query: str) -> list:
    """
    Execute a SQL query on the database and return results.

    Args:
        db_path (str): Path to the SQLite database.
        query (str): SQL query to execute.

    Returns:
        list: List of tuples with query results.
    """
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    results = cursor.fetchall()
    close_connection(conn)
    return results


def fetch_table(db_path: str, table_name: str) -> pd.DataFrame:
    """
    Fetch all data from a specified table as a pandas DataFrame.

    Args:
        db_path (str): Path to the SQLite database.
        table_name (str): Name of the table to fetch.

    Returns:
        pd.DataFrame: DataFrame containing the table data.
    """
    conn = connect(db_path)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    close_connection(conn)
    return df


def table_exists(db_path: str, table_name: str) -> bool:
    """
    Check if a table exists in the SQLite database.

    Args:
        db_path (str): Path to the SQLite database.
        table_name (str): Name of the table to check.

    Returns:
        bool: True if the table exists, False otherwise.
    """
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name=?;
    """, (table_name,))
    exists = cursor.fetchone() is not None
    close_connection(conn)
    return exists


def delete_table(db_path: str, table_name: str):
    """
    Delete a table from the SQLite database.

    Args:
        db_path (str): Path to the SQLite database.
        table_name (str): Table name to delete.
    """
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    close_connection(conn)


def list_tables(db_path: str) -> list:
    """
    List all tables in the SQLite database.

    Args:
        db_path (str): Path to the SQLite database.

    Returns:
        list: List of table names.
    """
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table';
    """)
    tables = [table[0] for table in cursor.fetchall()]
    close_connection(conn)
    return tables

    
def top_genres_per_country(top_50_by_country):
    """
    Finds which genres appear most frequently in each country's Top 50 songs.

    Args:
        top_50_by_country (dict): Dictionary where keys are country names and
                                  values are DataFrames of top 50 songs.

    Returns:
        pd.DataFrame: DataFrame showing the top 5 genres for each country.
    """
    country_genres = []

    for country, df in top_50_by_country.items():
        if 'Genre' in df.columns:
            top_genres = df['Genre'].value_counts().head(5)
            for genre, count in top_genres.items():
                country_genres.append({'Country': country, 'Genre': genre, 'Count': count})

    return pd.DataFrame(country_genres)

def number_one_genre_per_country(top_50_by_country):
    """
    Identifies the #1 (most frequent) genre per country.

    Args:
        top_50_by_country (dict): Dictionary where keys are country names and
                                  values are DataFrames of top 50 songs.

    Returns:
        pd.DataFrame: DataFrame with each country and its most common genre.
    """
    top_genre_list = []

    for country, df in top_50_by_country.items():
        if 'Genre' in df.columns:
            top_genre = df['Genre'].value_counts().idxmax()
            count = df['Genre'].value_counts().max()
            top_genre_list.append({'Country': country, 'Top Genre': top_genre, 'Count': count})

    return pd.DataFrame(top_genre_list)

def artist_country_counts(top_50_by_country):
    """
    Counts how many different countries each artist appears in.

    Args:
        top_50_by_country (dict): Dictionary of DataFrames keyed by country.

    Returns:
        pd.DataFrame: DataFrame showing artists and number of countries they appear in.
    """
    artist_country_map = {}

    for country, df in top_50_by_country.items():
        for artist_list in df['Artists']:
            for artist in [a.strip() for a in artist_list.split(',')]:
                if artist not in artist_country_map:
                    artist_country_map[artist] = set()
                artist_country_map[artist].add(country)

    data = [{'Artist': artist, 'Country Count': len(countries)} for artist, countries in artist_country_map.items()]
    return pd.DataFrame(data).sort_values('Country Count', ascending=False)

def classify_artists(artist_counts_df):
    """
    Categorizes artists as global, regional, or local based on the number of countries they appear in.

    Args:
        artist_counts_df (pd.DataFrame): DataFrame with columns ['Artist', 'Country Count'].

    Returns:
        pd.DataFrame: DataFrame with an additional 'Category' column.
    """
    def categorize(count):
        if count >= 3:
            return "Global"
        elif count == 2:
            return "Regional"
        else:
            return "Local"

    artist_counts_df['Category'] = artist_counts_df['Country Count'].apply(categorize)
    return artist_counts_df

def most_popular_artist_per_country(top_50_by_country):
    """
    Identifies the most popular (most frequently appearing) artist in each country's Top 50 list.

    Args:
        top_50_by_country (dict): Dictionary where keys are country names and
                                  values are DataFrames of top 50 songs.

    Returns:
        pd.DataFrame: DataFrame with columns ['Country', 'Most Popular Artist', 'Song Count'].
    """
    popular_artists = []

    for country, df in top_50_by_country.items():
        if 'Artists' not in df.columns or df.empty:
            continue

        # Split artists by comma and count frequencies
        artist_series = (
            df['Artists']
            .dropna()
            .apply(lambda x: [a.strip() for a in x.split(',')])
            .explode()
        )

        if artist_series.empty:
            continue

        top_artist = artist_series.value_counts().idxmax()
        count = artist_series.value_counts().max()

        popular_artists.append({
            'Country': country,
            'Most Popular Artist': top_artist,
            'Song Count': count
        })

    return pd.DataFrame(popular_artists)


if __name__ == "__main__":
    top_50_by_country = get_top_50_songs_by_countries(
        "SpotifyTopSongsByCountry - May 2020.csv",
        ["Spain", "South Africa", "Japan", "United States"]
    )

   # --- Define database path ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_filename = "Spotify_Top_Tracks_Queries.db"
    db_path = os.path.join(script_dir, db_filename)

    # --- Display results ---
    for country, df in top_50_by_country.items():
        print(f"\nTop 50 Songs in {country}:\n")
        print(df)

    # --- Create database connection ---
    conn = connect(db_path)
    print(f"\nConnected to database: {db_path}")

    # --- Save each country's DataFrame ---
    for country, df in top_50_by_country.items():
        table_name = country.lower().replace(" ", "_")  # e.g., 'united_states'
        save_dataframe(df, db_path, table_name=table_name, if_exists="replace")
        print(f"Saved table '{table_name}'")

    conn.close()
    print("\nConnection closed.")

    print("\n=== Top 5 Genres per Country ===")
    print(top_genres_per_country(top_50_by_country))

    print("\n=== Most Popular Genre per Country ===")
    print(number_one_genre_per_country(top_50_by_country))

    print("\n=== Artist Country Counts ===")
    artist_counts = artist_country_counts(top_50_by_country)
    print(artist_counts.head())

    print("\n=== Artist Classification (Global/Regional/Local) ===")
    classified = classify_artists(artist_counts)
    print(classified.head())

    print("\n=== Most Popular Artist per Country ===")
    print(most_popular_artist_per_country(top_50_by_country))
    







