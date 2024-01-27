from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from backend import Backend
from kivy.core.window import Window
from kivy.properties import StringProperty

class MainWindow(Screen):
    def flower_pot_press(self):
        backend = App.get_running_app().backend
        backend.buy_flower(1) #fix user id

class Login(Screen):
    def save_btn_press(self):
        backend = App.get_running_app().backend
        user_id = self.entry.text
        backend.login(user_id)
        print(user_id)
        self.entry.text = ""

class JournalWindow(Screen):
    feeling_label_text = StringProperty("How are you feeling?")

    def save_btn_press(self):
        backend = App.get_running_app().backend
        entered_text = self.entry.text
        backend.record_entry(entered_text) # fix user id
        print(entered_text)
        self.entry.text = ""

    def ask_btn_press(self):
        backend = App.get_running_app().backend
        entered_text = self.entry.text
        #question_prompt = backend.question_prompt(entered_text)
        question_prompt = "New Question?"
        self.feeling_label_text = question_prompt

class HistoryWindow(Screen):    
    def show_btn_press(self):
        backend = App.get_running_app().backend
        entries = backend.get_last_five_entries() # fix user id
        print(entries)
        finalStr = "" 
        for entry in entries:
            finalStr += entry[2] + "\n"
        self.entries.text = finalStr
    # pass

class GratitudeJarApp(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    backend = None

    def build(self):
        self.backend = Backend()
        entry = ObjectProperty(None)
        entries = ObjectProperty(None)
        Window.size = (650, 400)
        return kv

if __name__ == "__main__":
    MyApp().run()
