from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.uix.label import Label
from backend import Backend
import random

class MainWindow(Screen):
    pass

class Login(Screen):
    def save_btn_press(self):
        backend = App.get_running_app().backend
        user_id = self.entry.text
        backend.login(user_id)
        print(user_id)
        self.entry.text = ""

class JournalWindow(Screen):

    prompt_file = open("prompts.txt","r")
    prompts = prompt_file.read().split(", ")
    prompt_file.close()

    def save_btn_press(self):
        backend = App.get_running_app().backend
        entered_text = self.entry.text
        backend.record_entry(entered_text)
        print(entered_text)
        self.entry.text = ""
    
    def new_prompt(self):
        self.prompt.text = self.prompts[random.randint(0,199)]

class HistoryWindow(Screen):    
    def show_btn_press(self):
        backend = App.get_running_app().backend
        entries = backend.get_last_five_entries()
        print(entries)
        finalStr = "" 
        for entry in entries:
            finalStr += entry[2] + "\n"
        self.entries.text = finalStr
    
    def addLabels(self):
        self.entries.clear_widgets()
        backend = App.get_running_app().backend
        entries = backend.get_all_entries()
        for entry in entries:
            self.entries.add_widget(OneLineListItem(text = entry[2]))

class GratitudeJarApp(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    backend = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        self.backend = Backend()
        return Builder.load_file("my.kv")

if __name__ == "__main__":
    MyApp().run()
