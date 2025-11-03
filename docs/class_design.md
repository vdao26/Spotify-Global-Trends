## Architecture documentation

# Integrated Architecture — CSVManager, DataCleaner, MusicAnalyzer, and DatabaseManager

## 1. System Overview

This architecture integrates four modular classes — `CSVManager`, `DataCleaner`, `MusicAnalyzer`, and `DatabaseManager` — to build a data processing and analysis pipeline for Spotify’s top tracks dataset. Each class handles a specific stage of the data lifecycle, from loading raw CSV files to analyzing and storing results in an SQLite database.

---

## 2. Component Roles

| Class               | Responsibility                                                                                                                          |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **CSVManager**      | Handles loading and validation of CSV datasets. Ensures that required columns exist and manages access to the pandas DataFrame.         |
| **DataCleaner**     | Cleans and preprocesses the dataset (e.g., removes duplicates, trims whitespace). Ensures data consistency before analysis.             |
| **MusicAnalyzer**   | Performs analysis operations such as counting tracks, grouping by genre, or identifying top artists per country.                        |
| **DatabaseManager** | Manages SQLite database connections and handles persistence of processed DataFrames. Provides SQL query and table management utilities. |

---

## 3. Class Relationships and Data Flow

### **Data Flow Overview**

1. **CSVManager** loads the dataset from a CSV file → produces a `pandas.DataFrame`.
2. **DataCleaner** receives the DataFrame → cleans data inconsistencies → returns a refined DataFrame.
3. **MusicAnalyzer** performs analytical operations on the cleaned DataFrame.
4. **DatabaseManager** stores the results and enables querying for insights or persistence.

### **Interaction Diagram**

```
                   ┌──────────────────────────────┐
                   │         CSVManager           │
                   ├──────────────────────────────┤
                   │ + load_and_validate_csv()    │
                   │ + count_tracks()             │
                   └──────────────┬───────────────┘
                                  │ DataFrame
                                  ▼
                   ┌──────────────────────────────┐
                   │         DataCleaner          │
                   ├──────────────────────────────┤
                   │ + clean_titles()             |   
                   │ + remove_duplicates()        |
                   | + standardize_genres()       |
                   | + remove_duplicates()        |
                   | + fix_empty_genres()         |
                   | + clean_all()                |
                   └──────────────┬───────────────┘
                                  │ Cleaned DataFrame
                                  ▼
                   ┌──────────────────────────────┐
                   │        MusicAnalyzer         │
                   ├──────────────────────────────┤
                   │ + analyze_genres()           │
                   │ + count_artists()            │
                   │ + top_tracks_by_country()    │
                   └──────────────┬───────────────┘
                                  │ Analytical Results (DataFrames)
                                  ▼
                   ┌──────────────────────────────┐
                   │       DatabaseManager        │
                   ├──────────────────────────────┤
                   │ + connect()                  │
                   │ + save_dataframe()           │
                   │ + fetch_table()              │
                   │ + execute_query()            |
                   └──────────────┬───────────────┘
                                  │
                                  ▼
                           ┌───────────────┐
                           │ SQLite DB     │
                           │ (Data Storage)│
                           └───────────────┘
```

---

## 4. Data Flow Summary

1. **CSV Loading** → `CSVManager` loads validated CSV into a DataFrame.
2. **Cleaning** → `DataCleaner` refines the data by removing duplicates and correcting formatting.
3. **Analysis** → `MusicAnalyzer` extracts insights (genre distributions, top artists, etc.).
4. **Persistence** → `DatabaseManager` saves results into a database for future queries or dashboards.

---

## 5. Integration Notes

* Each class operates independently but exchanges data through pandas DataFrames.
* The pipeline is modular — individual classes can be tested or replaced without impacting others.
* `DatabaseManager` serves as the endpoint for storage, while `CSVManager` acts as the entry point.

---

## 6. Example Workflow

```python
# Step 1: Load data
csv_manager = CSVManager("SpotifyTopSongsByCountry.csv")
df = csv_manager.load_and_validate_csv()

# Step 2: Clean data
cleaner = DataCleaner(df)
cleaned_df = cleaner.remove_duplicates()

# Step 3: Analyze data
analyzer = MusicAnalyzer(cleaned_df)
top_genres = analyzer.top_genres_per_country()

# Step 4: Store results
from database_manager import DatabaseManager
db = DatabaseManager("data/spotify_tracks.db")
db.connect()
db.save_dataframe(top_genres, table_name="top_genres")
db.close()
```

---
