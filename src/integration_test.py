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
    csv_manager = CSVManager("SpotifyTopSongs - May 2020.csv")
    df csv_manager.load_and_validate_csv()
    self.assertTrue(df is not None)
    self.assertTrue(type(df)== pd.DataFrame)
    self.assertGreater(len(df), 0)
    self.assertTrue("Title" in df.columns)
    self.assertTrue("Artists" in df.columns)
    self.assertTrue("Genre" in df.columns)
    data_cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_all()
    self.assertTrue(type(cleaned_df)==pd.DataFrame)
    self.assertTrue(len(cleaned) > 0)
    self.assertTrue("Title" in cleaned_df.columns)
    self.assertTrue("Genre" in cleaned_df.columns)
