class MusicAnalzyer:
    """Handles loading, validating, and slicing of Spotify Top 50 data."""
    """The functions that will be in this class:
    
   __init__(dataframe: pd.DataFrame)

    get_top_50_songs_by_countries(country_list: list[str]) -> dict

    top_genres_per_country(top_50_by_country: dict) -> pd.DataFrame

    number_one_genre_per_country(top_50_by_country: dict) -> pd.DataFrame

    artist_country_counts(top_50_by_country: dict) -> pd.DataFrame

    most_popular_artist_per_country(top_50_by_country: dict) -> pd.DataFrame
    
    
    
    """