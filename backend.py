# backend.py
from database_manager import DatabaseManager
from datetime import datetime

class Backend:
    def __init__(self):
        self.db_manager = DatabaseManager('app_data.db')
        self.user_id = None

    def login(self, user_id):
        self.user_id = user_id

    def record_entry(self, entry_text):
        entry_date = datetime.now()
        self.db_manager.record_entry(self.user_id, entry_text, entry_date)
        points_to_add = 1 # random will need to change
        self.db_manager.add_points(self.user_id, points_to_add)
    
    def get_last_entry(self):
        return self.db_manager.get_last_text_entry()
    
    def get_last_five_entries(self):
        entries = self.db_manager.get_last_five_entries(self.user_id)
        print(self.user_id)
        return entries
    
    def get_points(self):
        return self.db_manager.get_points(self.user_id)
