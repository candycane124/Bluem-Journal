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
        # TO-DO: store 'entered_text'/'self.entry.text' to database
        entered_text = self.entry.text
        self.backend.save_text(entered_text) # doesn't work right now
        print(entered_text)
        self.entry.text = ""

class HistoryWindow(Screen):    
    def show_btn_press(self):
        self.backend = Backend()
        # TO-DO: get entries from database and set 'self.entries.text' equal to it
        last_entry = self.backend.get_last_entry()
        self.entries.text = last_entry
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
