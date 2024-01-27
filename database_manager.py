# database_manager.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text_entry TEXT NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

    def store_text(self, text):
        conn = sqlite3.connect(self.db_name)
        conn.execute('INSERT INTO entries (text_entry) VALUES (?);', (text,))
        conn.commit()
        conn.close()
