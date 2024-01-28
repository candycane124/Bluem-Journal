from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import builder
from kivy.animation import Animation

Builder.load_file ('my.kv')

class PebbleImage(Image):
    def animate_it(self, *args):
        animate = Animation(
            size_hint=(0.5,0.7),
            duration=0.2
        )
        animate += Animation(
            size_hint=(0,0),
            duration=0.8
        )
        animate.start(self)