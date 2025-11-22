from base_class import MusicItem
from song_item import SongItem

class ArtistItem(MusicItem):
    """Represents an artist and their songs (composition: has-a relationship)."""

    def __init__(self, artist_name, songs: list[SongItem]):
        self.artist_name = artist_name
        self.songs = songs  # composition

    def describe(self):
        return f"Artist: {self.artist_name}, Songs in dataset: {len(self.songs)}"
