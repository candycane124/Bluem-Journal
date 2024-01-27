# main.py
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from backend import Backend

kivy.require('2.0.0')

class SimpleApp(App):
    def build(self):
        self.backend = Backend()
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text='Enter text below and press the button')
        self.textinput = TextInput(text='', multiline=False)
        btn = Button(text='Submit')
        btn.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        entered_text = self.textinput.text
        result = self.backend.save_text(entered_text)
        self.label.text = result

if __name__ == '__main__':
    SimpleApp().run()
