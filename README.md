Spotify Global Trends Analysis- Function Library
Course: INST326: Object-Oriented Programming for Information Science
Section: 0203
Team: Information Retrieval
Team Members: Vivian Dao, Fatimah Shaw, Christiana Crabbe, Vince Baluis

## Project Overview
This function library will contain different functions that will retrieve data from a csv file and display track metadata using
Pandas, then take the DataFrame and create a SQLite database to write queries to compare music genres and artists. At the end,
we would display our findings about the genres and artists in the specified countries.   

This project requires a CSV file of Spotify Top 50 tracks from 4 countries(United States, Spain, Japan and South Africa). 
To do this, we used the data from the CSV file from Kaggle and limited it down to 4 countries and manually added the genre
column to do our analysis later. 

## The Problem
-Spotify tends only to recommend familiar artists and genres to listeners
-There is a lack of exposure for local and regional artists worldwide

Dataset we will use - https://www.kaggle.com/datasets/hkapoor/spotify-top-songs-by-country-may-2020

Our modified dataset - https://docs.google.com/spreadsheets/d/1K5LMb4e_-agQOSFF0RQRsvdBij60LD8Kj23rOJNDJbs/edit?gid=777437364#gid=777437364

## Installation and Setup
1. Clone this repository:
  ```bash
   git clone https://github.com/your-username/Spotify-Global-Trends.git
   cd Spotify-Global-Trends
  ```
2. One external dependency required - pandas

3. Download csv file mentioned in the README


## Function Library Overview
There are 15 different functions implemented in this library organized into 4 categories:

### Data Loading
- 'get_top_50_songs_by_countries()': Reads a CSV file and returns the top 50 songs for each country.
- 'load_and_validate_csv()': Loads CSV and validates required columns.

### Organization
- 'organize_track_title()': cleans each track title by removing extra spaces and characters thaat are not letters or numbers
- 'count_tracks()' - counts the number of tracks (songs) that are present in the dataset.
- 'filter_country()' - filters the dataset by returning rows for a specific country.
- 'delete_repeated_tracks()' - remove tracks that appear more than once based on both title and artist(s)
- 'standardized_genre_names()' - standardize the name of each genre for consistency
- 'fix_empty_genres()' - replace empty genre columns with "Genre Unknown" so that there are no empty spaces.

### SQLite Database Functions
-'create_and_connect_db()' – creates new SQLite database and returns a connection and cursor
-'save_dataframe_to_sqlite()' - Saves a pandas DataFrame into an SQLite database

### Query and Analysis
-'top_genres_per_country()' - finds which genres appears most in each country's Top 50
-'number_one_genre_per_country()' - #1 genre per country from query results
-'artist_country_counts()' - count how many countries each artist appears
-'classify_artists()' - categorizes artists as global, regional, or local 
-'most_popular_artist_per_country()' - finds the most popular artist per country


**Class Documentation**
-CSVManager: A class for managing, validating, and summarizing Spotify Top 50 CSV data.
   Methods:
        load_and_validate_csv() -> pd.DataFrame:
            Loads and validates the CSV file, ensuring it contains all required columns.
        count_tracks() -> int:
            Counts the number of tracks (rows) in the dataset. Automatically loads
            the file if it hasn’t been loaded yet.
        __str__():
            Returns a readable summary of the current CSVManager state.
        __repr__():
            Returns a detailed developer-friendly string representation.
-DataCleaner: 
-MusicAnalyzer: This class provides methods to extract, summarize, and compare top songs, 
genres, and artists across multiple countries.
Methods:
        get_top_50_songs_by_countries(country_list: list[str]) -> dict:
            Returns the top 50 ranked songs for each country in the given list.

        top_genres_per_country(top_50_by_country: dict) -> pd.DataFrame:
            Calculates the top 5 most frequent genres for each country.

        number_one_genre_per_country(top_50_by_country: dict) -> pd.DataFrame:
            Identifies the single most popular genre in each country's Top 50 list.

        artist_country_counts(top_50_by_country: dict) -> pd.DataFrame:
            Counts the number of different countries each artist appears in.

        most_popular_artist_per_country(top_50_by_country: dict) -> pd.DataFrame:
            Determines the most frequently appearing artist in each country's Top 50.

        __str__():
            Returns a readable summary of the MusicAnalyzer instance.

        __repr__():
            Returns a detailed string representation for debugging purposes.

## Team Member Contributions
**Vivian Dao** 
- SQLite Database functions
- Focused on getting the pandas DataFrame into SQLite to write queries
- Built the structure of the function_reference
- Worked on the CSVManager class

**Vince Baluis**
- Uploaded the current .csv file to GitHub
- Created the function to read the .csv file
- Created the analysis segment of the functions
- Worked on the MusicAnalyzer class

**Fatimah Shaw**
- Organization functions
- Filtered the dataset

**Christiana Crabbe**
-Modified the csv.file to fit our requirements
-Created and tested the demo script

## Code Review Process
All functions have been reviewed by at least one other team member:
- Pull request reviews documented in GitHub
- Code quality standards enforced consistently
- Documentation reviewed for clarity and completeness
- Function signatures standardized across the library



## AI Collaboration Documentation

**Team members used AI assistance for:** 
- Initial function structure generation
- Docstring formatting and examples
- Algorithm optimization suggestions
- Error handling pattern recommendations

All AI-generated code was thoroughly reviewed, tested, and modified to meet project requirements. Individual AI collaboration details documented in personal repositories

## Repository Structure

```
Spotify-Global-Trends/
├── README.md
├── src/
│   ├── CSVManager.py 
|   |–– DatabaseManagement.py
|   |–– DataCleaner.py
|   |–– MusicAnalyzer.py
│   ├── Spotify_Top_Tracks_Queries.db 
|   |–– SpotifyTopSongsByCountry - May 2020.csv
|   |–– spotify_retrieval_functions.py
├── docs/
|   |–– api_reference.md
|   |–– class_design.md
│   ├── function_reference.md
├── examples/
|   └── basic_usage.py
│   └── demo_script.py
|   └── Spotify_Top_Tracks_Queries.db
└── requirements.txt
```

---


