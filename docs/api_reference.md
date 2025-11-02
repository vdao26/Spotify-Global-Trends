## Class/method reference

This document provides reference information for the 4 classes in the Spotify Global Trends Analysis

## Table of Contents

1. [CSVManager](#csv-manager-class)
2. [DataCleaner](#data-cleaner-class)
3. [MusicAnalyzer](#music-analyzer-class)
4. [DatabaseManagement](#Query-Analysis-functions)

---

## CSV Manager Class

### Description

- The CSVManager class provides functionality for loading, validating, and summarizing Spotify Top 50 CSV data files.
- It ensures proper file handling, column validation, and encapsulated access to loaded data using Python properties.


### Example Usage 
'''python
    # Initialize manager 
    manager = CSVManager("SpotifyTopSongsByCountry.csv") 
    # Load and validate 
    data = manager.load_and_validate_csv() 
    # Get number of songs 
    print(manager.count_tracks()) 
    # Display summary 
    print(manager)

'''

---