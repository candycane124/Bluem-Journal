# backend.py
from database_manager import DatabaseManager
from datetime import datetime

class Backend:
    def __init__(self):
        self.db_manager = DatabaseManager('app_data.db')

    def record_entry(self, user_id, entry_text):
        entry_date = datetime.now()
        self.db_manager.record_entry(user_id, entry_text, entry_date)
        self.db_manager.add_points(user_id)
    
    def get_last_entry(self):
        return self.db_manager.get_last_text_entry()
    
    def get_last_five_entries(self, user_id):
        entries = self.db_manager.get_last_five_entries(user_id)
        return entries
    
    def get_points(self, user_id):
        return self.db_manager.get_points(user_id)
