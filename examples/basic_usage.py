if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
    import pandas as pd
    from CSVManager import CSVManager
    from DataCleaner import DataCleaner
    from MusicAnalyzer import MusicAnalyzer
    from DatabaseManagement import DatabaseManagement
    
    # --- 1. Load the CSV ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = "SpotifyTopSongsByCountry - May 2020.csv"
    
    csv_manager = CSVManager(csv_filename)
    df = csv_manager.load_and_validate_csv()
    if df is None:
        raise SystemExit("Failed to load CSV data. Exiting program.")
    
    print(f"CSV loaded: {csv_manager.count_tracks()} tracks")

    # --- 2. Clean the dataset ---
    cleaner = DataCleaner(df)
    cleaner.clean_all()
    cleaned_df = cleaner.dataframe
    print(f"Data cleaned: {len(cleaned_df)} rows remain after cleaning")

    # --- 3. Analyze the data ---
    analyzer = MusicAnalyzer(cleaned_df)
    countries = ["Spain", "United States", "Japan", "South Africa"]
    top_50_by_country = analyzer.get_top_50_songs_by_countries(countries)

    def display_with_1_based_index(df: pd.DataFrame):
        df_copy = df.copy().reset_index(drop=True)
        df_copy.index = df_copy.index + 1
        return df_copy

    print("\n===== Top 5 Genres Per Country =====")
    print(display_with_1_based_index(analyzer.top_genres_per_country(top_50_by_country)))

    print("\n===== Top Genre Per Country =====")
    print(display_with_1_based_index(analyzer.number_one_genre_per_country(top_50_by_country)))

    print("\n===== Most Common Artist Globally =====")
    print(display_with_1_based_index(analyzer.artist_country_counts(top_50_by_country)))

    print("\n===== Most Popular Artist Per Country =====")
    print(display_with_1_based_index(analyzer.most_popular_artist_per_country(top_50_by_country)))

    # --- 4. Save results to database ---
    db_filename = "Spotify_Top_Tracks.db"
    db_path = os.path.join(script_dir, db_filename)
    db_manager = DatabaseManagement(db_path)
    
    db_manager.connect()  # Open connection

    # Save top 50 songs per country
    for country, df_country in top_50_by_country.items():
        table_name = country.lower().replace(" ", "_")
        db_manager.save_dataframe(df_country, table_name)
    
    # Save top genres per country
    top_genres_df = analyzer.top_genres_per_country(top_50_by_country)
    db_manager.save_dataframe(top_genres_df, "top_genres_per_country")

    db_manager.close()
    
    print(f"\nData successfully saved to database: {db_filename}")
