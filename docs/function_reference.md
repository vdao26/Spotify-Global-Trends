## Function Library Overview
There are 8 different functions implemented in this library organized into 4 categories:

###Data Loading
-'get_top_50_songs_by_countries()' - Reads a CSV file and returns the top 50 songs for each country.

###SQLite Database Functions
-'create_and_connect_db()' – creates new SQLite database and returns a connection and cursor
-'save_dataframe_to_sqlite()' - Saves a pandas DataFrame into an SQLite database

###Query and Analysis
-'top_genres_per_country()' - finds which genres appears most in each country's Top 50
-'number_one_genre_per_country()' - #1 genre per country from query results
-'artist_country_counts()' - count how many countries each artist appears
-'classify_artists()' - categorizes artists as global, regional, or local 

###Display/Reporting
-'how_artist_findings()' - displays artist classifications
