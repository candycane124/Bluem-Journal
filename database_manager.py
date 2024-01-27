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

    def get_last_text_entry(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT text_entry FROM entries ORDER BY id DESC LIMIT 1")
        last_entry = cursor.fetchone()
        conn.close()
        return last_entry[0] if last_entry else "No entries found"
