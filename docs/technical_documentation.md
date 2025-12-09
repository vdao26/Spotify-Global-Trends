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

## Design Choices

## API or Interface Descriptions

## Known Limitations or Future Enhancements
