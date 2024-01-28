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
        if f1 != 0:
            image_widget = self.ids.flower1
            image_widget.source = f'flowers/f{f1}.png'

        f2 = backend.get_flower(2)
        if f2 != 0:
            image_widget = self.ids.flower2
            image_widget.source = f'flowers/f{f2}.png'

        f3 = backend.get_flower(3)
        if f3 != 0:
            image_widget = self.ids.flower3
            image_widget.source = f'flowers/f{f3}.png'

    def on_enter(self):
        self.auto_update(0)  # Pass dt=0 to simulate an immediate update

        Clock.schedule_interval(self.auto_update, 1)

    def buy_flower(self, pot_number):
        backend = App.get_running_app().backend
        buy_success = backend.buy_flower(pot_number)
        if not buy_success:
            dialog = MDDialog(
                title="Not enough points",
                text="Sorry, but you don't have enough points to buy a new seed. Keep journaling to earn more points!",
                buttons=[
                    MDFlatButton(
                        text="Okay",
                        on_release=lambda x: dialog.dismiss()
                    ),
                ],
            )
            dialog.open()

    def flower_pot_press(self, button):
        backend = App.get_running_app().backend
        print(button.btn_id)
        dialog = MDDialog(
            title="Plant Seed",
            text="Would you like to buy a new random new flower for 5 points?",
            buttons=[
                MDFlatButton(
                    text="NO",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text="YES",
                    on_press=lambda x: self.buy_flower(button.btn_id),
                    on_release=lambda x: dialog.dismiss()
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
        backend.record_entry(entered_text)
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


class NegativityPebbleApp(Screen):
    def reset_page(self):
        self.ids.negative_message.text=""
        self.ids.negative_message.opacity=1
        self.ids.negative_message.disabled=False
        self.ids.heading.opacity=1
        self.ids.heading.disabled=False
        self.ids.throw_button.opacity=1
        self.ids.throw_button.disabled=False
        self.ids.message.opacity=0
        #reset pebble
        self.ids.pebble.size_hint=(0.35,0.5)
        self.ids.pebble.pos_hint={'center_x': 0.5, 'center_y': 0.5} 
        self.ids.pebble.opacity=1

    def on_enter(self, *args):
        self.reset_page()

    def add_points(self):
        backend = App.get_running_app().backend
        backend.add_points(1)

    def throw_action(self):
        try:
            negative_thought = self.ids.negative_message.text
            print(negative_thought)
            self.ids.heading.opacity=0
            self.ids.heading.disabled=True
            self.ids.negative_message.opacity=0
            self.ids.negative_message.disabled=True
            self.ids.throw_button.opacity=0
            self.ids.throw_button.disabled=True
            self.ids.pebble.opacity=0
            self.ids.pebble.disabled=True
            self.ids.chew.opacity=1
            animate = Animation(
                size_hint=(0.45,0.65),
                duration=0.5
            )
            animate += Animation(
                size_hint=(0.15,0.23),
                duration=0.25
            )
            animate += Animation(
                size_hint=(0,0),
                pos_hint={'center_y':0.35},
                duration=0.34
            )
            animate.start(self.ids.chew)
            fade = Animation(
                opacity=1,
                duration=2.5 
            )
            fade.start(self.ids.message)
            # fade = Animation(
            #     opacity=1,
            #     duration=2
            # )
            # fade.start(self.ids.message)
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
        self.title = "Bluem"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        Window.size = (650, 400)
        return Builder.load_file("my.kv")

if __name__ == "__main__":
    MyApp().run()
