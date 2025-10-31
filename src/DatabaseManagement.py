class DatabaseManagement:
     """The functions that will be in this class:
    
    __init__(db_path: str)

    connect() -> sqlite3.Connection

    save_dataframe(df: pd.DataFrame, table_name: str, if_exists: str = "replace")

    close()
    
    
    """