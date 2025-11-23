"""
Music System Demonstration

This script demonstrates all Project 3 requirements:
- Inheritance hierarchies
- Polymorphic behavior
- Abstract base classes
- Composition relationships
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from base_class import MusicItem
from song_item import SongItem
from artist_item import ArtistItem


def demonstrate_inheritance():
    """Demonstrate inheritance hierarchy."""
    print("=" * 60)
    print("INHERITANCE DEMONSTRATION")
    print("=" * 60)
    
    # Create SongItem and ArtistItem
    song = SongItem("Blinding Lights", "The Weeknd", "Pop", "USA", 1)
    artist = ArtistItem("The Weeknd", songs=[song])
    
    print(f"\nCreated SongItem and ArtistItem:")
    print(f"  - {song.describe()} (SongItem)")
    print(f"  - {artist.describe()} (ArtistItem)")
    
    print(f"\nBoth inherit from MusicItem:")
    print(f"  - SongItem is MusicItem: {isinstance(song, MusicItem)}")
    print(f"  - ArtistItem is MusicItem: {isinstance(artist, MusicItem)}")


def demonstrate_polymorphism():
    """Demonstrate polymorphic behavior."""
    print("\n" + "=" * 60)
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    song1 = SongItem("Levitating", "Dua Lipa", "Pop", "UK", 2)
    song2 = SongItem("Save Your Tears", "The Weeknd", "Pop", "USA", 3)
    artist1 = ArtistItem("Dua Lipa", songs=[song1])
    artist2 = ArtistItem("The Weeknd", songs=[song2])
    
    music_items = [song1, song2, artist1, artist2]
    
    print("\nCalling describe() on all MusicItems (polymorphic):")
    for item in music_items:
        print(f"  {item.describe()}")


def demonstrate_abstract_base_class():
    """Demonstrate abstract base class usage."""
    print("\n" + "=" * 60)
    print("ABSTRACT BASE CLASS DEMONSTRATION")
    print("=" * 60)
    
    print("\nMusicItem is abstract and cannot be instantiated directly.")
    print("  Attempting to instantiate would raise TypeError (commented out).")
    # MusicItem("Some Title")  # Would raise TypeError
    
    song = SongItem("Anti-Hero", "Taylor Swift", "Pop", "USA", 4)
    artist = ArtistItem("Taylor Swift", songs=[song])
    
    print(f"\nConcrete subclasses implement describe():")
    print(f"  - SongItem: {song.describe()}")
    print(f"  - ArtistItem: {artist.describe()}")


def demonstrate_composition():
    """Demonstrate composition relationships."""
    print("\n" + "=" * 60)
    print("COMPOSITION DEMONSTRATION")
    print("=" * 60)
    
    print("\nArtistItem 'has-a' collection of SongItems.")
    song1 = SongItem("Song A", "Artist X", "Rock", "USA", 1)
    song2 = SongItem("Song B", "Artist X", "Rock", "USA", 2)
    
    artist = ArtistItem("Artist X", songs=[song1, song2])
    print(f"  Artist {artist.artist_name} has {len(artist.songs)} songs:")
    for s in artist.songs:
        print(f"    - {s.describe()}")
    
    print("\nYou can add more songs dynamically:")
    song3 = SongItem("Song C", "Artist X", "Rock", "USA", 3)
    artist.songs.append(song3)
    print(f"  Artist now has {len(artist.songs)} songs:")
    for s in artist.songs:
        print(f"    - {s.describe()}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 60)
    print("MUSIC SYSTEM - PROJECT 3 DEMONSTRATION")
    print("Object-Oriented Programming with Inheritance & Polymorphism")
    print("=" * 60)
    
    demonstrate_inheritance()
    demonstrate_polymorphism()
    demonstrate_abstract_base_class()
    demonstrate_composition()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThis system demonstrates:")
    print("  ✓ Inheritance hierarchies (SongItem and ArtistItem)")
    print("  ✓ Polymorphic behavior (describe() works for both subclasses)")
    print("  ✓ Abstract base class (MusicItem enforces interface)")
    print("  ✓ Composition relationships (ArtistItem has SongItems)")
    print("  ✓ Dynamic interaction between objects")


if __name__ == "__main__":
    main()
