import unittest
from abc import ABC
import pandas as pd
import os

from base_class import MusicItem
from song_item import SongItem
from artist_item import ArtistItem



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
        

if __name__ == "__main__":
    unittest.main()
