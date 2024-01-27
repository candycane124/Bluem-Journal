from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

class GratitudeJarApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10, 
            size_hint_y=None, 
            height=500, 
            )
        background_image= Image(source='garden background.png',
                                                                size=(1000, 800),
                                size_hint_x=None,
                                size_hint_y=None,
                                allow_stretch=True,
                                keep_ratio=False)
        layout.add_widget(background_image)

        # Create a label for instructions
        instructions = Label(text='What are you grateful for today?', font_size=20,)
        layout.add_widget(instructions)

        # Create a text input for user entry
        self.gratitude_input = TextInput(hint_text='Enter your gratitude...', multiline=False, font_size=14)
        layout.add_widget(self.gratitude_input)

        # Create a button to add the entry
        add_button = Button(text='Add Gratitude',
                            on_press=self.add_gratitude,
                            font_size=14,
                            background_color=(0, 1, 0, 1)
                            )
        layout.add_widget(add_button)

        # Create a label to display gratitude entries
        self.gratitude_display = Label(text='', font_size=14)
        layout.add_widget(self.gratitude_display)

        return layout

    def add_gratitude(self, instance):
        # Get the gratitude entry from the input field
        gratitude_text = self.gratitude_input.text

        # Check if the input is not empty
        if gratitude_text:
            # Display the gratitude entry
            self.gratitude_display.text += f'\n- {gratitude_text}'

            # Clear the input field
            self.gratitude_input.text = ''

if __name__ == '__main__':
    GratitudeJarApp().run()

