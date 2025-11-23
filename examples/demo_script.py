import os
import pandas as pd
import sqlite3
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# demo_script.py
from spotify_retrieval_functions import (
    get_top_50_songs_by_countries,
    save_dataframe,
    connect,
    top_genres_per_country,
    number_one_genre_per_country,
    artist_country_counts,
    classify_artists,
    most_popular_artist_per_country
)

def main():
    # --- Define CSV file and countries ---
    csv_file = "SpotifyTopSongsByCountry - May 2020.csv"
    countries = ["Spain", "South Africa", "Japan", "United States"]

    # --- Get Top 50 songs per country ---
    top_50_by_country = get_top_50_songs_by_countries(csv_file, countries)

    # --- Define database path ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "Spotify_Top_Tracks_Queries.db")

    # --- Create database connection ---
    conn = connect(db_path)
    print(f"Connected to database: {db_path}")

    # --- Save each country's top 50 songs to database ---
    for country, df in top_50_by_country.items():
        table_name = country.lower().replace(" ", "_")  # e.g., 'united_states'
        save_dataframe(df, db_path, table_name=table_name, if_exists="replace")
        print(f"Saved table '{table_name}' with {len(df)} songs")

    conn.close()
    print("Database connection closed.\n")

    # --- Display Analysis ---
    print("=== Top 5 Genres per Country ===")
    print(top_genres_per_country(top_50_by_country))

    print("\n=== Most Popular Genre per Country ===")
    print(number_one_genre_per_country(top_50_by_country))

    print("\n=== Artist Country Counts ===")
    artist_counts = artist_country_counts(top_50_by_country)
    print(artist_counts.head(10))

    print("\n=== Artist Classification (Global/Regional/Local) ===")
    classified = classify_artists(artist_counts)
    print(classified.head(10))

    print("\n=== Most Popular Artist per Country ===")
    print(most_popular_artist_per_country(top_50_by_country))


if __name__ == "__main__":
    main()
