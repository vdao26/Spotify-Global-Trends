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

##The Problem
-Spotify tends only to recommend familiar artists and genres to listeners
-There is a lack of exposure for local and regional artists worldwide

Dataset we will use - https://www.kaggle.com/datasets/hkapoor/spotify-top-songs-by-country-may-2020
Our modified dataset - 

## Installation and Setup
1. Clone this repository:
  ```bash
   git clone https://github.com/your-username/Spotify-Global-Trends.git
   cd Spotify-Global-Trends
  ```
2. One external dependency required - pandas

3. Download csv file mentioned in the README


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

##Team Member Contributions
**Vivian Dao** - 

##Code Review Process
All functions have been reviewed by at least one other team member:
- Pull request reviews documented in GitHub
- Code quality standards enforced consistently
- Documentation reviewed for clarity and completeness
- Function signatures standardized across the library

## AI Collaboration Documentation

Team members used AI assistance for:
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
│   ├── spotify_retrieval_functions
│   ├── 
│   └── utils.py
├── docs/
│   ├── function_reference.md
├── examples/
│   └── demo_script.py
└── requirements.txt
```

---


