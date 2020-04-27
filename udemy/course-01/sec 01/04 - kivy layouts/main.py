from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Design(GridLayout):
    def __init__(self, **kwargs):
        super(Design, self).__init__(**kwargs)
        self.rows = 2
        self.text = TextInput(text='')
        self.button = Button(text='Click me')
        self.add_widget(self.text)
        self.add_widget(self.button)


class TestingApp(App):
    def build(self):
        return Design()


TestingApp().run()
