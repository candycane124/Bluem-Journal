from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
#from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
#from kivy.uix.image import AsyncImage


class StartScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class RootScreen(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootScreen()

if __name__ == "__main__":
    MainApp().run()