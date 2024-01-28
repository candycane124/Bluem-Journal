# backend.py
from database_manager import DatabaseManager
from datetime import datetime
import random
from openai import OpenAI

class Backend:
    def __init__(self):
        self.db_manager = DatabaseManager('app_data.db')
        self.user_id = None
        self.entry_points_to_add = 2
        self.flower_price = 5

    def login(self, username):
        self.user_id = self.db_manager.login_or_create_user(username)

    def add_points(self, points_to_add):
        self.db_manager.add_points(self.user_id, points_to_add)

    def record_entry(self, entry_text):
        entry_date = datetime.now()
        self.db_manager.record_entry(self.user_id, entry_text, entry_date)
        self.db_manager.add_points(self.user_id, self.entry_points_to_add)

        current_points = self.db_manager.get_points(self.user_id)
        print(current_points)
    
    def get_last_entry(self):
        return self.db_manager.get_last_text_entry()
    
    def get_last_five_entries(self):
        entries = self.db_manager.get_last_five_entries(self.user_id)
        print(self.user_id)
        return entries
    
    def get_all_entries(self):
        entries = self.db_manager.get_all_entries(self.user_id)
        return entries
    
    def remove_entry(self, entry_id):
        self.db_manager.remove_entry(entry_id)
    
    def get_points(self):
        return self.db_manager.get_points(self.user_id)

    def buy_flower(self, pot_number):
        points = self.db_manager.get_points(self.user_id)
        if points >= self.flower_price:
            print("here")
            self.db_manager.subtract_points(self.user_id, self.flower_price)
            flower_id = random.randint(1, 9)
            self.db_manager.add_flower(self.user_id, pot_number, flower_id)

    def get_flower(self, pot_number):
        return self.db_manager.get_flower_id(self.user_id, pot_number)

    def query_chatgpt(self, current_journal_entry):
        client = OpenAI(
            # This is the default and can be omitted
            api_key='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',
        )

        try:
            chat_prompt = f"I have written a journal entry and I'm seeking a deeper reflection. Here is the entry: '{current_journal_entry}' Based on this, what is one impactful question you can ask to help me reflect further and think more deeply?"
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": chat_prompt,
                    }
                ],
            model="gpt-3.5-turbo",
            )
            
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return "How did that make you feel?"
