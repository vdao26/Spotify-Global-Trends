import unittest
from abc import ABC
import pandas as pd
import os

from CSVManager import CSVManager
from DataCleaner import DataCleaner
from DatabaseManagement import DatabaseManagement
from MusicAnalyzer import MusicAnalyzer

from base_class import MusicItem
from song_item import SongItem
from artist_item import ArtistItem

CSV_FILE = "test_minimal.csv"  # This will be created in src/

CSV_DATA = pd.DataFrame({
    "Country": ["USA", "UK"],
    "Rank": [1, 2],
    "Title": ["Blinding Lights", "Levitating"],
    "Artists": ["The Weeknd", "Dua Lipa"],
    "Genre": ["Pop", "Pop"]
})


def df_to_songitems(df: pd.DataFrame):
    """
    Convert a DataFrame with Spotify songs into a list of SongItem objects.

    Args:
        df (pd.DataFrame): Must have columns ['Title','Artists','Genre','Country','Rank']

    Returns:
        List[SongItem]: SongItem instances
    """
    song_items = []
    for _, row in df.iterrows():
        song = SongItem(
            title=row['Title'],
            artist=row['Artists'],
            genre=row['Genre'],
            country=row['Country'],
            rank=int(row['Rank'])
        )
        song_items.append(song)
    return song_items


class TestMusicSystem(unittest.TestCase):

    # ---------------------------------------------------------
    # setUp() — Prepare sample CSV data as SongItem objects
    # ---------------------------------------------------------
    def setUp(self):
        # Minimal realistic CSV data
        data = {
            "Country": ["USA", "UK"],
            "Rank": [1, 2],
            "Title": ["Blinding Lights", "Levitating"],
            "Artists": ["The Weeknd", "Dua Lipa"],
            "Genre": ["Pop", "Pop"]
        }
        self.df = pd.DataFrame(data)

        # Convert DataFrame rows to SongItem objects
        self.song_items = df_to_songitems(self.df)

        # Create ArtistItem instances with SongItems (composition)
        self.artist_weeknd = ArtistItem("The Weeknd", [self.song_items[0]])
        self.artist_dualipa = ArtistItem("Dua Lipa", [self.song_items[1]])

    # ---------------------------------------------------------
    # 1. ABSTRACT CLASS TESTS
    # ---------------------------------------------------------
    def test_music_item_is_abstract(self):
        self.assertTrue(issubclass(MusicItem, ABC))

    def test_cannot_instantiate_music_item(self):
        with self.assertRaises(TypeError):
            MusicItem()

    # ---------------------------------------------------------
    # 2. INHERITANCE TESTS
    # ---------------------------------------------------------
    def test_subclasses_inherit_from_music_item(self):
        self.assertTrue(issubclass(SongItem, MusicItem))
        self.assertTrue(issubclass(ArtistItem, MusicItem))

    def test_super_called_in_constructor(self):
        s = self.song_items[0]
        a = self.artist_weeknd

        self.assertEqual(s.title, "Blinding Lights")
        self.assertEqual(a.artist_name, "The Weeknd")

    # ---------------------------------------------------------
    # 3. COMPOSITION TESTS — ArtistItem HAS SongItems
    # ---------------------------------------------------------
    def test_artist_stores_songitems(self):
        artist = ArtistItem("Adele", [])
        s1 = SongItem("Hello", "Adele", "Pop", "UK", 1)
        s2 = SongItem("Easy On Me", "Adele", "Pop", "UK", 2)
        artist.songs.append(s1)
        artist.songs.append(s2)

        self.assertEqual(len(artist.songs), 2)
        self.assertIn(s1, artist.songs)
        self.assertIn(s2, artist.songs)

    def test_artist_is_not_subclass_of_songitem(self):
        self.assertFalse(issubclass(ArtistItem, SongItem))

    # ---------------------------------------------------------
    # 4. POLYMORPHIC DESCRIBE METHOD TESTS
    # ---------------------------------------------------------
    def test_songitem_describe(self):
        song = self.song_items[1]  # Levitating
        desc = song.describe()
        self.assertIn("Levitating", desc)
        self.assertIn("Dua Lipa", desc)
        self.assertIn("Pop", desc)
        self.assertIn("UK", desc)
        self.assertIn("2", desc)

    def test_artistitem_describe(self):
        artist = self.artist_dualipa
        desc = artist.describe()
        self.assertIn("Dua Lipa", desc)
        self.assertIn("1", desc)  # has 1 song

        # Add another song and check count
        new_song = SongItem("Don't Start Now", "Dua Lipa", "Pop", "UK", 3)
        artist.songs.append(new_song)
        desc2 = artist.describe()
        self.assertIn("2", desc2)  # now 2 songs
        
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
