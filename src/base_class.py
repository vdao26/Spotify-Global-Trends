from abc import ABC, abstractmethod

class MusicItem(ABC):
    """Abstract base class for music-related items."""

    @abstractmethod
    def describe(self) -> str:
        """Return a string description of the item."""
        pass
