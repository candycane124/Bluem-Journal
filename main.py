from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from backend import Backend
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
            animate.start(pebble)
        except Exception as e:
           print(f"An error occured: {e}")
           import traceback
           traceback.print_exc()
    pass

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
