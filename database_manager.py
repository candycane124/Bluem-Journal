# database_manager.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create the 'users' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                email TEXT,
                points INTEGER DEFAULT 0
            );
        ''')

        cursor.execute('''
            CREATE TABLE journal_entries (
                entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                entry_text TEXT NOT NULL,
                entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            );
        ''')

         # Create the 'journal_prompts' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS journal_prompts (
                prompt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt_text TEXT NOT NULL
            );
        ''')

        # Create the 'hints' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hints (
                hint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                hint_text TEXT NOT NULL
            );
        ''')

        # Commit the changes and close the connection
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
