import sqlite3
import pandas as pd
from .data_handlers import DataHandler
import json

class SQLiteHandler(DataHandler):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def load_data(self, query: str) -> pd.DataFrame:
        with sqlite3.connect(self.db_path) as conn:
            return pd.read_sql_query(query, conn)

    def save_data(self, data: pd.DataFrame, table_name: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            data.to_sql(table_name, conn, if_exists='replace', index=False)

