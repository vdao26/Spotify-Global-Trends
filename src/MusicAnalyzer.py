import os
import pandas as pd

class MusicAnalyzer:
    """

    This class provides methods to extract, summarize, and compare top songs,
    genres, and artists across multiple countries.

    Example:
    --------
        >>> df = pd.read_csv("SpotifyTopSongsByCountry - May 2020.csv")
        >>> analyzer = MusicAnalyzer(df)
        >>> top_50 = analyzer.get_top_50_songs_by_countries(["Spain", "United States"])
        >>> analyzer.top_genres_per_country(top_50)
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the MusicAnalyzer with a DataFrame.

        Args:
            dataframe (pd.DataFrame): A pandas DataFrame containing Spotify Top 50 data.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = {'Country', 'Rank', 'Title', 'Artists', 'Genre'}
        if not required_columns.issubset(dataframe.columns):
            raise ValueError(f"DataFrame must contain columns: {required_columns}")
        self._dataframe = dataframe.copy()

    @property
    def dataframe(self):
        """Returns the current working DataFrame."""
        return self._dataframe

    @dataframe.setter
    def dataframe(self, new_df: pd.DataFrame):
        """Allows controlled setting of a new DataFrame."""
        if not isinstance(new_df, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame.")
        self._dataframe = new_df.copy()

    def get_top_50_songs_by_countries(self, country_list: list[str]) -> dict:
        """
        Returns top 50 songs for each country in the given list.

        Args:
            country_list (list[str]): List of country names.

        Returns:
            dict: Country name keys with DataFrame values of top 50 songs.
        """
        results = {}
        for country in country_list:
            country_df = self._dataframe[self._dataframe['Country'].str.lower() == country.lower()].copy()
            country_df = country_df[['Country', 'Rank', 'Title', 'Artists', 'Genre']]
            country_df['Rank'] = pd.to_numeric(country_df['Rank'], errors='coerce')
            results[country] = country_df.sort_values('Rank').head(50)
        return results

    def top_genres_per_country(self, top_50_by_country: dict) -> pd.DataFrame:
        """
        Finds the top 5 most common genres in each country's Top 50 list.
        If a country has fewer than 5 genres, the remaining entries are filled with 'N/A' and count 0.

        Args:
            top_50_by_country (dict): Dictionary with country names and top 50 DataFrames.

        Returns:
            pd.DataFrame: DataFrame with columns ['Country', 'Genre', 'Count'].
        """
        country_genres = []
        for country, df in top_50_by_country.items():
            if 'Genre' in df.columns:
                top_genres = df['Genre'].value_counts().head(5)
                genres_listed = 0
                for genre, count in top_genres.items():
                    country_genres.append({'Country': country, 'Genre': genre, 'Count': count})
                    genres_listed += 1
                # Fill remaining slots if fewer than 5 genres
                while genres_listed < 5:
                    country_genres.append({'Country': country, 'Genre': 'N/A', 'Count': 0})
                    genres_listed += 1
        return pd.DataFrame(country_genres)


    def number_one_genre_per_country(self, top_50_by_country: dict) -> pd.DataFrame:
        """
        Finds the single most popular genre per country.

        Args:
            top_50_by_country (dict): Dictionary with country names and top 50 DataFrames.

        Returns:
            pd.DataFrame: DataFrame with ['Country', 'Top Genre', 'Count'].
        """
        top_genre_list = []
        for country, df in top_50_by_country.items():
            if 'Genre' in df.columns and not df.empty:
                top_genre = df['Genre'].value_counts().idxmax()
                count = df['Genre'].value_counts().max()
                top_genre_list.append({'Country': country, 'Top Genre': top_genre, 'Count': count})
        return pd.DataFrame(top_genre_list)

    def artist_country_counts(self, top_50_by_country: dict) -> pd.DataFrame:
        """
        Counts how many countries each artist appears in across all countries.

        Args:
            top_50_by_country (dict): Dictionary with country names and top 50 DataFrames.

        Returns:
            pd.DataFrame: DataFrame with ['Artist', 'Country Count'].
        """
        from collections import defaultdict

        # Map each artist to the set of countries they appear in
        artist_country_map = defaultdict(set)

        for country, df in top_50_by_country.items():
            if 'Artists' not in df.columns:
                continue
            for artist_list in df['Artists'].dropna():
                # Split by comma and strip whitespace
                artists = [a.strip() for a in artist_list.split(',')]
                for artist in artists:
                    artist_country_map[artist].add(country)

        # Convert to DataFrame
        data = [{'Artist': artist, 'Country Count': len(countries)} 
                for artist, countries in artist_country_map.items()]

        result_df = pd.DataFrame(data).sort_values(
            by=['Country Count', 'Artist'], ascending=[False, True]
        ).reset_index(drop=True)

        return result_df


    def most_popular_artist_per_country(self, top_50_by_country: dict) -> pd.DataFrame:
        """
        Finds the most frequently appearing artist per country.

        Args:
            top_50_by_country (dict): Dictionary with country names and top 50 DataFrames.

        Returns:
            pd.DataFrame: DataFrame with ['Country', 'Most Popular Artist', 'Song Count'].
        """
        popular_artists = []
        for country, df in top_50_by_country.items():
            if 'Artists' not in df.columns or df.empty:
                continue
            artist_series = (
                df['Artists']
                .dropna()
                .apply(lambda x: [a.strip() for a in x.split(',')])
                .explode()
            )
            if artist_series.empty:
                continue
            top_artist = artist_series.value_counts().idxmax()
            count = artist_series.value_counts().max()
            popular_artists.append({'Country': country, 'Most Popular Artist': top_artist, 'Song Count': count})
        return pd.DataFrame(popular_artists)

    def __str__(self):
        """Readable summary of the MusicAnalyzer instance."""
        return f"MusicAnalyzer with {len(self._dataframe)} total records."

    def __repr__(self):
        """Detailed representation for debugging."""
        return f"MusicAnalyzer(dataframe=DataFrame with {len(self._dataframe)} rows)"


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "SpotifyTopSongsByCountry - May 2020.csv")
    csv_path = os.path.normpath(csv_path)

    print(f"Loading CSV from: {csv_path}")  # For debugging

    df = pd.read_csv(csv_path)

    analyzer = MusicAnalyzer(df)
    top_50 = analyzer.get_top_50_songs_by_countries(["Spain", "United States", "Japan", "South Africa"])

    print("\n===== Top 5 Genres Per Country =====")
    print(analyzer.top_genres_per_country(top_50))
    print("\n===== Top Genre Per Country =====")
    print(analyzer.number_one_genre_per_country(top_50))
    print("\n===== Most Common Artist Globally =====")
    print(analyzer.artist_country_counts(top_50).to_string(index = False))
    print("\n===== Most Popular Artist per Country =====")
    print(analyzer.most_popular_artist_per_country(top_50))