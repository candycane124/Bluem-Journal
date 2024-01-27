from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from backend import Backend

class MainWindow(Screen):
    pass

class JournalWindow(Screen):
    def save_btn_press(self):
        self.backend = Backend()
        entered_text = self.entry.text
        self.backend.record_entry(123, entered_text) # fix user id
        print(entered_text)
        self.entry.text = ""

class HistoryWindow(Screen):    
    def show_btn_press(self):
        self.backend = Backend()
        entries = self.backend.get_last_five_entries(123) # fix user id
        print(entries)
        finalStr = "" 
        for entry in entries:
            finalStr += entry[2] + "\n"
        self.entries.text = finalStr
    # pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        self.backend = Backend()
        entry = ObjectProperty(None)
        entries = ObjectProperty(None)
        return kv

if __name__ == "__main__":
    MyApp().run()
