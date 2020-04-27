from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


class Design(BoxLayout):

    def change_text(self, inputText):
        inputText.text = f'they you have clicked a button'


root_kv = """
<Design>:
    orientation: 'vertical'
    TextInput:
        id: inputText
        text: 'hello'
        
    Button:
        id: clickButton
        text: 'click-me !'
        on_press: root.change_text(inputText)
Design:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(root_kv)


TestingApp().run()
