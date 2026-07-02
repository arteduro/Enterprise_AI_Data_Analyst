"""
core/database.py
Administrador de SQLite para Enterprise AI Data Analyst.
"""
import sqlite3
from pathlib import Path
from .settings import settings
from .logger import LoggerManager

class DatabaseManager:
    def __init__(self):
        settings.create_directories()
        self.logger = LoggerManager.get_logger("Database")
        self.db_path = Path(settings.SQLITE_PATH)
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.logger.info("Conexión SQLite establecida.")
        return self.connection

    def initialize(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS projects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS analysis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            dataset_name TEXT,
            model_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        self.logger.info("Base de datos inicializada.")

    def execute(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        return cur

    def fetchall(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()
            self.logger.info("Conexión cerrada.")
