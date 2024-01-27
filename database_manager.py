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
                points INTEGER DEFAULT 0
                streak INTEGER DEFAULT 0
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

        

    def record_entry(self, user_id, entry_text, entry_date):
        conn = sqlite3.connect(self.db_name)
        conn.execute('INSERT INTO journal_entries (user_id, entry_text, entry_date) VALUES (?, ?, ?);', (user_id, entry_text, entry_date))
        conn.commit()
        conn.close()

    def get_last_text_entry(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT text_entry FROM entries ORDER BY id DESC LIMIT 1")
        last_entry = cursor.fetchone()
        conn.close()
        return last_entry[0] if last_entry else "No entries found"
    
    def get_last_5_entries(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM journal_entries WHERE user_id = ? ORDER BY entry_date DESC LIMIT 5", (user_id,))
        entries = cursor.fetchall()

        conn.close()
        return entries
    
    def get_points(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT points FROM users WHERE user_id = ? ORDER BY entry_date DESC LIMIT 5", (user_id,))
        result = cursor.fetchone()

        conn.close()
        return result
    
    def add_points(self, user_id, points_to_add):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points_to_add, user_id))
        result = cursor.fetchone()

        conn.close()
        return result
    




