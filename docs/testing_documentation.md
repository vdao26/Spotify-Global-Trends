# Testing Documentation

## Testing Strategy

Our testing strategy combines **unit tests**, **integration tests**, **system tests**, and a **domain-specific test **. All tests are standard `pytest` files:

- `test_unit_test.py`
- `test_integration_test.py`
- `test_system_test.py`
- `test_spotify_global_trends.py`

## Coverage Rationale (What We Test and Why)

We prioritize testing:

- **Data transformations** in `DataCleaner`, since mistakes here can affect every step.
- **File I/O and database operations** (CSV loading and SQLite writes/reads), which are common of runtime errors.
- **Business logic** in `MusicAnalyzer` and domain tests in `test_spotify_global_trends.py`, because they represent the core goals of the project.
- **OOP behavior** in the `MusicItem` hierarchy to ensure polymorphism and abstract class behavior are correct.

We test a mix of:

- **Small, focused unit tests** for reliability and easy debugging.
- **Integration/system tests** to ensure the pipeline works end-to-end.
- **Domain tests** to confirm the project answers the intended music-trend questions.

We test less heavily:

- Pure formatting of printed output (we care more about the correctness of the underlying data).
- Extreme error conditions (completely corrupted CSVs, huge datasets), since they are outside the main project scope.

## How to Run Test Suite

All tests are plain Python files located in the `src/` directory:

- `src/test_unit_test.py`
- `src/test_integration_test.py`
- `src/test_system_test.py`
- `src/test_spotify_global_trends.py`

Each file can be run directly with Python or an IDE.

Example:
1. **Open the project in VS Code**
   - File -> Open Folder -> select the project folder (the one that contains `src/`).
2. **Make sure the correct Python environment is selected**
3. **Run each test file**
Running all four files this way constitutes the full test suite for the project.


## Test Results Summary

We ran four separate test files:

- `test_unit_test.py`  
  - **14 tests**, all **passed**.  
  - Covers core functions and classes such as `CSVManager`, `DataCleaner`, `DatabaseManagement`, and the `MusicItem` hierarchy.

- `test_integration_test.py`  
  - **4 tests**, all **passed** in the final run.  
  - These tests exercise the data pipeline across multiple components (CSV → clean DataFrame → SQLite → analysis).

- `test_spotify_global_trends.py`  
  - **8 tests**, all **passed**.  
  - Focuses on domain-specific behavior such as top genres per country and most popular artists.

- `test_system_test.py`  
  - System-level tests that run the full workflow; all current tests **pass**.  
  - Verifies that the whole pipeline completes without errors on a realistic dataset.

Overall, all automated tests are currently green.
In addition to the automated tests, we manually ran the full workflow script. The console output shows:

- Successful completion of all four main steps:
  1. **Load and clean** the CSV  
  2. **Save** cleaned data to the `spotify_cleaned` SQLite table  
  3. **Analyze** genres and artists with `MusicAnalyzer`  
  4. **Generate objects** (e.g., `ArtistItem` samples)

- Correct-looking analytical results, including:
  - **Top 5 genres per country** (e.g., Reggaeton dominating Spain, Hip Hop/Rap dominating the US).  
  - **Top genre per country** summary table.  
  - **Most common artist globally** (160 artists listed with counts).  
  - **Most popular artist per country** (e.g., Bad Bunny for Spain, Travis Scott for the US and South Africa).  
  - Sample `ArtistItem` objects with the expected song counts.

No crashes or unhandled exceptions occurred during these runs.
