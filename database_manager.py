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
                points INTEGER DEFAULT 0,
                streak INTEGER DEFAULT 0,
                flower1 INTEGER DEFAULT 0,
                flower2 INTEGER DEFAULT 0,
                flower3 INTEGER DEFAULT 0
            );
        ''')

        # Create 'journal entries' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS journal_entries (
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

        # Create the 'flowers' table
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flowers (
                id INTEGER PRIMARY KEY,
                image_path TEXT NOT NULL
            );
        ''')

        # Populate the 'flowers' table if it is empty
        self.populate_flowers_table(conn)

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
    
    def get_last_five_entries(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM journal_entries WHERE user_id = ? ORDER BY entry_date DESC LIMIT 5", (user_id,))
        entries = cursor.fetchall()

        conn.close()
        return entries

    def get_all_entries(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM journal_entries WHERE user_id = ? ORDER BY entry_date DESC", (user_id,))
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
    
    def check_table_empty_flowers(self, conn):
        # Check if the flowers table is empty
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM flowers')
        count = cursor.fetchone()[0]
        return count == 0

    def populate_flowers_table(self, conn):
            # Check if the flowers table is empty
            if self.check_table_empty_flowers(conn):
                # Insert flower images
                for i in range(1, 10):
                    image_path = f"flowers/f{i}.png"
                    conn.execute('INSERT INTO flowers (image_path) VALUES (?)', (image_path,))

    def subtract_points(self, user_id, flower_price):
        """ Remove the price of a flower from the user """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Subtract points from the user's current points
        cursor.execute('UPDATE users SET points = points - ? WHERE user_id = ?', (flower_price, user_id,))

        conn.commit()
        conn.close()

    def add_flower(self, user_id, flower_number, flower_id):
        """ Add a flower to the specified user """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Update the specific flower column for the user
        cursor.execute(f'UPDATE users SET flower{flower_number} = ? user_id = ?', (flower_id, user_id,))

        conn.commit()
        conn.close()