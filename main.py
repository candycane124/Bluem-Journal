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

        save_btn = Button(text='Submit')
        save_btn.bind(on_press=self.on_save_button_press)

        self.last_entry_label = Label(text='Last entry will be shown here')

        show_last_entry_btn = Button(text='Show Last Entry')
        show_last_entry_btn.bind(on_press=self.on_show_last_entry_press)

        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(save_btn)
        layout.add_widget(self.last_entry_label)
        layout.add_widget(show_last_entry_btn)

        return layout

    def on_save_button_press(self, instance):
        entered_text = self.textinput.text
        result = self.backend.save_text(entered_text)
        self.label.text = result

    def on_show_last_entry_press(self, instance):
        last_entry = self.backend.get_last_entry()
        self.last_entry_label.text = f"Last entry: {last_entry}"

if __name__ == '__main__':
    SimpleApp().run()
