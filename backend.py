# backend.py
from database_manager import DatabaseManager
from datetime import datetime
import random

class Backend:
    def __init__(self):
        self.db_manager = DatabaseManager('app_data.db')
        self.user_id = None
        self.flower_price = 1

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
    
    def get_all_entries(self):
        entries = self.db_manager.get_all_entries(self.user_id)
        return entries
    
    def get_points(self):
        return self.db_manager.get_points(self.user_id)
    
    def buy_flower(self, flower_number):
        points = self.db_manager.get_points(self.user_id)
        if points >= self.flower_price:
            self.db_manager.subtract_points(self.user_id, self.flower_price)
            flower_id = random.randint(1, 9)
            self.db_manager.add_flower(self.user_id, flower_number, flower_id)
