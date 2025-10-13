import os
import pandas as pd
import sqlite3
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from spotify_retrieval_functions import (
    get_top_50_songs_by_countries,
    load_and_validate_csv,
    create_and_connect_db,
    save_dataframe_to_sqlite,
    top_genres_per_country,
    number_one_genre_per_country,
    artist_country_counts,
    classify_artists,
    most_popular_artist_per_country,
    filter_country,
    count_tracks,
    fix_empty_genres
    )

def demo():
    """
    Runs a full demonstration of the Spotify analysis workflow.
    """

    print("=== Step 1: Load and Validate CSV ===")
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'SpotifyTopSongsByCountry - May 2020.csv')

    df = load_and_validate_csv(csv_path)
    if df is None:
        print("CSV could not be loaded or validated. Exiting.")
        return
    print(" CSV successfully loaded and validated.")
    print(f"Total records in CSV: {len(df)}")

    print("\n=== Step 2: Get Top 50 Songs for Selected Countries ===")
    countries = ["Spain", "South Africa", "Japan", "United States"]
    top_50_by_country = get_top_50_songs_by_countries(csv_path, countries)

    for country, top_df in top_50_by_country.items():
        print(f"\n {country}: {count_tracks(top_df)} tracks loaded.")  #  Using count_tracks
        print(top_df.head(3))  # show a preview of the top few rows

    print("\n=== Step 3: Save to SQLite Database ===")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_filename = "Spotify_Top_Tracks_Queries.db"
    conn = create_and_connect_db(os.path.join(script_dir, db_filename))

    for country, df in top_50_by_country.items():
        table_name = country.lower().replace(" ", "_")
        save_dataframe_to_sqlite(df, conn, table_name, if_exists="replace")
        print(f" Saved {country} table to database.")
        
    print("\n=== Step 4: Analytical Insights ===")
    print("\nTop 5 Genres per Country:")
    print(top_genres_per_country(top_50_by_country))

    print("\nMost Popular Genre per Country:")
    print(number_one_genre_per_country(top_50_by_country))

    print("\nArtist Country Counts:")
    artist_counts = artist_country_counts(top_50_by_country)
    print(artist_counts.head())

    print("\nArtist Classification (Global / Regional / Local):")
    classified = classify_artists(artist_counts)
    print(classified.head())

    print("\nMost Popular Artist per Country:")
    print(most_popular_artist_per_country(top_50_by_country))

    print("\n=== Step 5: Utility Function Demonstration ===")
    #  Using filter_country to show only Japan's data
    japan_data = filter_country(df, "Japan")
    print(f"\nFiltered dataset for Japan ({len(japan_data)} records):")
    print(japan_data.head())
    conn.close()
    print("\n Demo complete! Database and analyses successfully generated.")


if __name__ == "__main__":
    demo()