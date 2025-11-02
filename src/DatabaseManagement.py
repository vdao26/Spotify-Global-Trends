import sqlite3
import pandas as pd
import os

class DatabaseManagement:
    """This class handles the database operations.

    Methods
    -------
    __init__(db_path: str)
    connect() -> sqlite3.Connection
    save_dataframe(df: pd.DataFrame, table_name: str, if_exists: str = "replace")
    close()
    """

    def __init__(self, db_path: str= "SpotifyTopSongsByCountry - May 2020.csv.db"):
        """Initialize the DatabaseManagement with the path to the database file.
        Args:
            db_path (str): Path to the SQLite database file.
        Raises:
            ValueError: If db_path is not a string.
        """
        if not isinstance(db_path, str):
            raise ValueError("db_path must be a string")
        self.db_path = db_path
        self.conn = None

    def connect(self) -> sqlite3.Connection:
        """Open a SQLite connection and return it (reuses existing connection)."""
        if self.conn is None:
            # Ensure directory exists when a directory component is provided
            dirpath = os.path.dirname(self.db_path)
            if dirpath:
                os.makedirs(dirpath, exist_ok=True)
            self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def save_dataframe(self, df: pd.DataFrame, table_name: str, if_exists: str = "replace"):
        """Save a pandas DataFrame to the specified table in the database."""
        if not isinstance(df, pd.DataFrame):
            raise TypeError("df must be a pandas DataFrame")
        conn = self.connect()
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)

    def close(self):
        """Close the database connection if open."""
        if self.conn:
            self.conn.close()
            self.conn = None
    @property
    def database_path(self) -> str:
        """Get the path to the database file."""
        return self.db_path
    @property
    def connection(self) -> sqlite3.Connection:
        """Get the current database connection."""
        return self.conn
    
    # --- C0RE FUNCTIONS --- #
    def execute_query(self, query: str):
        """Execute a SQL query on the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()
    def fetch_table(self, table_name: str) -> pd.DataFrame:
        """Fetch all data from a specified table as a pandas DataFrame."""
        conn = self.connect()
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(query, conn)
    def table_exists(self, table_name: str) -> bool:
        """Check if a table exists in the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name=?;
        """, (table_name,))
        return cursor.fetchone() is not None
    def delete_table(self, table_name: str):
        """Delete a table from the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
    def list_tables(self) -> list:
        """List all tables in the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table';
        """)
        tables = cursor.fetchall()
        return [table[0] for table in tables]
