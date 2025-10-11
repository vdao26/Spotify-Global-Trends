Spotify Global Trends Analysis- Function Library
Course: INST326: Object-Oriented Programming for Information Science
Section: 0203
Team: Information Retrieval
Team Members: Vivian Dao, Fatimah Shaw, Christiana Crabbe, Vince Baluis

## Project Overview
This function library will contain different functions that will retrieve data from a csv file and extract track metadata, 
clean and normalize the data, write queries using SQLite in Python to compare music genres, artists, and popularity, 
and show our findings by displaying top genres in each country and which artists are global vs. local.  

The Problem
-Spotify tends only to recommend familiar artists and genres to listeners
-There is a lack of exposure for local and regional artists worldwide

Dataset we will use - https://www.kaggle.com/datasets/yelexa/spotify200

## Installation and Setup
1. Clone this repository:
  ```bash
   git clone https://github.com/your-username/Spotify-Global-Trends.git
   cd Spotify-Global-Trends
  ```
2. No external dependancies required - uses Python standard library

3. Download CSV file to Google Drive

This project requires a CSV file of Spotify Top 50 tracks from 5 countries. To use it, upload your CSV to Google Drive and copy its file ID from the shareable link. 
In the script, set the file_id variable to your file’s ID. When you run the program, it will automatically download the CSV 
to src/universal_top_spotify_songs.csv (or a folder you choose). If the file already exists locally, it will use the existing copy.

## Function Library Overview
There are 10 different functions implemented in this library organized into 5 categories:

###Data Loading
-'download_csv_from_drive()' - Downloads CSV from Google Drive if not already present.

###SQLite Database Functions
-'create_database()' – creates new SQLite database and returns a connection and cursor
-'connect_db()' – connects to an existing databasefile
-'insert_csv_to_db()' - Reads CSV and inserts rows into the tracks table.

###Filtering
-'get_top50_per_country()' - Retrieve only the Top 50 songs per country

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


