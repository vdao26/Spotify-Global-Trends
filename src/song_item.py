from base_class import MusicItem

class SongItem(MusicItem):
    """Represents a single song from the CSV."""

    def __init__(self, title, artist, genre, country, rank):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.country = country
        self.rank = rank

    def describe(self):
        return f"{self.title} by {self.artist} ({self.genre}) [{self.country}] Rank: {self.rank}"