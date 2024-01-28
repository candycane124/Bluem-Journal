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
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from kivy.uix.widget import Widget

class MainWindow(Screen):
    point_txt = StringProperty("Points: 0")
    streak_txt = StringProperty("Streak: 0")

    def auto_update(self, dt):
        backend = App.get_running_app().backend
        point = backend.get_points()
        self.point_txt = f"Points: {point}"

        f1 = backend.get_flower(1)
        f2 = backend.get_flower(2)
        f3 = backend.get_flower(3)
        print(f"1: {f1}\n2: {f2}\n3: {f3}")
    
    def on_enter(self):
        self.auto_update(0)  # Pass dt=0 to simulate an immediate update

        Clock.schedule_interval(self.auto_update, 1)

    
    def flower_pot_press(self, button):
        backend = App.get_running_app().backend
        print(button.btn_id)
        dialog = MDDialog(
            title="Plant Seed",
            text="Would you like to buy a new random new flower for 10 points?",
            buttons=[
                MDFlatButton(
                    text="NO",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text="YES",
                    on_release=lambda x: backend.buy_flower(button.btn_id)
                ),
            ],
        )
        dialog.open()

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
            item.theme_text_color = "Custom"
            item.text_color: (0.3, 0.6, 0.6, 1)  
            self.entries.add_widget(item)

    def confirm_delete(self, item):
        dialog = MDDialog(
            title="Delete Entry?",
            # text="Would you like to delete this entry? This action is irreversible.",
            text=item.text,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text="CONFIRM (IRREVERSIBLE)",
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


# class PebbleImage(Image):
#     def animate_it(self, *args):
#         animate = Animation(
#             size_hint=(0.5,0.7),
#             duration=0.2
#         )
#         animate += Animation(
#             size_hint=(0,0), 
#             duration=0.8
#         )
#         animate.start(self)
    
class NegativityPebbleApp(Screen):
    # class PebbleImage(Image):
    # def animate_it(self, *args):
    #         animate = Animation(
    #             size_hint=(0.5,0.7),
    #             duration=0.2
    #         )
    #         animate += Animation(
    #             size_hint=(0,0),
    #             duration=0.8
    #         )
    #         animate.start(self)

    # def animate_it(self, *args):
    #     self.ids.pebble.animate_it()
        # animate = Animation(
        #     size_hint=(0.5,0.7),
        #     duration=0.2
        # )
        # animate += Animation(
        #     size_hint=(0,0),
        #     duration=0.8
        # )
        # animate.start(self)

    def throw_action(self):
        try:
            negative_thought = self.ids.negative_message.text
            print(negative_thought)
            # self.ids.throww.text = (negative_thought)
            self.ids.heading.opacity=0
            self.ids.heading.disabled=True
            self.ids.negative_message.opacity=0
            self.ids.negative_message.disabled=True
            self.ids.throw_button.opacity=0
            self.ids.throw_button.disabled=True
            # self.ids.pebble.animate_it()
            animate = Animation(
                size_hint=(0.5,0.7),
                duration=0.2
            )
            animate += Animation(
                size_hint=(0,0),
                duration=0.8
            )
            animate.start(self.ids.pebble)
        except Exception as e:
           print(f"An error occured: {e}")
           import traceback
           traceback.print_exc()
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
