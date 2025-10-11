## Function Library Overview
There are 12 different functions implemented in this library organized into 5 categories:

###Data Loading
-'load_csv()' – reads the csv file containing Spotify Top 50 tracks per country.
-'extract_metadata() – extract the columns needed in dataset

###Data Cleaning and Filtering
-'clean_data()' – removes duplicates, handles missing values, and formats text
-'filter_top_fifty() - filters top 50 songs in each country 

###SQLite Database Functions
-'create_database()' – creates new SQLite database and returns a connection and cursor
-'insert_data()' – inserts cleaned data into the tracks table
-'connect_db()' – connects to an existing databasefile

###Query and Analysis
-'top_genres_per_country()' - finds which genres appears most in each country's Top 50
-'number_one_genre_per_country()' - #1 genre per country from query results
-'artist_country_counts()' - count how many countries each artist appears
-'classify_artists()' - categorizes artists as global, regional, or local 

###Display/Reporting
-'how_artist_findings()' - displays artist classifications

