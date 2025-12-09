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
  
                  
                                 
