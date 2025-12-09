import unittest
import os
import pandas as pd
from CSVManager import CSVManager
from DataCleaner import DataCleaner
from DatabaseManagement import DatabaseManagement
from MusicAnalyzer import MusicAnalyzer
from artist_item import ArtistItem
from song_item import SongItem

class TestIntegration(unittest.TestCase):

  def test_csvmanager_in_datacleaner(self):
    csv_manager = CSVManager("SpotifyTopSongsByCountry - May 2020.csv")
    df = csv_manager.load_and_validate_csv()
    self.assertIsNotNone(df)
    self.assertTrue(type(df) == pd.DataFrame)
    self.assertGreater(len(df), 0)
    self.assertTrue("Title" in df.columns)
    self.assertTrue("Artists" in df.columns)
    self.assertTrue("Genre" in df.columns)
    data_cleaner = DataCleaner(df)
    cleaned_df = data_cleaner.clean_all()
    self.assertTrue(type(cleaned_df)==pd.DataFrame)
    self.assertTrue(len(cleaned_df) > 0)
    self.assertTrue("Title" in cleaned_df.columns)
    self.assertTrue("Genre" in cleaned_df.columns)
    self.assertTrue("Artists" in cleaned_df.columns)

def test_datacleaner_in_databasemanagement(self):
  df = pd.DataFrame({"Country": ["United States", "United States"], "Rank": [1, 2], "Title": ["  Tester", "testsong"], "Artists": ["Artistname", "Artistname"], "Genre": ["pop", ""]})
  data_cleaner = DataCleaner(df)
  cleaned_df = data_cleaner.clean_all()

  test_database = "test_spotify.db"
  if os.path.exists(test_database):
      os.remove(test_database)
  database = DatabaseManagement(test_database)
  database.save_dataframe(cleaned_df, "sample_data")

  test_data = database.list_tables()
  self.assertIn("sample_data", test_data)
  database.close()
  if os.path.exists(test_database):
      os.remove(test_database)
def test_cleaned_data_in_musicanalyzer(self):
  csv_manager = CSVManager("SpotifyTopSongsByCountry - May 2020.csv")
  df = csv_manager.load_and_validate_csv()
  self.assertFalse(df is None)
  self.asserTrue(isinstance(df, pd.DataFrame))
  self.assertTrue(len(df) != 0)
  data_cleaner = DataCleaner)df)
  cleaned_df = data_cleaner.clean_all()
  self.assertTrue(isinstance(cleaned_df, pd.DataFrame))
  self.assertTrue(len(cleaned_df) > 0)
  music_analyzer = MusicAnalyzer(cleaned_df)
  countries = ["United Staes", "Mexico"]
  top_50_songs = music_analyzer.get_top_50_songs_by_countries(countries)
  self.assertIsInstance(top_50, dict)
  self.assertIn("United States", top_50)
  self.assertIn("Mexico", top_50)
  self.assertEqual(type(top_50["Mexico]), pd.DataFrame)
  self.assertFalse(top_50["Mexico"].empty)

  genres_df = music_analyzer.top_genres_per_country(top_50)
  self.assertEqual(type(genres_df), pd.DataFrame)
  self.assertFalse(genres_df.empty)
  self.assertIn("Country", genres_df.columns)
  self.assertIn("Genre", genres_df.columns)
                  
                                 
