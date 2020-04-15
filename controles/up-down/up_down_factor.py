# coding: utf-8

import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

kivy.require('1.11.1')

Window.clearcolor = [0, 0, .2, 1]


class UpDown(Widget):
    current = NumericProperty(0)
    factor_up = NumericProperty(10)
    factor_down = NumericProperty(-10)

    @staticmethod
    def get_valid_factor(value):
        try:
            var = int(value)
            return var
        except ValueError:
            return 0

    def change_factor_up(self, value):
        self.factor_up = UpDown.get_valid_factor(value)

    def increment_current_up(self):
        self.current += self.factor_up

    def change_factor_down(self, value):
        self.factor_down = UpDown.get_valid_factor(value)

    def increment_current_down(self):
        self.current += self.factor_down

    def command(self):
        pass


code = """
<FactorButton@BoxLayout>:
    orientation: 'vertical'
    command_btn: None
    command_txt: None
    factor: 0
    Button:
        text: str(root.factor)
        on_press: root.command_btn()
    TextInput:
        size_hint_y: .5
        text: str(root.factor)
        input_filter: 'int'
        multiline: False
        on_text_validate: root.command_txt(self.text)
    
<UpDown@Widget>:
    BoxLayout:
        orientation:'vertical'
        size_hint: (None, None)
        size:(root.width, root.height)
           
        Label:
            size_hint_y: .2
            text: str(root.current)
            
        BoxLayout:
            orientation: 'horizontal'
                
            FactorButton:
                factor: root.factor_down
                command_btn: root.increment_current_down
                command_txt: root.change_factor_down
                
            FactorButton:
                factor:root.factor_up
                command_btn: root.increment_current_up
                command_txt: root.change_factor_up
                
                
UpDown:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(code)


if __name__ == '__main__':
    TestingApp().run()
