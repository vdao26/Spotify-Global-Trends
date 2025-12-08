"""
FULL WORKING MUSIC ANALYSIS SYSTEM
==================================
This script ties together all components:

1. Load CSV
2. Validate + clean dataset
3. Store cleaned data in SQLite
4. Analyze the music dataset
5. Create SongItem and ArtistItem object structures
6. Produce meaningful outputs to answer charter questions
"""

import os
import pandas as pd
from CSVManager import CSVManager
from DataCleaner import DataCleaner
from DatabaseManagement import DatabaseManagement
from MusicAnalyzer import MusicAnalyzer
from song_item import SongItem
from artist_item import ArtistItem


class MusicSystem:
    """
    Complete workflow that integrates:
    - CSV loading
    - Cleaning
    - Database saving
    - Analysis
    - Object construction
    """

    def __init__(self, csv_filename: str, db_filename: str = "music_database.db"):
        self.csv_manager = CSVManager(csv_filename)
        self.db_manager = DatabaseManagement(db_filename)
        self.cleaned_df = None
        self.analyzer = None

    def load_and_clean_data(self):
        print("Loading CSV...")
        df = self.csv_manager.load_and_validate_csv()

        if df is None:
            raise RuntimeError("CSV could not be loaded.")

        print("Cleaning CSV data...")
        cleaner = DataCleaner(df)
        self.cleaned_df = cleaner.clean_all()

        print("Cleaning complete.")
        return self.cleaned_df

    def save_to_database(self, table_name="spotify_cleaned"):
        if self.cleaned_df is None:
            raise RuntimeError("Cleaned DataFrame not available.")

        print(f"Saving cleaned data to database table '{table_name}'...")
        self.db_manager.save_dataframe(self.cleaned_df, table_name)
        print("Database save complete.")

    def analyze(self, countries: list[str]):
        if self.cleaned_df is None:
            raise RuntimeError("Dataset not cleaned yet.")

        print("Initializing MusicAnalyzer...")
        self.analyzer = MusicAnalyzer(self.cleaned_df)

        print("Computing top 50 lists...")
        top_50 = self.analyzer.get_top_50_songs_by_countries(countries)

        results = {
            "top_genres": self.analyzer.top_genres_per_country(top_50),
            "number_one_genre": self.analyzer.number_one_genre_per_country(top_50),
            "global_artist_counts": self.analyzer.artist_country_counts(top_50),
            "most_popular_by_country": self.analyzer.most_popular_artist_per_country(top_50)
        }

        return results, top_50

    def create_song_objects(self, df: pd.DataFrame):
        """Convert DataFrame rows into SongItem objects."""
        songs = []
        for _, row in df.iterrows():
            song = SongItem(
                title=row["Title"],
                artist=row["Artists"],
                genre=row["Genre"],
                country=row["Country"],
                rank=row["Rank"]
            )
            songs.append(song)
        return songs

    def create_artist_objects(self, df: pd.DataFrame):
        """Group songs by artist into ArtistItem objects."""
        artist_groups = df.groupby("Artists")
        artists = []

        for artist_name, group in artist_groups:
            song_objects = self.create_song_objects(group)
            artist_item = ArtistItem(artist_name, song_objects)
            artists.append(artist_item)

        return artists

    def run(self, countries: list[str]):
        print("=== Part 1: Load and Clean ===")
        cleaned = self.load_and_clean_data()

        print("\n=== Part 2: Save to Database ===")
        self.save_to_database()

        print("\n=== Part 3: Analyze ===")
        analysis_results, top_50 = self.analyze(countries)

        print("\n=== Part 4: Generate Objects ===")
        artist_objects = self.create_artist_objects(cleaned)

        print("\n=== System Workflow Complete ===")

        return analysis_results, artist_objects, top_50

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = "SpotifyTopSongsByCountry - May 2020.csv"
    csv_path = os.path.join(script_dir, csv_file)

    system = MusicSystem(csv_path)

    countries_to_analyze = ["Spain", "United States", "Japan", "South Africa"]

    analysis, artists, top_50_data = system.run(countries_to_analyze)

    print("\n===== Top 5 Genres Per Country =====")
    print(analysis["top_genres"])

    print("\n===== Top Genre Per Country =====")
    print(analysis["number_one_genre"])

    print("\n===== Most Common Artist Globally =====")
    print(analysis["global_artist_counts"])

    print("\n===== Most Popular Artist Per Country =====")
    print(analysis["most_popular_by_country"])

    print("\n===== Sample Artist Objects =====")
    for a in artists[:3]:
        print(a.describe())
