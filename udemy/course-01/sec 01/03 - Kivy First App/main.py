from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class TestingApp(App):
    def build(self):
        return Button(text='click me')


TestingApp().run()
