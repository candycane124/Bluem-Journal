from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from backend import Backend
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class MainWindow(Screen):
    point_txt = "Points: 0"
    
    def auto_update(self):
        backend = App.get_running_app().backend
        point = backend.get_points()
        self.point_txt = "Points: " + str(point)

    # Clock.schedule_interval(auto_update, 1)   automatically check the point and update every 1 sec
        
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
        current_journal_entry = self.entry.text
        question_prompt = backend.query_chatgpt(current_journal_entry)
        #question_prompt = "New Question?"
        self.feeling_label_text = question_prompt

class HistoryWindow(Screen):
    def addLabels(self):
        self.entries.clear_widgets()
        backend = App.get_running_app().backend
        entries = backend.get_all_entries()
        for entry in entries:
            item = OneLineListItem(text=entry[2])
            setattr(item, 'entry_id', entry[0])
            item.bind(on_press=lambda x, item=item: self.confirm_delete(item))
            self.entries.add_widget(item)

    def confirm_delete(self, item):
        dialog = MDDialog(
            title="Delete Entry",
            text="Would you like to delete this entry? This action is irreversible.",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text="CONFIRM",
                    on_release=lambda x: self.delete_entry(item, dialog)
                ),
            ],
        )
        dialog.open()

    def delete_entry(self, item, dialog):
        dialog.dismiss()
        backend = App.get_running_app().backend
        backend.remove_entry(item.entry_id)
        self.entries.remove_widget(item)


class GratitudeJarApp(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(MDApp):
    backend = None

    def build(self):
        self.backend = Backend()
        self.title = "name goes here"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        Window.size = (650, 400)
        return Builder.load_file("my.kv")

if __name__ == "__main__":
    MyApp().run()
