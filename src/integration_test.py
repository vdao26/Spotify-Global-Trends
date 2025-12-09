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
  self.assertTrue(isinstance(df, pd.DataFrame))
  self.assertTrue(len(df) != 0)
  data_cleaner = DataCleaner(df)
  cleaned_df = data_cleaner.clean_all()
  self.assertTrue(isinstance(cleaned_df, pd.DataFrame))
  self.assertTrue(len(cleaned_df) > 0)
  music_analyzer = MusicAnalyzer(cleaned_df)
  countries = ["United States", "Mexico"]
  top_50_songs = music_analyzer.get_top_50_songs_by_countries(countries)
  self.assertIsInstance(top_50_songs, dict)
  self.assertIn("United States", top_50_songs)
  self.assertIn("Mexico", top_50_songs)
  self.assertEqual(type(top_50_songs["Mexico"]), pd.DataFrame)
  self.assertFalse(top_50_songs["Mexico"].empty)

  genres_df = music_analyzer.top_genres_per_country(top_50_songs)
  self.assertEqual(type(genres_df), pd.DataFrame)
  self.assertFalse(genres_df.empty)
  self.assertIn("Country", genres_df.columns)
  self.assertIn("Genre", genres_df.columns)

def test_music_analyzer_and_song_and_artist_items(self):
  df = pd.DataFrame({
    "Country": ["United States", "Canada"],
    "Rank": [1, 2],
    "Title": ["Test_song", "Test_song_two"],
    "Artists": ["Sally", "Ned"],
    "Genre": ["pop", "hip-hop"]
  })
  data_cleaner = DataCleaner(df)
  cleaned_df = data_cleaner.clean_all()

  self.assertTrue(isinstance(cleaned_df, pd.DataFrame))
  self.assertTrue(len(cleaned_df) > 0)
  music_analyzer = MusicAnalyzer(cleaned_df)
  countries = ["United States"]
  top_50_songs = music_analyzer.get_top_50_songs_by_countries(countries)

  self.assertEqual(type(top_50_songs), dict)
  self.assertTrue("United States" in top_50_songs)
  tester_df = top_50_songs["United States"]
  self.assertTrue(type(tester_df) == pd.DataFrame)
  self.assertTrue(len(tester_df) != 0)

  songs_list = []
  for i, row in tester_df.iterrows():
      songs_list.append(SongItem(row["Title"], row["Artists"], row["Genre"], row["Country"], row["Rank"]))
  self.assertTrue(len(songs_list) > 0)
  self.assertTrue(isinstance(songs_list[0], SongItem)
  artist = tester_df["Artists"].values[0]
  artist_item = ArtistItem(artist, songs_list)

  self.assertTrue(type(artist_item) is ArtistItem)
  self.assertTrue(artist_item.artist_name == artist)
  self.assertEqual(len(artist_item.songs), len(songs_list))
                            
                  
                          
