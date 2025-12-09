# Technical Documentation

## Architecture Overview and Design Decisions

### Overview
This project is a Python-based function library that analyzes global music trends using Spotify chart data. It reads a CSV file of Spotify Top 50 tracks, uses Pandas to clean and explore the data, and then loads the results into a SQLite database for deeper analysis. From there, we run SQL queries to compare music genres and artists across different countries and summarize our findings.

The dataset is based on Spotify Top 50 tracks from four countries: the United States, Spain, Japan, and South Africa. We started from a Kaggle CSV file, filtered it down to these four countries, and manually added a **genre** column to support genre-based analysis later on.

This system is designed to:

- Handle inconsistent or messy CSV data using Pandas and data-cleaning functions  
- Highlight trends and artists that might be overlooked in global, combined rankings  
- Help artists or analysts see where certain genres or artists perform strongly and where there may be opportunities to expand their audience

### Architecture

1. **Data Ingestion (CSV -> Pandas)**
   - `CSVManager` reads the Spotify Top 50 CSV file.
   - The raw dataset is filtered down to the four target countries.
   - Basic validation is performed to ensure the file is present and in the expected structure.
   - Output: a raw Pandas DataFrame.

2. **Data Cleaning (Pandas -> Clean DataFrame)**
   - `DataCleaner` removes duplicates and fixes formatting issues (e.g., trimming whitespace, normalizing strings).
   - Handles missing or inconsistent values where possible.
   - Uses the manually added **genre** column to prepare the data for genre-based analysis.
   - Output: a cleaned Pandas DataFrame suitable for analysis and storage.

3. **Persistence Layer (DataFrame -> SQLite)**
   - `DatabaseManagement` takes the cleaned DataFrame and writes it into a SQLite database.
   - Creates or initializes tables and manages the database schema.
   - Centralizes SQL operations (e.g., inserts, table creation) using `sqlite3`.
   - Output: a SQLite database file with the structured track data.

4. **Analysis and Reporting (SQLite -> Insights)**
   - `MusicAnalyzer` runs analysis on genres, artists, and countries.
   - Can operate directly on DataFrames or query the SQLite database via `DatabaseManagement`.
   - Generates results such as:
     - Top genres per country
     - Most frequent artists per country or genre
     - Cross-country comparisons for specific genres or artists
   - Output: analysis DataFrames and printed or displayed summaries.
     
## Key Design Choices and Rationale

- **Pandas for initial data handling**  
  We use Pandas for CSV loading and cleaning because it provides powerful tools for dealing with inconsistent or messy data, which is common in real-world CSV files.

- **SQLite as a lightweight database**  
  SQLite allows us to use database concepts and run SQL queries without setting up a full database server. It is file-based, portable.

- **Separation of concerns via service classes**  
  Splitting responsibilities across `CSVManager`, `DataCleaner`, `MusicAnalyzer`, and `DatabaseManagement` makes the code easier to maintain, test, and extend. Each class has a clear, focused role.

- **Object-oriented design with `MusicItem` hierarchy**  
  Using an abstract base class and polymorphism lets us treat different music concepts uniformly while still capturing their differences. This makes future extensions (e.g., new item types) smoother.

## API or Interface Descriptions

1. Use `CSVManager` to load the CSV into a raw DataFrame.
2. Pass the DataFrame to `DataCleaner` to get a cleaned DataFrame.
3. Use `DatabaseManagement` to write the cleaned data into SQLite.
4. Use `MusicAnalyzer` to:
   - Run analysis directly on the DataFrame, or
   - Query the SQLite database and analyze those results.

## Known Limitations or Future Enhancements


**Known Limitations**

- The dataset is limited to four countries (United States, Spain, Japan, and South Africa) and one snapshot of Top 50 tracks.
- Genres were manually added, so some genre classifications may be simplified or inconsistent.
- The system does not currently include a user interface; all interactions are via code (functions and scripts).

**Future Enhancements**

- Add support for additional countries and time periods to analyze trends over time, not just one snapshot.
- Enhance genre classification (e.g., mapping to higher-level genre categories or using external metadata).
- Add more advanced analysis methods (e.g., similarity between countries, artist growth over time).

