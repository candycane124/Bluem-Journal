import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Ensure you are using the correct version of Kivy
kivy.require('2.0.0')

class SimpleApp(App):
    def build(self):
        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a Label
        self.label = Label(text='Enter text below and press the button')

        # Create a TextInput
        self.textinput = TextInput(text='', multiline=False)

        # Create a Button and attach a callback for when the button is pressed
        btn = Button(text='Submit')
        btn.bind(on_press=self.on_button_press)

        # Add the widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        # Update the label text with the text from the TextInput when the button is pressed
        entered_text = self.textinput.text
        self.label.text = f'You entered: {entered_text}'

# Run the app
if __name__ == '__main__':
    SimpleApp().run()
