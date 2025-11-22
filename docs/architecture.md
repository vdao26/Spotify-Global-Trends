## Project 3 Architecture documentation

### Inheritance Hierarchy
```
MusicItem (ABC) <- Abstract Base Class
├── SongItem
└── ArtistItem
```
### Rationale
- `MusicItem` defines a common interface `(describe)` that all music-related objects implement.
- `SongItem` specializes a single track.
- `ArtistItem` specializes an artist summary (composition: has-a relationship with SongItem).

### Polymorphic Methods
- `describe()` is polymorphic: same method call on a MusicItem reference outputs type-specific information.
- Allows generic handling of multiple object types (song, artist, country) in the same workflow.

### Composition vs. Inheritance Decisions
- **Composition used:** ArtistItem contain `SongItem` objects.
- **Reason:** An artist or country is not a song, but they aggregate songs.
- Avoided inheritance because `ArtistItem` is not a type of `SongItem`.

### Design Pattern Usage
- **Factory pattern:** Optional helper function converts `DataFrame` rows into `SongItem` objects.
- **Polymorphism:** `describe()` allows uniform handling of diverse music objects.