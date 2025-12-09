"""
Unit testing - ensures class, method, and functions are working properly.

"""
import unittest
import pandas as pd
import os

from CSVManager import CSVManager
from DataCleaner import DataCleaner
from DatabaseManagement import DatabaseManagement
from MusicAnalyzer import MusicAnalyzer

CSV_FILE = "test_minimal.csv"  # This will be created in src/

CSV_DATA = pd.DataFrame({
    "Country": ["USA", "UK"],
    "Rank": [1, 2],
    "Title": ["Blinding Lights", "Levitating"],
    "Artists": ["The Weeknd", "Dua Lipa"],
    "Genre": ["Pop", "Pop"]
})

#Unit Tests
#---------------- CSVManager Tests ----------------
class TestCSVManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Make sure the CSV file exists where CSVManager expects it
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cls.csv_path = os.path.join(script_dir, CSV_FILE)
        CSV_DATA.to_csv(cls.csv_path, index=False)
        cls.cm = CSVManager(CSV_FILE)

    @classmethod
    def tearDownClass(cls):
        # Remove the CSV after tests
        if os.path.exists(cls.csv_path):
            os.remove(cls.csv_path)

    def test_load_and_validate_csv(self):
        df = self.cm.load_and_validate_csv()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)

    def test_count_tracks(self):
        self.cm.load_and_validate_csv()
        self.assertEqual(self.cm.count_tracks(), 2)


# ---------------- DataCleaner Tests ----------------
class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = DataCleaner(CSV_DATA.copy())

    def test_clean_titles(self):
        df_cleaned = self.cleaner.clean_titles()
        for title in df_cleaned["Title"]:
            self.assertEqual(title, title.strip())

    def test_standardize_genres(self):
        df_cleaned = self.cleaner.standardize_genres()
        self.assertIn("Pop", df_cleaned["Genre"].values)

    def test_remove_duplicates(self):
        # Add a duplicate for testing
        dup_row = CSV_DATA.copy()
        self.cleaner._dataframe = pd.concat([self.cleaner._dataframe, dup_row], ignore_index=True)
        df_cleaned = self.cleaner.remove_duplicates()
        self.assertEqual(len(df_cleaned), 2)

    def test_fix_empty_genres(self):
        self.cleaner._dataframe.loc[0, "Genre"] = ""
        df_fixed = self.cleaner.fix_empty_genres()
        self.assertEqual(df_fixed.loc[0, "Genre"], "Genre Unknown")

    def test_clean_all(self):
        df_cleaned = self.cleaner.clean_all()
        self.assertFalse(df_cleaned["Genre"].isnull().any())
        for title in df_cleaned["Title"]:
            self.assertEqual(title, title.strip())


# ---------------- DatabaseManagement Tests ----------------
class TestDatabaseManagement(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseManagement(":memory:")
        self.df = CSV_DATA.copy()

    def test_save_and_fetch_table(self):
        self.db.save_dataframe(self.df, "spotify_top50")
        self.assertTrue(self.db.table_exists("spotify_top50"))
        fetched_df = self.db.fetch_table("spotify_top50")
        self.assertEqual(len(fetched_df), len(self.df))

    def test_list_and_delete_tables(self):
        self.db.save_dataframe(self.df, "temp_table")
        self.assertIn("temp_table", self.db.list_tables())
        self.db.delete_table("temp_table")
        self.assertNotIn("temp_table", self.db.list_tables())


# ---------------- MusicAnalyzer Tests ----------------
class TestMusicAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = MusicAnalyzer(CSV_DATA.copy())

    def test_top_50_songs_by_countries(self):
        top_50 = self.analyzer.get_top_50_songs_by_countries(["USA", "UK"])
        self.assertIsInstance(top_50, dict)
        self.assertEqual(len(top_50["USA"]), 1)
        self.assertEqual(len(top_50["UK"]), 1)

    def test_top_genres_per_country(self):
        top_50 = self.analyzer.get_top_50_songs_by_countries(["USA", "UK"])
        df_genres = self.analyzer.top_genres_per_country(top_50)
        self.assertIn("Country", df_genres.columns)
        self.assertIn("Genre", df_genres.columns)
        self.assertIn("Count", df_genres.columns)

    def test_number_one_genre_per_country(self):
        top_50 = self.analyzer.get_top_50_songs_by_countries(["USA", "UK"])
        df_top = self.analyzer.number_one_genre_per_country(top_50)
        self.assertIn("Top Genre", df_top.columns)

    def test_artist_country_counts(self):
        top_50 = self.analyzer.get_top_50_songs_by_countries(["USA", "UK"])
        df_artists = self.analyzer.artist_country_counts(top_50)
        self.assertIn("Artist", df_artists.columns)
        self.assertIn("Country Count", df_artists.columns)

    def test_most_popular_artist_per_country(self):
        top_50 = self.analyzer.get_top_50_songs_by_countries(["USA", "UK"])
        df_popular = self.analyzer.most_popular_artist_per_country(top_50)
        self.assertIn("Most Popular Artist", df_popular.columns)
        self.assertIn("Song Count", df_popular.columns)

if __name__ == "__main__":
    unittest.main()