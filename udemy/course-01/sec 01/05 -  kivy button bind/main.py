from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Design(GridLayout):
    def __init__(self, **kwargs):
        super(Design, self).__init__(**kwargs)
        self.rows = 2
        self.user_input = TextInput(text='')
        self.button = Button(text='Click me')
        self.add_widget(self.user_input)
        self.add_widget(self.button)
        self.button.bind(on_press=self.change_text)

    def change_text(self, instance):
        self.user_input.text = f'they you have clicked a button {instance}'


class TestingApp(App):
    def build(self):
        return Design()

TestingApp().run()